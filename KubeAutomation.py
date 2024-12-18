import subprocess

def run_command(command):
    """
    Runs a shell command and captures its output.
    """
    try:
        print(f"Running command: {command}")
        result = subprocess.run(command, shell=True, text=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing: {command}")
        print(e.stderr)
        raise

def main():
    docker_image = "my-app"
    docker_hub_repo = "ankitu03/my-app"
    tag = "v1.0"
    deployment_file = "deployment.yaml"
    service_file = "service.yaml"

    try:
        # Step 1: Build Docker Image
        print("Building Docker image...")
        run_command(f"docker build -t {docker_image} .")

        # Step 2: Tag Docker Image
        print("Tagging Docker image...")
        run_command(f"docker tag {docker_image} {docker_hub_repo}:{tag}")

        # Step 3: Push Docker Image to Docker Hub
        print("Pushing Docker image to Docker Hub...")
        run_command(f"docker push {docker_hub_repo}:{tag}")

        # Step 4: Apply Kubernetes Deployment
        print("Applying deployment.yaml...")
        run_command(f"kubectl apply -f {deployment_file}")

        # Step 5: Apply Kubernetes Service
        print("Applying service.yaml...")
        run_command(f"kubectl apply -f {service_file}")

        print("Automation completed successfully!")

    except Exception as e:
        print(f"Automation failed: {e}")

if __name__ == "__main__":
    main()
