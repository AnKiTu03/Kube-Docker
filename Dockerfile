# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /kube-dock

# Install dependencies and Docker CLI
RUN apt-get update && \
    apt-get install -y curl gnupg apt-transport-https ca-certificates && \
    curl -fsSL https://download.docker.com/linux/static/stable/x86_64/docker-24.0.6.tgz | tar xzvf - --strip 1 -C /usr/local/bin && \
    chmod +x /usr/local/bin/docker && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the Python script into the container
COPY KubeAutomation.py /kube-dock/

# Command to run the Python script
CMD ["python3", "KubeAutomation.py"]
