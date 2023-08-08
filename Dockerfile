# Use an official Python runtime as the base image
FROM python:3.10.12-slim-bullseye

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Copy the git_repo_cloner directory to the container
COPY git_repo_cloner/git_repo_cloner.py .

# Install git
RUN apt-get update && apt-get install -y git

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Make the script executable
RUN chmod +x git_repo_cloner.py

# Set the script as the entrypoint
ENTRYPOINT ["python", "./git_repo_cloner.py"]
