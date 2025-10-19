# Language Notebook API
Django + DRF backend for vocab, expressions, and spaced repetition.
📝 Language Notebook

A personal language-learning notebook built with Django and Django REST Framework.
Users can store vocabulary, example sentences, and cultural expressions such as idioms, slangs, and proverbs — all organized into topic-based decks.

🚀 Features

User Authentication — Login and logout using Django’s session or JWT authentication

Deck Management — Create topic-based decks to group related words

Vocabulary Tracking — Add words with translations, examples, notes, and tags

Expressions — Save slangs, idioms, and sayings with region, register, and usage notes

Search & Filter — Quickly find words or expressions

Admin Dashboard — Manage users and data via Django Admin

Responsive Frontend — Clean UI built with Django templates + CSS + JavaScript (fetches data from your API)

🧠 Tech Stack
Layer	Technology
Backend	Django 5, Django REST Framework
Authentication	JWT (SimpleJWT) + SessionAuth
Database	SQLite (default)
Frontend	Django Templates + Vanilla JS
Docs	drf-spectacular (Swagger UI)
Styling	Custom CSS (static files)

🗂 Project Structure
Language_Note_App/
├── accounts/           # user auth (JWT + session)
├── vocab/              # decks, words, tags
├── expressions/        # idioms, slangs, sayings
├── language_notebook/  # project settings & URLs
├── templates/          # base.html, home.html, login.html, etc.
├── static/             # css, js, images
├── manage.py
└── requirements.txt


⚙️ Setup Instructions
1️⃣ Clone the repo
git clone https://github.com/<your-username>/Language_Note_App.git
cd Language_Note_App

2️⃣ Create a virtual environment & install dependencies
python -m venv venv
source venv/bin/activate       # on Mac/Linux
venv\Scripts\activate          # on Windows

pip install -r requirements.txt

3️⃣ Apply migrations
python manage.py makemigrations
python manage.py migrate

4️⃣ Create a superuser
python manage.py createsuperuser

5️⃣ Run the server
python manage.py runserver


Now visit:

Home: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

API Docs: http://127.0.0.1:8000/api/docs/

💡 Future Improvements

Add spaced-repetition practice feature

Add review reminders & progress tracking

Improve frontend design and user experience

Add support for importing/exporting decks

🧑‍💻 Author

Meskerem Habtom
Built as part of the ALX Software Engineering Capstone Project
