# SSH into Android Termux using Netmiko

This mini project uses Python and Netmiko to SSH into an Android device running Termux, execute a hard-coded command string, return the output, and write logs.

The goal is simple:

```text
Python script -> Netmiko SSH connection -> Android Termux SSH server -> run command -> return output
```

This project was originally written with Paramiko. It has now been converted to Netmiko.

---

## Current command being executed

Inside `command_execution.py`, the command is hard-coded:

```python
COMMAND = "uptime; date; date +%Z; date +%z; whoami"
```

This command gives basic information from the Android Termux shell:

```text
uptime      -> shows how long the system/session has been running
date        -> shows current date and time
date +%Z    -> shows timezone name, for example IST
date +%z    -> shows timezone offset, for example +0530
whoami      -> shows the current Termux SSH user
```

The semicolon `;` lets the remote shell run multiple commands one after another.

---

## Project files

```text
android_conn.py          -> creates and returns the Netmiko SSH connection
command_execution.py     -> imports android_conn and runs the hard-coded command
requirements.txt         -> Python dependencies
logs/ssh_android.log     -> log file created when the program runs
```

---

## Requirements

### On Android Termux

Install and start the SSH server:

```bash
pkg update
pkg install openssh
sshd
```

If you have not set a Termux password yet, run:

```bash
passwd
```

Termux SSH usually runs on port:

```text
8022
```

Check your Termux username:

```bash
whoami
```

Check your Android device IP address:

```bash
ip addr
```

You will need:

```text
host      -> Android device IP address
user      -> Termux username
password  -> Termux SSH password
port      -> usually 8022
```

---

### On your computer

Install dependencies:

```bash
pip install -r requirements.txt
```

`requirements.txt`:

```text
netmiko
```

---

## Running the program

Run:

```bash
python command_execution.py
```

The program will ask for:

```text
Hostname:
Username:
Password:
```

Example:

```text
Hostname: 192.168.1.20
Username: u0_a123
Password:
```

The password is entered using `getpass`, so it should not be displayed in the terminal.

---

## Example output

The output may look like this:

```text
send_command_timing
up 2 hours, 35 minutes
Fri Jun  5 18:45:21 IST 2026
IST
+0530
u0_a123
Log saved to: logs/ssh_android.log
```

The exact output depends on your Android device and Termux environment.

---

# What is Netmiko?

Netmiko is a Python library used for SSH automation.

It is built on top of Paramiko, but it gives a simpler interface for connecting to devices and running commands.

Instead of manually creating a raw SSH client, opening channels, reading stdout, and closing the client, Netmiko gives methods such as:

```python
ConnectHandler(...)
connection.send_command_timing(...)
connection.disconnect()
```

Netmiko is commonly used for network devices such as routers, switches, and firewalls. However, Netmiko also supports a `linux` device type, which is why this project uses:

```python
DEVICE_TYPE = "linux"
```

Official documentation:

```text
Netmiko documentation:
https://ktbyers.github.io/netmiko/docs/netmiko/

Netmiko supported platforms:
https://github.com/ktbyers/netmiko/blob/develop/PLATFORMS.md

Netmiko BaseConnection methods:
https://ktbyers.github.io/netmiko/docs/netmiko/base_connection.html
```

---

# Why we converted from Paramiko to Netmiko

The earlier version used Paramiko directly.

Paramiko version:

```python
client = paramiko.SSHClient()
client.connect(...)
_, stdout, stderr = client.exec_command(COMMAND)
client.close()
```

Netmiko version:

```python
connection = ConnectHandler(**device)
output = connection.send_command_timing(COMMAND)
connection.disconnect()
```

The Netmiko version is cleaner because:

1. `ConnectHandler` creates the right connection object using `device_type`.
2. `send_command_timing()` handles command execution and output reading.
3. `disconnect()` cleanly closes the SSH connection.
4. The code is closer to network automation style.

---

# Code explanation

## `android_conn.py`

This file is responsible only for creating and returning the SSH connection.

It does not run commands.

### Imports

```python
import logging
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException
```

Meaning:

```text
logging                         -> writes program activity to logs
ConnectHandler                  -> creates the Netmiko SSH connection
NetmikoAuthenticationException  -> handles wrong username/password errors
NetmikoTimeoutException         -> handles timeout or unreachable device errors
```

---

## `connect_to_mobile()`

```python
def connect_to_mobile(host, user, port=8022, password=None, device_type="linux"):
```

This function accepts:

```text
host         -> Android device IP address
user         -> Termux username
port         -> SSH port, usually 8022
password     -> Termux SSH password
device_type  -> Netmiko device type, set to linux
```

---

## Netmiko device dictionary

```python
device = {
    "device_type": device_type,
    "host": host,
    "username": user,
    "password": password,
    "port": port,
    "conn_timeout": 10,
    "auth_timeout": 10,
    "banner_timeout": 15,
    "timeout": 30,
    "fast_cli": False,
    "ssh_strict": False,
    "system_host_keys": True,
}
```

This dictionary tells Netmiko how to connect.

Important fields:

```text
device_type       -> tells Netmiko what type of device this is
host              -> Android IP address
username          -> Termux username
password          -> Termux SSH password
port              -> Termux SSH port
conn_timeout      -> connection timeout
auth_timeout      -> authentication timeout
banner_timeout    -> SSH banner timeout
timeout           -> general timeout
fast_cli          -> disabled for better reliability
ssh_strict        -> false so unknown host keys do not stop the learning project
system_host_keys  -> uses system host keys when available
```

