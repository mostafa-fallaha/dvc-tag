import subprocess
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="version of data by git tag")
parser.add_argument("git_tag", type=str, help="git tag")
args = parser.parse_args()

# Define variables
data_file = "data_version/categories.csv"
dvc_file = "data_version/categories.csv.dvc"
gitignore_file = "data_version/.gitignore"

git_tag = args.git_tag
commit_message = "went back to " + git_tag

# Run DVC and Git commands
subprocess.run(["git", "checkout", git_tag], check=True)
subprocess.run(["dvc", "checkout"], check=True)
subprocess.run(["git", "checkout", "main"], check=True)
subprocess.run(["dvc", "add", data_file], check=True)
subprocess.run(["git", "add", dvc_file, gitignore_file,], check=True)
subprocess.run(["git", "commit", "-m", commit_message], check=True)
subprocess.run(["dvc", "push"], check=True)
subprocess.run(["git", "push"], check=True)
