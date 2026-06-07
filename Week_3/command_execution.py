import logging
import time
from pathlib import Path
from android_conn import connect_to_mobile


LOG_FILE = Path(__file__).with_name("ssh_android.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)


PORT = 8022

COMMAND = "uptime; date; date +%Z; date +%z; whoami"

EXECUTION_METHOD = "exec_command"
# EXECUTION_METHOD = "invoke_shell"
# EXECUTION_METHOD = "open_session"


def run_command(host, user, password, port=PORT):
    client = None

    logger.info("Program started")
    logger.info("Execution method selected: %s", EXECUTION_METHOD)
    logger.info("Command to execute: %s", COMMAND)

    try:
        client = connect_to_mobile(
            host=host,
            user=user,
            port=port,
            password=password,
        )

        logger.info("Connected to Android device")

        if EXECUTION_METHOD == "exec_command":
            logger.info("Running command using exec_command")

            _, stdout, stderr = client.exec_command(COMMAND)

            output = stdout.read().decode("utf-8", errors="replace").strip()
            error = stderr.read().decode("utf-8", errors="replace").strip()

            if error:
                logger.error("Command returned error: %s", error)
                return error

            logger.info("Command executed successfully")
            logger.info("Output length: %s characters", len(output))

            return output

        elif EXECUTION_METHOD == "invoke_shell":
            logger.info("Running command using invoke_shell")

            shell = client.invoke_shell()

            shell.send(COMMAND + "\n")
            logger.info("Command sent to shell")

            shell.send("exit\n")
            logger.info("Exit command sent to shell")

            time.sleep(1)

            output = ""

            while shell.recv_ready():
                output += shell.recv(4096).decode("utf-8", errors="replace")

            output = output.strip()

            logger.info("Shell command executed successfully")
            logger.info("Output length: %s characters", len(output))

            return output

        elif EXECUTION_METHOD == "open_session":
            logger.info("Running command using open_session")

            transport = client.get_transport()
            channel = transport.open_session()

            channel.exec_command(COMMAND)
            logger.info("Command sent through channel")

            output = channel.makefile("r").read().decode("utf-8", errors="replace").strip()
            error = channel.makefile_stderr("r").read().decode("utf-8", errors="replace").strip()

            channel.close()
            logger.info("Channel closed")

            if error:
                logger.error("Command returned error: %s", error)
                return error

            logger.info("Command executed successfully")
            logger.info("Output length: %s characters", len(output))

            return output

        else:
            logger.warning("Invalid execution method selected: %s", EXECUTION_METHOD)
            return "Invalid execution method selected."

    except Exception:
        logger.exception("Unexpected error while running command")
        raise

    finally:
        if client:
            client.close()
            logger.info("SSH connection closed")


if __name__ == "__main__":
    host = input("Hostname: ")
    user = input("Username: ")
    password = input("Password: ")

    result = run_command(
        host=host,
        user=user,
        password=password,
    )

    print(EXECUTION_METHOD)
    print(result)