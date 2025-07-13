# 🎭 Dare Exchange

Welcome to **Dare Exchange** — a playful platform where users can post, accept, and complete dares. Built with Django, Dare Exchange brings the thrill of anonymous dares into the digital world.

---

## 🚀 Features

- 📝 **Post Dares** — Create and submit dares for others.
- 💪 **Accept Dares** — Take up challenges posted by others.
- 📜 **Track Completion** — View completed and pending dares.
- 🔐 **User Authentication** — Sign up, login, and manage your dare activity.
- 🧼 **Clean UI** — Minimal and intuitive interface for a fun experience.

---

## 🛠️ Tech Stack

- ⚙️ **Backend**: Django (Python)
- 💾 **Database**: SQLite (default), PostgreSQL for production
- 🌐 **Frontend**: HTML, CSS, Bootstrap (can be customized further)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/anandku06/dare-exchange.git
cd dare-exchange
````

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations and run the server:

```bash
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to start using Dare Exchange.

---

## 🧪 Development Notes

* Ensure your `.env` or settings variables are configured for production deployment.
* Don’t forget to run `python manage.py collectstatic` when deploying.
* Uses `gunicorn` and `whitenoise` for production serving.

---

## 🌍 Deployment

You can deploy this app on platforms like:

* 🚀 [Render](https://render.com)
* ☁️ Heroku
* 🛠️ VPS (Ubuntu + Gunicorn + Nginx)

## 🤝 Contributing

Contributions are welcome! Whether it's a bug fix, feature suggestion, or design enhancement, feel free to [open an issue](https://github.com/anandku06/dare-exchange/issues) or submit a PR.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

Built with ❤️ by [Anand Kumar](https://github.com/anandku06) 
