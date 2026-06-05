# SSH into Android Termux using Paramiko

This mini project uses Python and Paramiko to SSH into an Android device running Termux and execute a hard-coded command string.

The goal is simple:

```text
Python script -> Android Termux SSH server -> run command -> return output
```

Currently, the project runs simple read-only commands such as:

```bash
uptime; date; date +%Z; date +%z; whoami; pwd; uname -a
```

These commands give basic information such as:

- Device uptime
- Current date and time
- Time zone name
- Time zone offset
- Current SSH user
- Current working directory
- Kernel/system information

---

## Project files

```text
android_conn.py          -> handles SSH connection
command_execution.py     -> imports android_conn and runs a hard-coded command
```

---

## What this program does

The program:

1. Creates an SSH client using Paramiko.
2. Connects to the Android device running Termux.
3. Runs one hard-coded command string on the Android device.
4. Reads the command output.
5. Reads possible errors.
6. Closes the SSH connection.

---

## Current command being executed

Inside `command_execution.py`, the command is hard-coded:

```python
COMMAND = "uptime; date; date +%Z; date +%z; whoami; pwd; uname -a"
```

Even though this contains multiple shell commands, it is still sent using one Paramiko call:

```python
client.exec_command(COMMAND)
```

The semicolon `;` lets the remote shell run the commands one after another.

---

## Requirements

### On Android Termux

Install and start the SSH server:

```bash
pkg update
pkg install openssh
sshd
```

Termux SSH usually runs on port:

```text
8022
```

You can check your Termux username with:

```bash
whoami
```

You can check your Android device IP address with:

```bash
ip addr
```

---

### On your computer

Install Paramiko:

```bash
pip install paramiko
```

---

# Code explanation

## `android_conn.py`

This file is responsible only for creating and returning the SSH connection.

---

### Import Paramiko

```python
import paramiko
```

Paramiko is the Python library used to create the SSH connection.

---

### Create the connection function

```python
def connect_to_mobile(host, user, port=8022, password=None):
```

This function accepts:

```text
host      -> Android device IP address
user      -> Termux username
port      -> SSH port, usually 8022
password  -> Termux SSH password
```

---

### Create the SSH client

```python
client = paramiko.SSHClient()
```

This creates a Paramiko SSH client object.

The client is used to connect to the Android device.

---

### Load known SSH host keys

```python
client.load_system_host_keys()
```

This loads trusted SSH host keys from your computer, usually from:

```text
~/.ssh/known_hosts
```

SSH host keys help verify that you are connecting to the correct device.

---

### Automatically trust unknown hosts

```python
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
```

This tells Paramiko to automatically trust the Android device if it has not been seen before.

This is convenient for learning and home projects.

For production use, this is less secure because it automatically trusts new SSH servers.

---

### Connect to the Android device

```python
client.connect(
    hostname=host,
    port=port,
    username=user,
    password=password,
    timeout=10,
)
```

This connects to the Termux SSH server using the provided details.

---

### Return the connected client

```python
return client
```

This is important.

`android_conn.py` does not run commands anymore.

It only connects and returns the connected SSH client.

The command execution happens in `command_execution.py`.

---

### Close the client if connection fails

```python
except Exception:
    client.close()
    raise
```

If something goes wrong while connecting, the SSH client is closed and the error is raised again.

---

## `command_execution.py`

This file imports the connection function and runs the hard-coded command.

---

### Import the connection function

```python
from android_conn import connect_to_mobile
```

This imports `connect_to_mobile()` from `android_conn.py`.

So `command_execution.py` does not need to know how the SSH connection is created internally.

---

### Store connection details

```python
HOST = ""
USER = ""
PASSWORD = ""
PORT = 8022
```

These values are used to connect to the Android device.

Example:

```python
HOST = "192.168.1.10"
USER = "u0_a123"
PASSWORD = "your_password"
PORT = 8022
```

Do not commit your real password to GitHub.

---

### Store the hard-coded command

```python
COMMAND = "uptime; date; date +%Z; date +%z; whoami; pwd; uname -a"
```

This is the command string sent to the Android device.

Command meaning:

```text
uptime      -> shows how long the device/session has been running
date        -> shows current date and time
date +%Z    -> shows timezone name, for example IST
date +%z    -> shows timezone offset, for example +0530
whoami      -> shows the current SSH user
pwd         -> shows the current working directory
uname -a    -> shows kernel/system information
```

---

### Run the command

