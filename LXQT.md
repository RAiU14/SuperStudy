# POCO F1 Proot-Distro Debian Desktop Setup

A practical guide for running a Debian desktop environment inside Termux using `proot-distro`, LXQt, XRDP, GitLab, DNS tooling, and lightweight development tools.

---

# Overview

This setup turns a POCO F1 into a portable Linux workstation.

Features:

* Debian via `proot-distro`
* LXQt Desktop
* XRDP Remote Desktop
* OpenSSH Access
* Git & GitLab Workflow
* Geany Code Editor
* Firefox Browser
* Optional DNS Services

---

# Architecture

```text
Android (POCO F1)
│
├── Termux
│   ├── OpenSSH (8022)
│   └── proot-distro
│
└── Debian
    ├── LXQt
    ├── Openbox
    ├── XRDP (3389)
    ├── Geany
    ├── Firefox
    └── Development Tools
```

---

# Current Status

| Component      | Status     |
| -------------- | ---------- |
| Termux         | Installed  |
| Debian         | Installed  |
| LXQt           | Installed  |
| XRDP           | Configured |
| OpenSSH        | Configured |
| Geany          | Installed  |
| Firefox        | Installed  |
| Git            | Configured |
| GitLab         | Configured |
| Technitium DNS | Optional   |

---

# Quick Start

Start SSH:

```bash
sshd
```

Start Desktop:

```bash
./start-desktop.sh
```

Connect from PC:

```text
PHONE_IP:3389
```

Login using Debian credentials.

---

# 1. Install Termux Packages

```bash
pkg update && pkg upgrade -y

pkg install -y \
proot-distro \
git \
wget \
curl \
openssh \
nano \
vim
```

Grant storage access:

```bash
termux-setup-storage
```

Set password:

```bash
passwd
```

Start SSH:

```bash
sshd
```

---

# 2. Install Debian

```bash
proot-distro install debian
```

Login:

```bash
proot-distro login debian
```

Update:

```bash
apt update
apt full-upgrade -y
```

---

# 3. Create User

```bash
apt install -y sudo

adduser poco

usermod -aG sudo poco
```

Switch user:

```bash
su - poco
```

---

# 4. Install Desktop Environment

```bash
sudo apt update

sudo apt install -y \
lxqt \
openbox \
xorg \
dbus-x11 \
xrdp \
firefox-esr \
geany \
pcmanfm-qt \
featherpad \
git \
curl \
wget \
zip \
unzip \
nano \
vim \
ca-certificates \
openssh-client
```

Useful extras:

```bash
sudo apt install -y \
htop \
tmux \
neofetch \
glances
```

---

# Geany

Geany is the preferred lightweight editor for this setup.

Launch:

```bash
geany
```

Advantages:

* Fast startup
* Low RAM usage
* Good Python support
* Good Bash support
* Markdown friendly

---

# 5. Configure XRDP

Create LXQt session:

```bash
echo "startlxqt" > ~/.xsession
chmod +x ~/.xsession
```

Edit XRDP:

```bash
sudo nano /etc/xrdp/xrdp.ini
```

Recommended settings:

```ini
[Globals]
max_bpp=16
tcp_nodelay=true
use_fastpath=both
bitmap_compression=true
bulk_compression=true
```

Restart:

```bash
sudo service xrdp restart
```

Verify:

```bash
ss -ltnp | grep 3389
```

---

# 6. Startup Script

Create:

```bash
nano ~/start-desktop.sh
```

Contents:

```bash
#!/bin/bash

echo "Starting Debian Desktop..."

proot-distro login debian -- bash -c "
service dbus start || true
service xrdp restart
"

echo ""
echo "Desktop Started"
echo "Connect using:"
echo "PHONE_IP:3389"
```

Make executable:

```bash
chmod +x ~/start-desktop.sh
```

Run:

```bash
./start-desktop.sh
```

---

# 7. Daily Workflow

Start SSH:

```bash
sshd
```

Start desktop:

```bash
./start-desktop.sh
```

