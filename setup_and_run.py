import os
import subprocess
import sys

def run_command(command, cwd=None):
    """Run a command in the shell and handle errors."""
    try:
        subprocess.run(command, check=True, shell=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def setup_virtualenv():
    """Activate virtual environment and install dependencies."""
    print("Setting up virtual environment and installing dependencies...")
    run_command('pip install -r requirements.txt')

def start_docker_services():
    """Start Docker services."""
    print("Starting Docker services...")
    run_command('docker-compose up -d')

def run_migrations():
    """Run Django migrations."""
    print("Running Django migrations...")
    run_command('docker-compose exec web python manage.py migrate')

def collect_static_files():
    """Collect static files."""
    print("Collecting static files...")
    run_command('docker-compose exec web python manage.py collectstatic --noinput')

def run_tests():
    """Run Django tests."""
    print("Running Django tests...")
    run_command('docker-compose exec web python manage.py test')

def start_dev_server():
    """Start the Django development server."""
    print("Starting Django development server...")
    run_command('docker-compose exec web python manage.py runserver 0.0.0.0:8000')

def main():
    setup_virtualenv()
    start_docker_services()
    run_migrations()
    collect_static_files()
    run_tests()  # Optional: Comment this line if you don't want to run tests
    start_dev_server()

if __name__ == "__main__":
    main()
