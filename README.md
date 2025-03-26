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

This project implements an GENAI-powered solution for automating the process of checking the risk score analytics based on entity attributes involved in the unstructured and strucured transactional data.

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
1. Setup FastAPI and Dependencies

Step 1: Install FastAPI and required libraries.

pip install fastapi uvicorn transformers torch psycopg2 requests redis

Step 2: Install PostgreSQL on your local machine if it isn't installed.

Ubuntu: sudo apt-get install postgresql postgresql-contrib

Mac: brew install postgresql


Step 3: Install Redis for webhook and caching (optional for scalability)

2. Create a Transaction Extraction API with FastAPI

Step 1: Create a file called main.py for the FastAPI server.

3. PostgreSQL Database Integration

Step 1: Create a PostgreSQL database for storing transactions.

CREATE DATABASE transaction_db;

Step 2: Create a table for storing transaction data.

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    transaction_id VARCHAR(255),
    sender JSONB,
    receiver JSONB,
    amount FLOAT,
    risk_score INT
);

Step 3: Configure the PostgreSQL connection.

4. Risk Threshold Tuning

To enable risk threshold tuning, you can create a configuration table or environment variables to store the thresholds.

5. Dockerize the Application

Step 1: Create a Dockerfile to containerize your FastAPI application.

# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app

# Expose port for FastAPI
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

Step 2: Create a requirements.txt file.

fastapi
uvicorn
transformers
torch
psycopg2
requests
redis

Step 3: Build and run the Docker container.

docker build -t transaction-api .
docker run -d -p 8000:8000 transaction-api

6. Run the Application

You can now run the FastAPI server with:

uvicorn main:app --reload

Then, use a tool like Postman or curl to test the API by sending a POST request to http://localhost:8000/process_transaction with the raw transaction data.


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

A.Ravikishore ,
M.Rajshekhar ,
K.Aruna ,
P.Lakshmi Sravani ,
N.Shalini.

