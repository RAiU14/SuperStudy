import logging
from pathlib import Path
from getpass import getpass

from netmiko.exceptions import ReadTimeout
from android_conn import connect_to_mobile


BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "ssh_android.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)


PORT = 8022
DEVICE_TYPE = "linux"

COMMAND = "uptime; date; date +%Z; date +%z; whoami"

# Netmiko methods
EXECUTION_METHOD = "send_command_timing"
# EXECUTION_METHOD = "send_command"


def run_command(host, user, password, port=PORT, device_type=DEVICE_TYPE):
    connection = None

    logger.info("Program started")
    logger.info("Execution method selected: %s", EXECUTION_METHOD)
    logger.info("Command to execute: %s", COMMAND)

    try:
        connection = connect_to_mobile(
            host=host,
            user=user,
            port=port,
            password=password,
            device_type=device_type,
        )

        logger.info("Connected to Android device using Netmiko")

        if EXECUTION_METHOD == "send_command_timing":
            logger.info("Running command using send_command_timing")

            output = connection.send_command_timing(
                COMMAND,
                read_timeout=30,
                last_read=2,
                strip_prompt=True,
                strip_command=True,
            )

        elif EXECUTION_METHOD == "send_command":
            logger.info("Running command using send_command")

            output = connection.send_command(
                COMMAND,
                read_timeout=30,
                strip_prompt=True,
                strip_command=True,
            )

        else:
            logger.warning("Invalid execution method selected: %s", EXECUTION_METHOD)
            return "Invalid execution method selected."

        output = output.strip()

        logger.info("Command executed successfully")
        logger.info("Output length: %s characters", len(output))

        return output or "No output returned."

    except ReadTimeout:
        logger.exception("Command timed out while waiting for output")
        raise

    except Exception:
        logger.exception("Unexpected error while running command")
        raise

    finally:
        if connection:
            connection.disconnect()
            logger.info("Netmiko SSH connection disconnected")


if __name__ == "__main__":
    host = input("Hostname: ")
    user = input("Username: ")
    password = getpass("Password: ")

    result = run_command(
        host=host,
        user=user,
        password=password,
    )

    print(EXECUTION_METHOD)
    print(result)
    print(f"Log saved to: {LOG_FILE}")