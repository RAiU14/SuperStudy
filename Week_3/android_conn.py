import paramiko


def connect_to_mobile(host, user, port=8022, password=None):
    client = paramiko.SSHClient()

    client.load_system_host_keys()
    # Used to load the SSH host keys from system.
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # If the device IP is new or unknown, trust it automatically.

    try:
        client.connect(
            hostname=host,
            port=port,
            username=user,
            password=password,
            timeout=10,
        )

        _, stdout, stderr = client.exec_command("uptime")

        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()

        if error:
            return error

        return output

    finally:
        client.close()


if __name__ == "__main__":
    print(
        connect_to_mobile(
            host="",
            user="",
            password=""
        )
    )