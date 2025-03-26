from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
import transformers
import torch
import requests
import redis
import json
from typing import List
import jwt

# Load Hugging Face Model
model_name = "EleutherAI/gpt-j-6B"  # Can be replaced with LLaMA
tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
model = transformers.AutoModelForCausalLM.from_pretrained(model_name)

# Initialize API & Redis (for webhooks)
app = FastAPI()
redis_client = redis.Redis(host="localhost", port=6379, db=0)

# Dummy Risk Database
risk_db = {"Global Horiacne Consulting LLC": 85, "Quantum Holdings Ltd": 90}  # Higher means riskier

# JWT Secret for RBAC
SECRET_KEY = "your_secret_key"


# Role-Based Access Control
def get_current_user(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["role"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


# Request Model
class TransactionRequest(BaseModel):
    raw_text: str


# Response Model
class TransactionResponse(BaseModel):
    transaction_id: str
    sender: dict
    receiver: dict
    amount: float
    risk_score: int
    flagged: bool


# Function to Extract Transaction Data
def extract_transaction(raw_text):
    inputs = tokenizer(raw_text, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=512)
    structured_text = tokenizer.decode(outputs[0])

    # Dummy Parsed Data
    transaction_data = {
        "transaction_id": "TAN-2023-5A98",
        "sender": {
            "name": "Global Horiacne Consulting LLC",
            "account": "TEAN CH56 0482 5012 3456 7800 9",
            "address": "Rue du Marché 17, Geneva, Switzerland",
        },
        "receiver": {
            "name": "Bright Future Nonprofit Inc.",
            "account": "987654321",
            "address": "P.O. Box 1234, George Town, Cayman Islands",
        },
        "amount": 449850.00,
        "currency": "USD",
        "risk_score": 0,
        "flagged": False
    }

    return transaction_data


# Risk Evaluation
def evaluate_risk(transaction):
    sender_name = transaction["sender"]["name"]
    risk_score = risk_db.get(sender_name, 20)  # Default Low Risk

    # High Amount Flag
    if transaction["amount"] > 100000:
        risk_score += 10

    # Threshold to flag
    flagged = risk_score > 70
    transaction["risk_score"] = risk_score
    transaction["flagged"] = flagged

    return transaction


# Webhook Trigger
def trigger_webhook(transaction):
    webhook_url = "https://your-webhook-endpoint.com"
    if transaction["flagged"]:
        requests.post(webhook_url, json=transaction)


# API Endpoint to Process Transactions
@app.post("/process_transaction", response_model=TransactionResponse)
async def process_transaction(request: TransactionRequest, role: str = Depends(get_current_user)):
    if role not in ["admin", "auditor"]:
        raise HTTPException(status_code=403, detail="Access Denied")

    transaction = extract_transaction(request.raw_text)
    transaction = evaluate_risk(transaction)
    trigger_webhook(transaction)

    return transaction


# Run the API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
