# 🛒 EBAY DealFinder AI

EBAY DealFinder AI is a Django-based web application that helps users find the **cheapest** and **best-reviewed** products on eBay across different marketplaces.

---

## 🚀 Features

- 🌎 Supports multiple eBay marketplaces (e.g., US, Canada, UK)
- 🔍 Search for any product in real-time
- 💰 View cheapest results
- ⭐ View best-reviewed results
- 🔗 Direct links to buy the products on eBay

---

## 🖥️ Screenshots
![image](https://github.com/user-attachments/assets/50f290e9-e201-4a47-92a8-e799c202a63b)
![image](https://github.com/user-attachments/assets/d9e3b195-00fc-48d8-81bd-0c4545c69b96)

---

## 📦 Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS (no framework)
- **API:** eBay Browse API
- **Environment:** dotenv for secure credentials

---

## ⚙️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/dealfinder-ai.git
cd dealfinder-ai

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

Create a .env file in the project root:
CLIENT_ID=your_ebay_client_id
CLIENT_SECRET=your_ebay_client_secret

python manage.py runserver
