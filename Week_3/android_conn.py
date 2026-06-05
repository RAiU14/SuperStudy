import paramiko


def connect_to_mobile(host, user, port=8022, password=None):
    client = paramiko.SSHClient()

    # Load known SSH host keys from your system
    client.load_system_host_keys()

    # Automatically trust unknown devices
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=host,
            port=port,
            username=user,
            password=password,
            timeout=10,
        )

        return client

    except Exception:
        client.close()
        raise