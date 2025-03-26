# AI - Driven Entity Intelligence Risk Analysis

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction



## 🎥 Demo
🔗 
  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
This project was created during the Technology Hackathon 2025 to showcase how AI-driven workflows can improve risk analytics based on entity driven and risk score as well without interfere the manual processes


## ⚙️ What It Does
Features:
✅ Transaction Data Extraction – Using GPT-J/LLaMA

✅ Real-Time Risk Evaluation – Based on entity reputation & anomalies

✅ API Endpoint – /process_transaction (Requires JWT authentication)

✅ RBAC Security – Fixed roles (Admin, Auditor)

✅ Logging & Audit Trails – Stores risk scores for compliance

✅ Webhook Support – Alerts for high-risk transactions



## 🛠️ How We Built It



## 🚧 Challenges We Faced



## 🏃 How to Run

curl -X 'POST' 'http://127.0.0.1:8000/process_transaction' \
-H 'Content-Type: application/json' \
-H "Authorization: Bearer YOUR_JWT_TOKEN" \
-d '{"raw_text": "Your transaction raw data here"}'


## 🏗️ Tech Stack
Hugging Face Transformers (GPT-J, LLaMA) – For NLP-based transaction extraction.

FastAPI – To expose API endpoints.

PostgreSQL – For logging and audit trails.

Redis/Webhooks – For real-time alerts.

JWT Authentication – For RBAC security.


## 👥 Team

A.Ravikishore 
M.Rajshekhar 
K.Aruna
P.Lakshmi Sravani 
N.Shalini