Connect from PC:

```text
PHONE_IP:3389
```

Open:

* Geany
* Firefox
* Terminal

Work normally.

---

# 8. Git & GitLab Setup

Install Git:

```bash
sudo apt install -y git
```

Configure:

```bash
git config --global user.name "Your Name"

git config --global user.email "you@example.com"
```

Clone:

```bash
git clone https://gitlab.com/group/repository.git
```

Recommended cache:

```bash
git config --global credential.helper 'cache --timeout=28800'
```

Workflow:

```bash
git status

git add .

git commit -m "Description"

git push
```

Protected branches:

```bash
git checkout -b feature/my-change

git push -u origin feature/my-change
```

---

# 9. DNS Notes

Technitium DNS is optional. [I did not test this myself]

Common ports:

| Service | Port |
| ------- | ---- |
| DNS     | 53   |
| Web UI  | 5380 |

Check resolver:

```bash
cat /etc/resolv.conf
```

Test:

```bash
getent hosts gitlab.com
```

Temporary resolver:

```bash
echo "nameserver 1.1.1.1" | sudo tee /etc/resolv.conf
```

---

# 10. SSH & SCP

SSH Port:

```text
8022
```

Copy PC → Phone:

```bash
scp -P 8022 file.txt USER@PHONE_IP:/sdcard/Download/
```

Copy Phone → PC:

```bash
scp -P 8022 USER@PHONE_IP:/sdcard/Download/file.txt .
```

---

# 11. Performance Tips

### XRDP

```ini
max_bpp=16
bitmap_compression=true
bulk_compression=true
tcp_nodelay=true
use_fastpath=both
```

### Android

* Disable battery optimization for Termux
* Use USB tethering if possible
* Reduce animations
* Keep device charging during long sessions

### Debian Cleanup

```bash
sudo apt autoremove -y

sudo apt clean
```

---

# 12. Useful Paths

| Purpose       | Path                                                                            |
| ------------- | ------------------------------------------------------------------------------- |
| Termux Home   | `/data/data/com.termux/files/home`                                              |
| Downloads     | `/sdcard/Download`                                                              |
| Debian RootFS | `/data/data/com.termux/files/usr/var/lib/proot-distro/containers/debian/rootfs` |
| XRDP Config   | `/etc/xrdp/xrdp.ini`                                                            |
| DNS Config    | `/etc/resolv.conf`                                                              |

---

# 13. Common Commands

Enter Debian:

```bash
proot-distro login debian
```

Enter as user:

```bash
proot-distro login debian --user poco
```

Check ports:

```bash
ss -ltnp
```

System info:

```bash
uname -m
free -h
df -h
```

Backup home:

```bash
tar -czf home-backup.tar.gz /home/poco
```

---

# 14. Troubleshooting

### XRDP not connecting

```bash
sudo service xrdp restart

ss -ltnp | grep 3389
```

### Blank LXQt screen

```bash
echo "startlxqt" > ~/.xsession

chmod +x ~/.xsession

sudo service xrdp restart
```

### DNS not working

```bash
cat /etc/resolv.conf

getent hosts google.com
```

### systemctl unavailable

Use:

```bash
sudo service xrdp restart

sudo service dbus start
```

---

# 15. Security

* Use strong passwords
* Do not expose 3389 publicly
* Do not expose 8022 publicly
* Prefer LAN access
* Use GitLab PATs instead of passwords
* Never commit credentials

---

# 16. Repositories

| Repository   | URL                                                        |
| ------------ | ---------------------------------------------------------- |
| Landing Page | https://gitlab.com/parenthses-group/landing-page           |
| Project Hub  | https://gitlab.com/parenthses-group/PARENTHSES-project-hub |

---

# 17. Maintenance

Update Termux:

```bash
pkg update && pkg upgrade -y
```

Update Debian:

```bash
sudo apt update

sudo apt full-upgrade -y

sudo apt autoremove -y

sudo apt clean
```

Check health:

```bash
free -h

df -h

uptime
```
