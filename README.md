🔐 Password Security Analyzer (Flask Web App)

A web-based Password Strength Analyzer and Dictionary Attack Simulator built using Python and Flask, designed to demonstrate password security concepts, entropy calculation, and ethical attack simulations.

🚀 Features

✅ Password strength analysis (Weak / Medium / Strong)

🔢 Entropy calculation based on character diversity

🔐 Secure SHA-256 hashing (passwords are never stored)

📖 Dictionary attack simulation using a curated wordlist

🌐 Web-based interface using Flask

🎨 Modern, responsive UI

☁️ Deployed on Render using Gunicorn

🧠 How It Works

User enters a password on the web page

Password is analyzed for:

Length

Uppercase, lowercase, digits, special characters

Entropy

Password is hashed using SHA-256

If the password is weak, a dictionary attack simulation is performed

Results are displayed instantly on the web page

⚠️ Passwords are never stored or logged — all processing happens in memory.

🛠️ Tech Stack

Backend: Python, Flask

Frontend: HTML, CSS (Jinja2 templating)

Security: hashlib (SHA-256)

Deployment: Render + Gunicorn

Version Control: Git & GitHub

📁 Project Structure
password-security-tool/
│
├── app.py               # Flask application entry point
├── analyzer.py          # Password strength & entropy logic
├── cracker.py           # Dictionary attack simulation
├── utils.py             # Hashing & utility functions
├── wordlist.txt         # Curated common password list
├── requirements.txt     # Python dependencies
│
├── templates/
│   └── index.html       # Frontend HTML (Jinja template)
│
└── static/
    └── style.css        # Styling

▶️ Running Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/password-security-tool.git
cd password-security-tool

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the application
python app.py


Open your browser and go to:

http://127.0.0.1:5000

🌐 Live Demo

👉 Deployed Application:
(Add your Render URL here)

🔐 Security & Ethics

This project is educational only

Demonstrates how weak passwords can be compromised

Uses a curated wordlist, not full leaked datasets

Designed to promote security awareness, not exploitation
