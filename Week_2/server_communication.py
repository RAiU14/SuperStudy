import paramiko
import getpass

def run_command(ssh, command):
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode().strip()
    error = stderr.read().decode().strip()
 
    if error:
        return error
    return output

host = input("Enter server IP address: ").strip()
username = input("Enter SSH username: ").strip()
password = getpass.getpass("Enter SSH password: ")
 
commands = {
    "Hostname": "hostname",
    "CPU Model": "lscpu | grep 'Model name' | cut -d ':' -f2 | sed 's/^ *//'",
    "RAM": "free -h",
    "Uptime": "uptime -p",
    "IP Address(es)": "hostname -I",
    "Disk Usage": "df -h /",
    "Download Speed": "curl -L -o /dev/null -s -w '%{speed_download}' 'https://speed.cloudflare.com/__down?bytes=25000000' | awk '{printf \"%.2f Mbps\", ($1 * 8) / 1000000}'",
    "Upload Speed": "head -c 25000000 /dev/zero | curl -s -o /dev/null -X POST --data-binary @- -w '%{speed_upload}' 'https://speed.cloudflare.com/__up' | awk '{printf \"%.2f Mbps\", ($1 * 8) / 1000000}'"
}

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=host,
        username=username,
        password=password,
        timeout=10
    )
    print("\n===== Server Information =====\n")
 
    for title, command in commands.items():
        print(f"{title}:")
        print(run_command(ssh, command))
        print()
 
    ssh.close()
 
except paramiko.AuthenticationException:
    print("Login failed: wrong username or password.")
 
except paramiko.SSHException as e:
    print(f"SSH error: {e}")
 
except Exception as e:
    print(f"Error: {e}")