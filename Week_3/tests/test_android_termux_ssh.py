import sys
import logging
from unittest.mock import Mock, patch
import pytest
import android_termux_ssh as app


def test_connect_to_mobile_success():
    mock_client = Mock()

    with patch(
        "paramiko_study.android_termux_ssh.paramiko.SSHClient",
        return_value=mock_client,
    ) as mock_ssh_client:
        with patch(
            "paramiko_study.android_termux_ssh.paramiko.AutoAddPolicy",
            return_value="auto_policy",
        ) as mock_auto_policy:
            result = app.connect_to_mobile(
                host="192.168.1.10",
                user="u0_a123",
                port=8022,
                password="test_password",
                key_filename=None,
            )

    mock_ssh_client.assert_called_once()
    mock_auto_policy.assert_called_once()

    mock_client.load_system_host_keys.assert_called_once()
    mock_client.set_missing_host_key_policy.assert_called_once_with("auto_policy")

    mock_client.connect.assert_called_once_with(
        hostname="192.168.1.10",
        port=8022,
        username="u0_a123",
        password="test_password",
        key_filename=None,
        timeout=10,
    )

    assert result == mock_client
    mock_client.close.assert_not_called()


def test_connect_to_mobile_failure_closes_client():
    mock_client = Mock()
    mock_client.connect.side_effect = Exception("Connection failed")

    with patch(
        "paramiko_study.android_termux_ssh.paramiko.SSHClient",
        return_value=mock_client,
    ):
        with patch(
            "paramiko_study.android_termux_ssh.paramiko.AutoAddPolicy",
            return_value="auto_policy",
        ):
            with pytest.raises(Exception, match="Connection failed"):
                app.connect_to_mobile(
                    host="192.168.1.10",
                    user="u0_a123",
                    port=8022,
                    password="wrong_password",
                )

    mock_client.close.assert_called_once()


def test_send_command_success():
    mock_client = Mock()

    mock_stdout = Mock()
    mock_stderr = Mock()
    mock_channel = Mock()

    mock_stdout.read.return_value = b"up 2 hours\n"
    mock_stderr.read.return_value = b""
    mock_channel.recv_exit_status.return_value = 0

    mock_stdout.channel = mock_channel

    mock_client.exec_command.return_value = (
        Mock(),
        mock_stdout,
        mock_stderr,
    )

    exit_code, output, error = app.send_command(mock_client, "uptime")

    mock_client.exec_command.assert_called_once_with("uptime")

    assert exit_code == 0
    assert output == "up 2 hours"
    assert error == ""


def test_send_command_failure_exit_code():
    mock_client = Mock()

    mock_stdout = Mock()
    mock_stderr = Mock()
    mock_channel = Mock()

    mock_stdout.read.return_value = b""
    mock_stderr.read.return_value = b"command not found\n"
    mock_channel.recv_exit_status.return_value = 127

    mock_stdout.channel = mock_channel

    mock_client.exec_command.return_value = (
        Mock(),
        mock_stdout,
        mock_stderr,
    )

    exit_code, output, error = app.send_command(mock_client, "wrong_command")

    assert exit_code == 127
    assert output == ""
    assert error == "command not found"


def test_send_command_logs_success(caplog):
    mock_client = Mock()

    mock_stdout = Mock()
    mock_stderr = Mock()
    mock_channel = Mock()

    mock_stdout.read.return_value = b"up 2 hours\n"
    mock_stderr.read.return_value = b""
    mock_channel.recv_exit_status.return_value = 0

    mock_stdout.channel = mock_channel

    mock_client.exec_command.return_value = (
        Mock(),
        mock_stdout,
        mock_stderr,
    )

    with caplog.at_level(logging.INFO):
        app.send_command(mock_client, "uptime")

    assert "Executing command: uptime" in caplog.text
    assert "Command executed successfully" in caplog.text


def test_main_success_with_password_argument(monkeypatch, capsys):
    mock_mobile = Mock()

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "android_termux_ssh.py",
            "--host",
            "192.168.1.10",
            "--user",
            "u0_a123",
            "--password",
            "test_password",
        ],
    )

    with patch(
        "paramiko_study.android_termux_ssh.connect_to_mobile",
        return_value=mock_mobile,
    ) as mock_connect:
        with patch(
            "paramiko_study.android_termux_ssh.send_command",
            return_value=(0, "up 2 hours", ""),
        ) as mock_send:
            app.main()

    mock_connect.assert_called_once_with(
        host="192.168.1.10",
        user="u0_a123",
        port=8022,
        password="test_password",
        key_filename=None,
    )

    mock_send.assert_called_once_with(mock_mobile, "uptime")
    mock_mobile.close.assert_called_once()

    captured = capsys.readouterr()

    assert "[+] Connected to Android Termux" in captured.out
    assert "Android uptime:" in captured.out
    assert "up 2 hours" in captured.out
    assert "[+] Connection closed" in captured.out


def test_main_asks_for_password_when_no_password_or_key(monkeypatch):
    mock_mobile = Mock()

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "android_termux_ssh.py",
            "--host",
            "192.168.1.10",
            "--user",
            "u0_a123",
        ],
    )

    with patch(
        "paramiko_study.android_termux_ssh.getpass.getpass",
        return_value="typed_password",
    ) as mock_getpass:
        with patch(
            "paramiko_study.android_termux_ssh.connect_to_mobile",
            return_value=mock_mobile,
        ) as mock_connect:
            with patch(
                "paramiko_study.android_termux_ssh.send_command",
                return_value=(0, "up 2 hours", ""),
            ):
                app.main()

    mock_getpass.assert_called_once_with("Termux SSH password: ")

    mock_connect.assert_called_once_with(
        host="192.168.1.10",
        user="u0_a123",
        port=8022,
        password="typed_password",
        key_filename=None,
    )

    mock_mobile.close.assert_called_once()


def test_main_does_not_ask_password_when_key_is_used(monkeypatch):
    mock_mobile = Mock()

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "android_termux_ssh.py",
            "--host",
            "192.168.1.10",
            "--user",
            "u0_a123",
            "--key",
            "C:/Users/test/.ssh/id_rsa",
        ],
    )

    with patch(
        "paramiko_study.android_termux_ssh.getpass.getpass",
    ) as mock_getpass:
        with patch(
            "paramiko_study.android_termux_ssh.connect_to_mobile",
            return_value=mock_mobile,
        ) as mock_connect:
            with patch(
                "paramiko_study.android_termux_ssh.send_command",
                return_value=(0, "up 2 hours", ""),
            ):
                app.main()

    mock_getpass.assert_not_called()

    mock_connect.assert_called_once_with(
        host="192.168.1.10",
        user="u0_a123",
        port=8022,
        password=None,
        key_filename="C:/Users/test/.ssh/id_rsa",
    )

    mock_mobile.close.assert_called_once()


def test_main_command_failure(monkeypatch, capsys):
    mock_mobile = Mock()

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "android_termux_ssh.py",
            "--host",
            "192.168.1.10",
            "--user",
            "u0_a123",
            "--password",
            "test_password",
        ],
    )

    with patch(
        "paramiko_study.android_termux_ssh.connect_to_mobile",
        return_value=mock_mobile,
    ):
        with patch(
            "paramiko_study.android_termux_ssh.send_command",
            return_value=(127, "", "command not found"),
        ):
            app.main()

    captured = capsys.readouterr()

    assert "[!] Command failed:" in captured.out
    assert "command not found" in captured.out

    mock_mobile.close.assert_called_once()