```python
_, stdout, stderr = client.exec_command(COMMAND)
```

`exec_command()` returns three values:

```text
stdin, stdout, stderr
```

In this program:

```python
_
```

is used for `stdin` because the command does not need input.

---

### Read output and errors

```python
output = stdout.read().decode().strip()
error = stderr.read().decode().strip()
```

This reads the command result.

```text
stdout -> normal command output
stderr -> error output
```

`.decode()` converts bytes into a string.

`.strip()` removes extra spaces and newlines from the beginning and end.

---

### Return error if there is one

```python
if error:
    return error
```

If the command produces an error, the program returns the error.

---

### Return normal output

```python
return output
```

If there is no error, the program returns the command output.

---

### Close the connection

```python
finally:
    if client:
        client.close()
```

The `finally` block makes sure the SSH connection closes even if an error occurs.

---

## Example output

The output may look like this:

```text
up 2 hours, 35 minutes
Fri Jun  5 18:45:21 IST 2026
IST
+0530
u0_a123
/data/data/com.termux/files/home
Linux localhost 5.10.123-android12-9-g123456789 #1 SMP PREEMPT ...
```

The exact output will be different depending on your Android device.

---

# Study notes

## One command string vs multiple commands

This project sends one command string:

```python
COMMAND = "uptime; date; date +%Z; date +%z; whoami; pwd; uname -a"
```

The semicolon separates shell commands.

So this:

```bash
uptime; date
```

means:

```text
Run uptime first.
Then run date.
```

From Python's point of view, it is still one string passed to `exec_command()`.

---

## Paramiko command execution methods

Paramiko does not have Netmiko-style `send_command()`.

In Paramiko, the common ways are:

---

### 1. `exec_command()`

```python
client.exec_command("uptime")
```

This is the simplest method.

Use this when you want to run a command and get the output.

This project currently uses `exec_command()`.

---

### 2. `invoke_shell()`

```python
shell = client.invoke_shell()
shell.send("uptime\n")
shell.send("date\n")
```

This opens an interactive shell.

It behaves more like a real terminal session.

Useful later if you want to send multiple commands interactively.

But the output can include prompts and echoed commands, so it is harder to parse.

---

### 3. `open_session()`

```python
transport = client.get_transport()
channel = transport.open_session()
channel.exec_command("uptime")
```

This is a lower-level way to run commands.

It gives more control, but for this project `exec_command()` is easier.

---

## Paramiko vs Netmiko

## Paramiko

Paramiko is a Python SSH library.

It is useful when you want to connect to normal SSH systems, such as:

- Linux servers
- Ubuntu machines
- Raspberry Pi devices
- Android Termux
- Remote shells

Paramiko gives you lower-level SSH control.

You connect, run commands, read output, and close the connection.

This project uses Paramiko because Termux behaves like a normal Linux-style SSH environment.

---

## Netmiko

Netmiko is built on top of Paramiko and is mainly designed for network devices.

It is useful for devices such as:

- Cisco routers
- Cisco switches
- Juniper devices
- Arista switches
- Fortinet firewalls
- Palo Alto firewalls

Netmiko understands network-device CLI behavior, such as:

- `show` commands
- config mode
- device prompts
- vendor-specific command behavior

---

## Why we used Paramiko, not Netmiko

We used Paramiko because the target is an Android device running Termux.

Termux is not a router, switch, or firewall.

It is closer to a small Linux terminal running on Android.

For this project, we only need to:

```text
SSH into Termux -> run command -> get output
```

That is exactly what Paramiko is good at.

Netmiko would be unnecessary here because we are not working with a network device CLI.

---

## About `send_command()`

`send_command()` is commonly used in Netmiko:

```python
connection.send_command("show version")
```

Paramiko does not use this style.

In Paramiko, use:

```python
client.exec_command("uptime")
```

or, for an interactive shell:

```python
shell = client.invoke_shell()
shell.send("uptime\n")
```

Simple rule:

```text
Paramiko exec_command()  -> normal SSH command execution
Paramiko invoke_shell()  -> interactive shell
Netmiko send_command()   -> network device command execution
```

---

## Simple rule

Use Paramiko for normal SSH automation.

Use Netmiko for network device automation.

For this project:

```text
Android Termux = Paramiko
Cisco router/switch = Netmiko
```

---

## Security note

Do not commit real passwords into code.

This example uses a simple password for learning.

In real projects, prefer:

- SSH keys
- environment variables
- a secrets manager
- prompting for the password at runtime