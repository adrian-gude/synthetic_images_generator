import argparse
import subprocess
import os
import os
import subprocess
import argparse


def transfer_files(files, server, username, remote_path):
    for file in files:
        if os.path.isfile(file):
            try:
                subprocess.run(
                    ["scp", file, f"{username}@{server}:{remote_path}"], check=True
                )
                print(f"File {file} transferred successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error transferring file {file}.")
        elif os.path.isdir(file):
            try:
                subprocess.run(
                    ["scp", "-r", file, f"{username}@{server}:{remote_path}"],
                    check=True,
                )
                print(f"Directory {file} transferred successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error transferring directory {file}.")
        else:
            print(f"{file} does not exist or is not valid anymore.")


def main():
    parser = argparse.ArgumentParser(
        description="Run scp command to transfer files or directories to CESGA"
    )
    parser.add_argument(
        "--files", nargs="+", help="Path to the source files or directories"
    )
    parser.add_argument(
        "--server", help="Address of the server", default="ft3.cesga.es"
    )
    parser.add_argument(
        "--username", help="Username for the server", default="ulciaalg"
    )
    parser.add_argument(
        "--destination", help="Path to the destination directory", default="$LUSTRE"
    )
    args = parser.parse_args()

    transfer_files(args.files, args.server, args.username, args.destination)


if __name__ == "__main__":
    main()
