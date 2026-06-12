import argparse
import getpass
import logging
from pathlib import Path
import paramiko


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


def connect_to_mobile(host, user, port=8022, password=None, key_filename=None):
    logger.info("Creating Paramiko SSH client")
    client = paramiko.SSHClient()
    logger.info("Loading system host keys")
    client.load_system_host_keys()
    logger.info("Setting missing host key policy")
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        logger.info(
            "Trying to connect to host=%s user=%s port=%s key_used=%s password_used=%s",
            host,
            user,
            port,
            bool(key_filename),
            bool(password),
        )
        client.connect(
            hostname=host,
            port=port,
            username=user,
            password=password,
            key_filename=key_filename,
            timeout=10,
        )
        logger.info("SSH connection successful")
        return client

    except Exception:
        logger.exception("SSH connection failed")

        try:
            client.close()
            logger.info("SSH client closed after failed connection")
        except Exception:
            logger.exception("Failed to close SSH client after connection failure")

        raise


def send_command(client, command):
    logger.info("Executing command: %s", command)
    try:
        _, stdout, stderr = client.exec_command(command)

        output = stdout.read().decode("utf-8", errors="replace").strip()
        error = stderr.read().decode("utf-8", errors="replace").strip()
        exit_code = stdout.channel.recv_exit_status()

        if exit_code == 0:
            logger.info("Command executed successfully")
            logger.info("Output length: %s characters", len(output))
        else:
            logger.warning("Command failed with exit code: %s", exit_code)
            logger.warning("Error output length: %s characters", len(error))

        return exit_code, output, error

    except Exception:
        logger.exception("Command execution failed")
        raise


def main():
    logger.info("Program started")
    parser = argparse.ArgumentParser(
        description="SSH into Android Termux and run commands."
    )

    parser.add_argument("--host", required=True, help="Android device IP address")
    parser.add_argument("--user", required=True, help="Termux username")
    parser.add_argument("--port", type=int, default=8022, help="Termux SSH port")
    parser.add_argument("--password", help="Termux SSH password")
    parser.add_argument("--key", help="Path to SSH private key")

    args = parser.parse_args()
    password = args.password

    if not args.key and not password:
        logger.info("No password or SSH key provided. Asking for password securely.")
        password = getpass.getpass("Termux SSH password: ")

    mobile = None

    try:
        mobile = connect_to_mobile(
            host=args.host,
            user=args.user,
            port=args.port,
            password=password,
            key_filename=args.key,
        )
        print("[+] Connected to Android Termux")
        exit_code, output, error = send_command(mobile, "uptime")

        if exit_code == 0:
            logger.info("Uptime command completed successfully")

            print("\nAndroid uptime:")
            print(output)
        else:
            logger.warning("Uptime command failed")

            print("\n[!] Command failed:")
            print(error)

    except Exception:
        logger.exception("Program failed")
        raise

    finally:
        if mobile:
            mobile.close()
            logger.info("SSH connection closed")
            print("\n[+] Connection closed")
        logger.info("Program finished")


if __name__ == "__main__":
    main()