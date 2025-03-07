from fastapi import FastAPI, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import uvicorn
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Explicitly load the correct .env file
load_dotenv("validCDKs.env")

# Debugging print
print("Raw ENV:", os.getenv("VALID_CDKS"))  

# Parse the environment variable properly
VALID_CDKS = set(cdk.strip() for cdk in os.getenv("VALID_CDKS", "").split(","))

print("Loaded VALID_CDKS:", VALID_CDKS)  # Debugging output



# CORS settings to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://payment-link-generator-frontend.onrender.com"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Base URL for generating payment links
PAYMENT_URL_TEMPLATE = "http://192.238.136.20/cashierDeskIndex.html?merchantName=&orderAmount=&transNumber={order_number}"

@app.get("/")
def home():
    return {"message": "Backend is working!"}

@app.post("/generate_payment_link/")
async def generate_payment_link(order_number: str = Form(...), cdk: str = Form(...)):
    logger.info(f"Received request: Order={order_number}, CDK={cdk}")
    if cdk not in VALID_CDKS:
        logger.warning(f"Invalid CDK: {cdk}")
        raise HTTPException(status_code=403, detail="Invalid CDK")

    payment_link = PAYMENT_URL_TEMPLATE.format(order_number=order_number)
    logger.info(f"Generated link: {payment_link}")
    return {"payment_link": payment_link}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))