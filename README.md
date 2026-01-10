# Composio Google Services Integration 🚀

This project demonstrates how to integrate **Google services** (Gmail, Google Calendar, Google Drive, etc.) using **Composio** to enable secure, scalable, and production-ready automation for AI agents and backend applications.

The goal is to abstract away OAuth complexity and allow seamless access to Google APIs using Composio-managed tools.

---

## ✨ Features

* 🔐 Secure OAuth-based authentication via **Composio**
* 📧 Gmail automation (send, read, search emails)
* 📅 Google Calendar event creation and management
* 📂 Google Drive file access and uploads
* 🤖 AI-agent friendly tool-based integration
* ⚡ Plug-and-play setup for backend services

---

## 🛠️ Tech Stack

* **Python**
* **Composio SDK**
* **Google APIs**
* **FastAPI / Backend Framework**
* **OAuth 2.0**
* **REST APIs**

---

## 📁 Project Structure

```bash
.
├── app/
│   ├── services/
│   │   └── google_service.py
│   ├── routes/
│   │   └── google_routes.py
│   └── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/kapilnila/composio-google-service.git
cd composio-google-service
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables

Create a `.env` file and add:

```env
COMPOSIO_API_KEY=your_composio_api_key
```

> ⚠️ **Do not expose API keys publicly**

---

## 🔑 Google OAuth via Composio

Composio handles:

* OAuth consent
* Token refresh
* Secure credential storage

Once connected, Google tools are available instantly to your app or AI agent.

---

## 🧠 Example Usage

### Gmail – Send Email

```python
from composio import ComposioToolSet

toolset = ComposioToolSet(api_key="YOUR_API_KEY")

toolset.execute(
    action="GMAIL_SEND_EMAIL",
    params={
        "to": "example@gmail.com",
        "subject": "Hello from Composio",
        "body": "This email was sent using Composio!"
    }
)
```

---

## 📅 Supported Google Actions

* `GMAIL_SEND_EMAIL`
* `GMAIL_SEARCH_EMAILS`
* `CALENDAR_CREATE_EVENT`
* `CALENDAR_LIST_EVENTS`
* `DRIVE_UPLOAD_FILE`
* `DRIVE_LIST_FILES`

---

## 🤖 Use Cases

* AI email assistants
* Automated meeting schedulers
* CRM and sales automation
* AI-powered productivity agents
* Backend automation workflows

---

## 🚀 Future Enhancements

* Role-based access control
* Multi-user Google account linking
* Agent-based orchestration
* UI dashboard for OAuth status

---

## 🧩 Why Composio?

* No manual OAuth handling
* Secure credential isolation
* Designed for AI-first workflows
* Production-grade reliability

---

## 📄 License

MIT License

---

## 🙌 Acknowledgements

* [Composio](https://composio.dev)
* Google Developer Platform

---
