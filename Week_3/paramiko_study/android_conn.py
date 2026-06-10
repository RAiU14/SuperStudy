import logging
import paramiko


logger = logging.getLogger(__name__)


def connect_to_mobile(host, user, port=8022, password=None):
    logger.info("Creating SSH client")

    client = paramiko.SSHClient()

    logger.info("Loading system host keys")
    client.load_system_host_keys()

    logger.info("Setting missing host key policy")
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        logger.info(
            "Trying to connect to host=%s user=%s port=%s",
            host,
            user,
            port,
        )

        client.connect(
            hostname=host,
            port=port,
            username=user,
            password=password,
            timeout=10,
        )

        logger.info("SSH connection successful")
        return client

    except Exception:
        logger.exception("SSH connection failed")

        try:
            client.close()
            logger.info("SSH client closed after connection failure")
        except Exception:
            logger.exception("Failed to close SSH client after connection failure")

        raise