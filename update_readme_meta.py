from pathlib import Path
from datetime import datetime
import argparse
import getpass
import subprocess
import re


def get_git_username():
    try:
        result = subprocess.run(
            ["git", "config", "user.name"],
            capture_output=True,
            text=True,
            check=True
        )
        name = result.stdout.strip()
        return name or None
    except Exception:
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Update README.md Last Updated and By fields at the end of the file."
    )

    parser.add_argument(
        "--file",
        default="README.md",
        help="README file path. Default: README.md"
    )

    parser.add_argument(
        "--by",
        default=None,
        help="Name to write after By:"
    )

    args = parser.parse_args()

    readme_path = Path(args.file)

    if not readme_path.exists():
        raise FileNotFoundError(f"File not found: {readme_path}")

    content = readme_path.read_text(encoding="utf-8")

    today = datetime.now().strftime("%d/%m/%Y")
    author = args.by or get_git_username() or getpass.getuser()

    content = re.sub(r"(?m)^Last Updated:\s*.*\n?", "", content)
    content = re.sub(r"(?m)^By:\s*.*\n?", "", content)

    content = content.rstrip() + f"\n\nLast Updated: {today}\\\nBy: {author}\n"

    readme_path.write_text(content, encoding="utf-8")

    print("README updated successfully.")
    print(f"Last Updated: {today}")
    print(f"By: {author}")


if __name__ == "__main__":
    main()