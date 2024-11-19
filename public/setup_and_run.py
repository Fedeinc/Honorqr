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
            file_lower = file.lower()
            if "auth" in file_lower:
                services["auth_service"] = True
            if "profile" in file_lower:
                services["user_profile_service"] = True
            if "media" in file_lower:
                services["media_service"] = True
            if "qr" in file_lower:
                services["qr_code_service"] = True
            if "tribute" in file_lower:
                services["tribute_wall_service"] = True
            if "notification" in file_lower:
                services["notification_service"] = True
            if "payment" in file_lower:
                services["payment_service"] = True
    
    return services

# Step 2: Install necessary dependencies with error handling
def install_dependencies():
    try:
        subprocess.run(["pip", "install", "django", "djangorestframework", "psycopg2-binary", "redis", "celery", "djangorestframework-jwt"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during dependency installation: {e}")
        return False
    return True

# Step 3: Setup backend services with error handling
def setup_services(services):
    for service_name, is_required in services.items():
        if is_required:
            try:
                subprocess.run(["django-admin", "startapp", service_name], check=True)
                print(f"{service_name} setup complete.")
            except subprocess.CalledProcessError as e:
                print(f"Error setting up {service_name}: {e}")
                
# Step 4: Connect frontend and backend
def connect_frontend_backend():
    # Assuming the frontend is served via a separate service, this might involve setting up CORS or API Gateway rules
    # Example CORS setup in Django:
    print("Configuring CORS for frontend...")
    with open('settings.py', 'a') as settings_file:
        settings_file.write("\n# CORS settings\n")
        settings_file.write("CORS_ORIGIN_ALLOW_ALL = True\n")
    print("CORS setup complete.")

# Run the setup
if __name__ == "__main__":
    directory = "./"  # Change this to your project directory
    services = scan_folder(directory)
    if install_dependencies():
        setup_services(services)
        connect_frontend_backend()
        print("Backend setup complete. Services installed and ready for development.")
    else:
        print("Failed to install dependencies. Exiting setup.")
