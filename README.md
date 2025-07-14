📧 Fake Email Generator
A web-based fake email generator built with Flask. Instantly generate bulk fake email addresses using various methods and export them as a .txt file. Useful for testing, dummy data population, and development.

🔧 Features
✅ Choose from 5 email generation methods:

Random String

1.Faker
2.Names
3.Mimesis
4.RandomUser

✅ Custom domain support (e.g. @gmail.com)

✅ Export as .txt file

✅ Simple and elegant user interface

✅ Built using Python, Flask, and HTML/CSS

🚀 Demo

🛠 Installation
bash
Copy code
git clone https://github.com/yourusername/fake-email-generator.git
cd fake-email-generator
pip install -r requirements.txt
📦 Requirements
Make sure the following Python packages are installed:

txt
Copy code
Flask
Faker
names
mimesis
randomuser
You can install them with:

bash
Copy code
pip install Flask Faker names mimesis randomuser
▶️ Usage
Run the Flask app:

bash
Copy code
python app.py
Then open your browser and go to:

cpp
Copy code
http://127.0.0.1:5000/
🧪 How It Works
Choose the method of generation.

Enter your desired domain (e.g. @outlook.com).

Choose the number of emails (minimum: 10).

Generate and download your fake email list.

📂 File Structure
cpp
Copy code
.
├── app.py
├── templates/
│   └── index.html
├── static/
├── README.md
└── requirements.txt
👨‍💻 Created By
Vatsal Varshney
