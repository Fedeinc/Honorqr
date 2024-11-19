import os

# Define the base path for the HTML files
base_path = os.getcwd()

# List of files and their paths to ensure their existence and necessary updates
file_structure = {
    'navigation.html': 'Navigation Optimization',
    'signup.html': 'Sign-Up and Registration',
    'tribute_wall.html': 'Tribute Wall',
    'profile.html': 'Profile and User Dashboard',
    'user_dashboard.html': 'Profile and User Dashboard',
    'qr_locator.html': 'Memorial Creation and QR Code Generation',
    'qr_share.html': 'Memorial Creation and QR Code Generation',
    'remembrance.html': 'Remembrance Calendar',
    'security.html': 'Security and Privacy Settings',
    'settings.html': 'Settings Expansion',
    'live_streaming.html': 'Live Streaming Feature',
    'notifications.html': 'Notification System',
    'pricing.html': 'Payment and Billing',
    'billing.html': 'Payment and Billing',
    'help.html': 'Help and Support Section',
    'chatbot.html': 'Help and Support Section',
}

# Function to create or update HTML file content
def ensure_file_and_content(filepath, description):
    file_full_path = os.path.join(base_path, filepath)
    
    # Check if the file exists
    if not os.path.exists(file_full_path):
        with open(file_full_path, 'w') as f:
            content = f"<!-- {description} -->\n"
            f.write(content)
        print(f"Created file: {filepath} with description.")
    else:
        print(f"File already exists: {filepath}")

# Function to update navigation HTML
def update_navigation(filepath):
    file_full_path = os.path.join(base_path, filepath)
    nav_content = """
    <nav class="top-0 left-0 z-50 fixed bg-white shadow-md w-full">
        <div class="mx-auto px-4 sm:px-6 lg:px-8 max-w-screen-xl">
            <div class="flex justify-between items-center h-16">
                <a href="index.html" class="flex items-center space-x-3">
                    <img src="images/logo.png" class="h-10" alt="HonorQR Logo">
                    <span class="font-semibold text-gray-900 text-xl">HonorQR</span>
                </a>
                <div class="hidden md:flex md:ml-4">
                    <ul class="flex space-x-8 text-gray-900">
                        <li><a href="index.html" class="px-3 py-2 rounded hover:text-blue-600">Home</a></li>
                        <li><a href="about.html" class="px-3 py-2 rounded hover:text-blue-600">About</a></li>
                        <li><a href="features.html" class="px-3 py-2 rounded hover:text-blue-600">Features</a></li>
                        <li><a href="pricing.html" class="px-3 py-2 rounded hover:text-blue-600">Pricing</a></li>
                        <li><a href="faq.html" class="px-3 py-2 rounded hover:text-blue-600">FAQ</a></li>
                        <li><a href="contact.html" class="px-3 py-2 rounded hover:text-blue-600">Contact</a></li>
                        <li><a href="signup.html" class="px-3 py-2 rounded hover:text-blue-600">Signup</a></li>
                        <li><a href="login.html" class="px-3 py-2 rounded hover:text-blue-600">Login</a></li>
                    </ul>
                </div>
                <div class="md:hidden">
                    <button id="hamburger-button" aria-expanded="false" aria-controls="mobile-menu" class="hover:bg-gray-200 p-2 rounded text-gray-900">
                        <span class="sr-only">Open main menu</span>
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
        <div id="mobile-menu" class="hidden md:hidden">
            <ul class="flex flex-col space-y-2 bg-gray-100 mt-2">
                <li><a href="index.html" class="block px-4 py-2 rounded hover:bg-gray-200">Home</a></li>
                <li><a href="about.html" class="block px-4 py-2 rounded hover:bg-gray-200">About</a></li>
                <li><a href="features.html" class="block px-4 py-2 rounded hover:bg-gray-200">Features</a></li>
                <li><a href="pricing.html" class="block px-4 py-2 rounded hover:bg-gray-200">Pricing</a></li>
                <li><a href="faq.html" class="block px-4 py-2 rounded hover:bg-gray-200">FAQ</a></li>
                <li><a href="contact.html" class="block px-4 py-2 rounded hover:bg-gray-200">Contact</a></li>
                <li><a href="signup.html" class="block px-4 py-2 rounded hover:bg-gray-200">Signup</a></li>
                <li><a href="login.html" class="block px-4 py-2 rounded hover:bg-gray-200">Login</a></li>
            </ul>
        </div>
    </nav>
    <script>
        const hamburgerButton = document.getElementById('hamburger-button');
        const mobileMenu = document.getElementById('mobile-menu');
        hamburgerButton.addEventListener('click', () => {
            const expanded = hamburgerButton.getAttribute('aria-expanded') === 'true';
            hamburgerButton.setAttribute('aria-expanded', !expanded);
            mobileMenu.classList.toggle('hidden');
        });
    </script>
    """
    with open(file_full_path, 'w') as f:
        f.write(nav_content)
    print(f"Updated navigation content in {filepath}")

# Create necessary files and ensure content exists
for file, description in file_structure.items():
    ensure_file_and_content(file, description)

# Update navigation in the navigation.html
update_navigation('navigation.html')

print("All required files ensured and updated.")
