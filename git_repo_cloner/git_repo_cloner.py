import os
import json
import git
from urllib.parse import urlparse
import sys
import re


def validate_template_url(template_url):
    if not template_url:
        raise ValueError("TEMPLATE_URL cannot be empty or null")
    try:
        git.cmd.Git().ls_remote(template_url)
    except git.exc.GitCommandError:
        raise ValueError(f"Invalid URL for git repository: {template_url}")


def extract_hostname(template_url):
    return urlparse(template_url).hostname


def extract_repo_name(url):
    # Regular expression pattern to match the repository name between the last '/' and '.git'
    pattern = r'https://github\.com/([^/]+/[^/]+\.git)'

    # Search for the pattern in the URL
    match = re.search(pattern, url)

    # If a match is found, return the first capturing group; otherwise, return None
    return match.group(1) if match else None


def validate_github_token(hostname, git_token):
    if hostname == 'github.com' and not git_token:
        raise ValueError("GIT_TOKEN cannot be empty when using GitHub URL")


def clone_repository(template_url, git_token, template_dir):
    hostname = extract_hostname(template_url)
    if hostname == "github.com":
        repo = extract_repo_name(template_url)
        clone_url = f"https://x-access-token:{git_token}@{hostname}/{repo}"
        git.Repo.clone_from(clone_url, template_dir, branch='main')
    else:
        git.Repo.clone_from(template_url, template_dir, branch='main')


def main():
    TEMPLATE_URL = os.getenv('TEMPLATE_URL')
    GIT_TOKEN = os.getenv('GIT_TOKEN')
    TEMPLATE_DIR = os.getenv('TEMPLATE_DIR')

    try:
        validate_template_url(TEMPLATE_URL)
        hostname = extract_hostname(TEMPLATE_URL)
        validate_github_token(hostname, GIT_TOKEN)
        clone_repository(TEMPLATE_URL, GIT_TOKEN, TEMPLATE_DIR)
        print(json.dumps({"success": "Repository successfully cloned", "message": "Repository cloned successfully"}))
        sys.exit(0)
    except Exception as e:
        print(json.dumps({"error": "Operation Failed", "message": str(e)}), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
