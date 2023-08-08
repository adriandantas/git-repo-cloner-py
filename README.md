# git-repo-cloner

`git-repo-cloner` is a Dockerized script designed to clone Git repositories. It handles validations for empty URLs, valid Git URLs, and GitHub private repositories using authentication tokens.

## Usage

### Environment Variables

The following environment variables must be set when running the Docker container:

| Variable      | Description                                                                                             | Example                                              |
|---------------|---------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| `TEMPLATE_URL`| The URL of the Git repository you want to clone. Must be a valid Git URL.                               | `"https://github.com/username/repo.git"`             |
| `GIT_TOKEN`   | The GitHub personal access token for authenticating when cloning private GitHub repositories.           | `"your-personal-access-token"`                       |
| `TEMPLATE_DIR`| The directory path where the Git repository will be cloned.                                             | `"/path/to/dir"`                                     |



### Building the Docker Image

1. Build the Docker image (replace `<version>` with the desired version number):

```shell
docker build -t git-repo-cloner-py .
```

## Running the Docker Container

Run the Docker container:

```shell
docker run -e TEMPLATE_URL=https://github.com/username/repo.git -e GIT_TOKEN=token123 -e TEMPLATE_DIR=/path/to/dir git-repo-cloner:<version>
```

Replace the environment variables with the appropriate values for your use case.

### Publishing the Docker Image

Tag the Docker image with your Docker Hub username and version number (replace <version> with the desired version number):

```shell
docker tag git-repo-cloner-py adriandantas/git-repo-cloner-py:<version>
```

Push the Docker image to Docker Hub (replace <version> with the desired version number):

```shell
docker push adriandantas/git-repo-cloner-py:<version>
```

## Running Tests

The `git-repo-cloner` project comes with a comprehensive test suite to ensure its functionality. To run the tests, follow these steps:

```shell
python -m unittest tests/test_git_repo_cloner.py
```