---

## Create the connection

```python
connection = ConnectHandler(**device)
```

`ConnectHandler` is Netmiko's factory function.

It reads `device_type` and creates the proper connection class.

For this project, the device type is:

```python
"linux"
```

That is used because Android Termux behaves like a Linux-style SSH shell.

---

## Return the connection

```python
return connection
```

`android_conn.py` returns the connected Netmiko object to `command_execution.py`.

The command execution happens in `command_execution.py`.

---

## Error handling in `android_conn.py`

The connection file handles common Netmiko errors:

```python
except NetmikoAuthenticationException:
    logger.exception("Netmiko authentication failed")
    raise

except NetmikoTimeoutException:
    logger.exception("Netmiko connection timed out")
    raise
```

This makes logs easier to understand when something fails.

---

# `command_execution.py`

This file imports the connection function and runs the command.

---

## Logging setup

The program creates a `logs` directory and writes logs to:

```text
logs/ssh_android.log
```

Code:

```python
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "ssh_android.log"
```

This keeps log files organized instead of writing them directly beside the Python files.

---

## Important constants

```python
PORT = 8022
DEVICE_TYPE = "linux"
COMMAND = "uptime; date; date +%Z; date +%z; whoami"
EXECUTION_METHOD = "send_command_timing"
```

Meaning:

```text
PORT              -> Termux SSH port
DEVICE_TYPE       -> Netmiko device type
COMMAND           -> command string sent to Android Termux
EXECUTION_METHOD  -> Netmiko command method being used
```

---

## Why `send_command_timing()` is used

The project uses:

```python
connection.send_command_timing(
    COMMAND,
    read_timeout=30,
    last_read=2,
    strip_prompt=True,
    strip_command=True,
)
```

`send_command_timing()` is delay-based.

That means Netmiko keeps reading output until no new data appears for a short time.

This is useful for Termux/Linux shell output because it avoids relying too heavily on network-device-style prompts.

Parameters:

```text
COMMAND        -> command to run
read_timeout   -> maximum time to wait for output
last_read      -> final wait after output appears to be done
strip_prompt   -> remove the shell prompt from output when possible
strip_command  -> remove the command itself from output when possible
```

---

## Optional method: `send_command()`

The file also allows this method:

```python
EXECUTION_METHOD = "send_command"
```

`send_command()` waits for an expected prompt pattern.

For simple Termux usage, `send_command_timing()` is usually easier.

---

## Closing the connection

At the end, the program closes the SSH connection:

```python
if connection:
    connection.disconnect()
    logger.info("Netmiko SSH connection disconnected")
```

This replaces the old Paramiko style:

```python
client.close()
```

---

# Paramiko vs Netmiko

## Paramiko

Paramiko is a lower-level SSH library.

With Paramiko, you usually do these steps manually:

```text
create SSH client -> connect -> execute command -> read stdout/stderr -> close client
```

Example:

```python
_, stdout, stderr = client.exec_command(COMMAND)
```

---

## Netmiko

Netmiko is built for network automation and gives a higher-level command interface.

With Netmiko, this project does:

```text
create Netmiko connection -> send command -> receive output -> disconnect
```

Example:

```python
output = connection.send_command_timing(COMMAND)
```

---

## Simple rule

```text
Paramiko  -> lower-level SSH automation
Netmiko   -> higher-level network automation built on SSH
```

For this project:

```text
Android Termux SSH server -> Netmiko with device_type="linux"
```

---

# Logging

The program writes logs to:

```text
logs/ssh_android.log
```

Example log messages:

```text
Program started
Execution method selected: send_command_timing
Command to execute: uptime; date; date +%Z; date +%z; whoami
Connected to Android device using Netmiko
Command executed successfully
Netmiko SSH connection disconnected
```

Logs are helpful for debugging connection failures, authentication failures, command timeouts, and output issues.

Recommended `.gitignore` entry:

```gitignore
logs/
__pycache__/
```

---

# Troubleshooting

## `Netmiko authentication failed`

Possible causes:

```text
Wrong username
Wrong password
Termux password not set
SSH server not running
```

Fix:

```bash
passwd
sshd
```

Then try again.

---

## `Netmiko connection timed out`

Possible causes:

```text
Wrong IP address
Phone and computer are on different networks
Termux SSH server is not running
Wrong port
Firewall or hotspot issue
```

Check Termux SSH:

```bash
sshd
```

Check IP address:

```bash
ip addr
```

Try port:

```text
8022
```

---

## Command times out

If the command takes too long, increase `read_timeout`:

```python
output = connection.send_command_timing(
    COMMAND,
    read_timeout=60,
    last_read=2,
)
```

---

## Output contains prompts or repeated commands

Try changing these values:

```python
strip_prompt=True
strip_command=True
```

If needed, set them to `False` to debug the raw output.

---

# Security notes

Do not hard-code real passwords in the code.

This project prompts for the password at runtime:

```python
password = getpass("Password: ")
```

For real projects, prefer:

```text
SSH keys
environment variables
a secrets manager
```

Do not commit logs if they contain sensitive data.

---

# Final notes

This project now uses Netmiko instead of Paramiko.

Main changes:

```text
paramiko.SSHClient()       -> netmiko.ConnectHandler()
client.exec_command()      -> connection.send_command_timing()
client.close()             -> connection.disconnect()
paramiko exceptions        -> netmiko exceptions
ssh_android.log beside app -> logs/ssh_android.log
```

The project still connects to Android Termux over SSH and runs a read-only command string.