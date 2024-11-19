import os
import sys
import requests
import logging
from urllib.parse import urlencode
import subprocess
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

# Fetch environment variables
API_BASE = os.getenv('API_BASE_URL', 'https://honorqr.api/v1')
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
FACEBOOK_CLIENT_ID = os.getenv('FACEBOOK_CLIENT_ID')
API_EMAIL = os.getenv('API_EMAIL')
API_PASSWORD = os.getenv('API_PASSWORD')

OAUTH_GOOGLE_URL = "https://accounts.google.com/o/oauth2/auth"
OAUTH_FACEBOOK_URL = "https://www.facebook.com/v8.0/dialog/oauth"

def check_admin():
    """
    Check if the script is running with administrative privileges.
    """
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        # Windows
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if not is_admin:
        logging.error("This script must be run as Administrator.")
        sys.exit(1)

def update_hosts_file(hostname, ip_address='127.0.0.1'):
    """
    Add a hostname to the hosts file mapping it to a specified IP address.
    """
    hosts_path = os.path.join(os.environ['SystemRoot'], 'System32', 'drivers', 'etc', 'hosts')
    entry = f"{ip_address}\t{hostname}\n"
    try:
        with open(hosts_path, 'r') as f:
            content = f.read()
        if hostname in content:
            logging.info(f"Hostname '{hostname}' already exists in the hosts file.")
        else:
            with open(hosts_path, 'a') as f:
                f.write(entry)
            logging.info(f"Added '{hostname}' to the hosts file with IP '{ip_address}'.")
    except Exception as e:
        logging.error(f"Failed to update hosts file: {e}")
        sys.exit(1)

def flush_dns():
    """
    Flush the DNS cache.
    """
    try:
        logging.info("Flushing DNS cache...")
        subprocess.run(['ipconfig', '/flushdns'], check=True, capture_output=True)
        logging.info("DNS cache flushed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to flush DNS cache: {e}")
        sys.exit(1)

def test_api():
    """
    Test the accessibility of OAuth endpoints and perform API login.
    """
    logging.info("Starting API tests...")
    
    # Verify that essential environment variables are set
    missing_vars = []
    if not GOOGLE_CLIENT_ID:
        missing_vars.append('GOOGLE_CLIENT_ID')
    if not FACEBOOK_CLIENT_ID:
        missing_vars.append('FACEBOOK_CLIENT_ID')
    if not API_EMAIL:
        missing_vars.append('API_EMAIL')
    if not API_PASSWORD:
        missing_vars.append('API_PASSWORD')
    
    if missing_vars:
        logging.error(f"Missing environment variables: {', '.join(missing_vars)}")
        return
    
    # Test Google OAuth
    google_params = {
        'client_id': GOOGLE_CLIENT_ID,
        'redirect_uri': 'https://yourapp.com/oauth2callback',
        'response_type': 'code',
        'scope': 'email profile',
    }
    google_oauth_url = f"{OAUTH_GOOGLE_URL}?{urlencode(google_params)}"
    logging.debug(f"Google OAuth URL: {google_oauth_url}")
    try:
        google_response = requests.get(google_oauth_url)
        google_response.raise_for_status()
        logging.info("Google OAuth endpoint is accessible.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Google OAuth access failed: {e}")
    
    # Test Facebook OAuth
    facebook_params = {
        'client_id': FACEBOOK_CLIENT_ID,
        'redirect_uri': 'https://yourapp.com/oauth2callback',
        'state': 'your_random_state_string',
    }
    facebook_oauth_url = f"{OAUTH_FACEBOOK_URL}?{urlencode(facebook_params)}"
    logging.debug(f"Facebook OAuth URL: {facebook_oauth_url}")
    try:
        facebook_response = requests.get(facebook_oauth_url)
        facebook_response.raise_for_status()
        logging.info("Facebook OAuth endpoint is accessible.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Facebook OAuth access failed: {e}")
    
    # Test API login
    payload = {
        "email": API_EMAIL,
        "password": API_PASSWORD
    }
    login_url = f"{API_BASE}/login"
    logging.debug(f"API Login URL: {login_url}")
    logging.debug(f"Payload: {payload}")
    try:
        response = requests.post(login_url, json=payload)
        response.raise_for_status()
        logging.info("API login successful.")
    except requests.exceptions.HTTPError as err:
        logging.error(f"API login failed: {err} - Response: {err.response.text}")
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred during API login: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

def main():
    """
    Main function to orchestrate the setup and API tests.
    """
    # Check for admin privileges
    check_admin()
    
    # Update the hosts file to resolve 'honorqr.api' if necessary
    hostname = 'honorqr.api'
    ip_address = '127.0.0.1'  # Change if your API is hosted elsewhere
    update_hosts_file(hostname, ip_address)
    
    # Flush DNS cache
    flush_dns()
    
    # Run the API tests
    test_api()

if __name__ == "__main__":
    main()
