import os
import subprocess

# Step 1: Scan the folder to identify necessary services
def scan_folder(directory):
    services = {
        "api_gateway": False,
        "auth_service": False,
        "user_profile_service": False,
        "media_service": False,
        "qr_code_service": False,
        "tribute_wall_service": False,
        "notification_service": False,
        "payment_service": False
    }
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check for specific markers in filenames or contents to identify services
            if "auth" in file.lower():
                services["auth_service"] = True
            if "profile" in file.lower():
                services["user_profile_service"] = True
            if "media" in file.lower():
                services["media_service"] = True
            if "qr" in file.lower():
                services["qr_code_service"] = True
            if "tribute" in file.lower():
                services["tribute_wall_service"] = True
            if "notification" in file.lower():
                services["notification_service"] = True
            if "payment" in file.lower():
                services["payment_service"] = True
    
    return services

# Step 2: Install necessary dependencies
def install_dependencies():
    subprocess.run(["pip", "install", "django", "djangorestframework", "psycopg2-binary", "redis", "celery", "djangorestframework-jwt"])
    # subprocess.run(["pip", "install", "docker-compose"])  # Comment out this line
    # subprocess.run(["docker-compose", "up", "-d"])  # Comment out this line too

# Step 3: Setup backend services
def setup_services(services):
    if services["auth_service"]:
        subprocess.run(["django-admin", "startapp", "auth_service"])
    if services["user_profile_service"]:
        subprocess.run(["django-admin", "startapp", "user_profile_service"])
    if services["media_service"]:
        subprocess.run(["django-admin", "startapp", "media_service"])
    if services["qr_code_service"]:
        subprocess.run(["django-admin", "startapp", "qr_code_service"])
    if services["tribute_wall_service"]:
        subprocess.run(["django-admin", "startapp", "tribute_wall_service"])
    if services["notification_service"]:
        subprocess.run(["django-admin", "startapp", "notification_service"])
    if services["payment_service"]:
        subprocess.run(["django-admin", "startapp", "payment_service"])

# Step 4: Connect frontend and backend
def connect_frontend_backend():
    # Assuming the frontend is served via a separate service, this might involve setting up CORS or API Gateway rules
    pass

# Run the setup
if __name__ == "__main__":
    directory = "./"  # Change this to your project directory
    services = scan_folder(directory)
    install_dependencies()
    setup_services(services)
    connect_frontend_backend()

    print("Backend setup complete. Services installed and ready for development.")
