# SSH into Android Termux using Paramiko

This mini project uses Python and Paramiko to SSH into an Android device running Termux and execute one command: `uptime`.

The goal is simple:

```text
Python script -> Android Termux SSH server -> run uptime -> return output
```

---

## What this program does

The program:

1. Creates an SSH client using Paramiko.
2. Connects to the Android device running Termux.
3. Runs the `uptime` command on the Android device.
4. Reads the command output.
5. Closes the SSH connection.

---

## Requirements

### On Android Termux

Install and start the SSH server:

```bash
pkg update
pkg install openssh
sshd
```

Termux SSH usually runs on port `8022`.

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

## Important lines of the program explained
> android_conn.py
### Create the SSH client

```python
client = paramiko.SSHClient()
```

This creates a Paramiko SSH client object. The client is used to connect to the Android device and run commands.

---

### Load known SSH host keys

```python
client.load_system_host_keys()
```

This loads trusted SSH host keys from your system, usually from:

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

For production use, this is less secure because it trusts new SSH servers automatically.

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

This connects to the Termux SSH server using:

- `hostname`: Android device IP address
- `port`: Termux SSH port, usually `8022`
- `username`: Termux username, for example `u0_XXX`
- `password`: Termux SSH password
- `timeout`: maximum time to wait for connection

---

### Run the uptime command

```python
_, stdout, stderr = client.exec_command("uptime")
```

`exec_command()` returns three values:

```text
stdin, stdout, stderr
```

In this program, `stdin` is ignored using `_` because the `uptime` command does not need input.

---

### Read command output

```python
output = stdout.read().decode().strip()
error = stderr.read().decode().strip()
```

This reads the output and error streams.

- `stdout` contains normal command output.
- `stderr` contains error messages.
- `.decode()` converts bytes into a string.
- `.strip()` removes extra spaces and newlines.

---

### Close the connection

```python
finally:
    client.close()
```

The `finally` block makes sure the SSH connection closes even if an error occurs.

---

## Example output

```text
up 2 hours, 35 minutes
```

The exact output may be different depending on your Android device.

---
# Study Related stuffs below:
# Paramiko vs Netmiko

## Paramiko

Paramiko is a Python SSH library.

It is useful when you want to connect to normal SSH systems, such as:

- Linux servers
- Ubuntu machines
- Raspberry Pi devices
- Android Termux
- Remote shells

Paramiko gives you lower-level SSH control. You connect, run commands, read output, and close the connection.

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

Termux is not a router, switch, or firewall. It is closer to a small Linux terminal running on Android.

For this project, we only need to:

```text
SSH into Termux -> run uptime -> get output
```

That is exactly what Paramiko is good at.

Netmiko would be unnecessary here because we are not working with a network device CLI.

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

This example uses a simple password for learning. In real projects, prefer:

- SSH keys
- environment variables
- a secrets manager
- prompting for the password at runtime