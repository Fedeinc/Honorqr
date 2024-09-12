import os
import shutil
import subprocess

# Define the paths
project_root = os.path.dirname(os.path.abspath(__file__))
staticfiles_dir = os.path.join(project_root, 'staticfiles')
publish_dir = os.path.join(project_root, 'public')  # Change if your HTML files are in a different directory
netlify_toml_path = os.path.join(project_root, 'netlify.toml')

# Step 1: Collect static files using Django's collectstatic command
def collect_static():
    try:
        subprocess.run(['python', 'manage.py', 'collectstatic', '--no-input'], check=True)
        print("Static files collected successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during collectstatic: {e}")
        exit(1)

# Step 2: Ensure the publish directory exists and contains necessary files
def setup_publish_directory():
    if not os.path.exists(publish_dir):
        os.makedirs(publish_dir)
    
    # Move static files to the publish directory
    if os.path.exists(staticfiles_dir):
        for item in os.listdir(staticfiles_dir):
            s = os.path.join(staticfiles_dir, item)
            d = os.path.join(publish_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
    
    print(f"Static files moved to {publish_dir}.")

# Step 3: Ensure that the netlify.toml file is correctly configured
def configure_netlify_toml():
    netlify_toml_content = f"""
[build]
  command = "python manage.py collectstatic --no-input"
  publish = "{publish_dir}"  # Adjust this based on where your static files are located

[dev]
  command = "python manage.py runserver"
  port = 8000

[functions]
  external_node_modules = [
    "module-one",
    "module-two"
  ]

[functions.environment]
  PYTHONUNBUFFERED = "true"
"""
    with open(netlify_toml_path, 'w') as netlify_toml_file:
        netlify_toml_file.write(netlify_toml_content)
    
    print("netlify.toml configured successfully.")

# Run the setup steps
if __name__ == "__main__":
    collect_static()
    setup_publish_directory()
    configure_netlify_toml()
    print("Setup completed. You're ready to deploy on Netlify!")
