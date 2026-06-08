import logging
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException


logger = logging.getLogger(__name__)


def connect_to_mobile(host, user, port=8022, password=None, device_type="linux"):
    logger.info("Creating Netmiko connection")

    device = {
        "device_type": device_type,
        "host": host,
        "username": user,
        "password": password,
        "port": port,

        # Timeouts
        "conn_timeout": 10,
        "auth_timeout": 10,
        "banner_timeout": 15,
        "timeout": 30,

        # Reliability settings
        "fast_cli": False,

        # Similar behavior to Paramiko AutoAddPolicy
        "ssh_strict": False,
        "system_host_keys": True,
    }

    try:
        logger.info(
            "Trying to connect to host=%s user=%s port=%s device_type=%s",
            host,
            user,
            port,
            device_type,
        )

        connection = ConnectHandler(**device)

        logger.info("Netmiko SSH connection successful")
        return connection

    except NetmikoAuthenticationException:
        logger.exception("Netmiko authentication failed")
        raise

    except NetmikoTimeoutException:
        logger.exception("Netmiko connection timed out")
        raise

    except Exception:
        logger.exception("Netmiko SSH connection failed")
        raise