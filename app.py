from flask import Flask, render_template, request, send_file
from faker import Faker
from mimesis.locales import Locale
from mimesis import Person
from randomuser import RandomUser
import random
import string
import names
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    emails = []
    error = ""
    if request.method == "POST":
        method = request.form.get("method")
        domain = request.form.get("domain", "").strip()
        count = int(request.form.get("count", 0))

        if not domain.startswith("@") or "." not in domain:
            error = "Please enter a valid domain starting with '@' and containing a '.'"
        elif count < 10:
            error = "Please enter a count of at least 10."
        else:
            fake = Faker()
            if method == "Random String":
                for _ in range(count):
                    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
                    emails.append(username + domain)

            elif method == "Faker":
                for _ in range(count):
                    email = fake.email()
                    username = email.split("@")[0]
                    emails.append(username + domain)

            elif method == "Names":
                for _ in range(count):
                    first = names.get_first_name().lower()
                    last = names.get_last_name().lower()
                    emails.append(f"{first}.{last}{domain}")

            elif method == "Mimesis":
                person = Person(Locale.EN)
                for _ in range(count):
                    emails.append(person.email(domains=[domain]))

            elif method == "RandomUser":
                for _ in range(count):
                    user = RandomUser()
                    email = user.get_email().replace("@example.com", domain)
                    emails.append(email)

    return render_template("index.html", emails=emails, error=error)

@app.route("/download", methods=["POST"])
def download():
    email_data = request.form.get("emails")
    buffer = io.BytesIO()
    buffer.write(email_data.encode("utf-8"))
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="fake_emails.txt", mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True)
