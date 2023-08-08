import unittest
from unittest.mock import patch
from git_repo_cloner.git_repo_cloner import validate_template_url, extract_hostname, validate_github_token, clone_repository
import git

class TestGitRepoCloner(unittest.TestCase):

    def test_validate_template_url_empty(self):
        with self.assertRaises(ValueError) as context:
            validate_template_url(None)
        self.assertEqual(str(context.exception), "TEMPLATE_URL cannot be empty or null")

    def test_validate_template_url_invalid(self):
        with self.assertRaises(ValueError) as context:
            validate_template_url("https://invalid.git")
        self.assertEqual(str(context.exception), "Invalid URL for git repository: https://invalid.git")

    def test_extract_hostname(self):
        hostname = extract_hostname("https://github.com/repo.git")
        self.assertEqual(hostname, "github.com")

    def test_validate_github_token_empty(self):
        with self.assertRaises(ValueError) as context:
            validate_github_token("github.com", None)
        self.assertEqual(str(context.exception), "GIT_TOKEN cannot be empty when using GitHub URL")

    def test_validate_github_token_not_github(self):
        # Should not raise an exception
        validate_github_token("gitlab.com", None)

    @patch('git.Repo.clone_from')
    def test_clone_repository_github(self, mock_clone_from):
        template_url = "https://github.com/someuser/repo.git"
        git_token = "token123"
        template_dir = "/path/to/dir"
        clone_repository(template_url, git_token, template_dir)
        clone_url = "https://x-access-token:token123@github.com/someuser/repo.git"
        mock_clone_from.assert_called_once_with(clone_url, template_dir, branch='main')

    @patch('git.Repo.clone_from')
    def test_clone_repository_not_github(self, mock_clone_from):
        template_url = "https://not-github.com/repo.git"
        git_token = "token123"
        template_dir = "/path/to/dir"
        clone_repository(template_url, git_token, template_dir)
        mock_clone_from.assert_called_once_with(template_url, template_dir, branch='main')

if __name__ == '__main__':
    unittest.main()
