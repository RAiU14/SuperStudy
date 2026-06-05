import time
from android_conn import connect_to_mobile


HOST = input("Hostname: ")
USER = input("Username: ")
PASSWORD = input("Password: ")
PORT = 8022


COMMAND = "uptime; date; date +%Z; date +%z; whoami"

EXECUTION_METHOD = "exec_command"
# EXECUTION_METHOD = "invoke_shell"
# EXECUTION_METHOD = "open_session"


def run_command():
    client = None

    try:
        client = connect_to_mobile(
            host=HOST,
            user=USER,
            port=PORT,
            password=PASSWORD,
        )

        if EXECUTION_METHOD == "exec_command":
            _, stdout, stderr = client.exec_command(COMMAND)

            output = stdout.read().decode().strip()
            error = stderr.read().decode().strip()

            if error:
                return error

            return output

        elif EXECUTION_METHOD == "invoke_shell":
            shell = client.invoke_shell()

            shell.send(COMMAND + "\n")
            shell.send("exit\n")

            time.sleep(1)
            # Necessarry in a shell

            output = ""

            while shell.recv_ready():
                output += shell.recv(4096).decode()

            return output.strip()

        elif EXECUTION_METHOD == "open_session":
            transport = client.get_transport()
            channel = transport.open_session()

            channel.exec_command(COMMAND)

            output = channel.makefile("r").read().decode().strip()
            error = channel.makefile_stderr("r").read().decode().strip()

            channel.close()

            if error:
                return error

            return output

        else:
            return "Invalid execution method selected."

    finally:
        if client:
            client.close()


if __name__ == "__main__":
    result = run_command()
    print(EXECUTION_METHOD)
    print(result)