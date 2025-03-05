from fastapi import FastAPI, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import uvicorn

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
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Base URL for generating payment links
PAYMENT_URL_TEMPLATE = "http://192.238.136.20/cashierDeskIndex.html?merchantName=&orderAmount=&transNumber={order_number}"

@app.post("/generate_payment_link/")
async def generate_payment_link(order_number: str = Form(...), cdk: str = Form(...)):
    if cdk not in VALID_CDKS:
        raise HTTPException(status_code=403, detail="Invalid CDK")

    payment_link = PAYMENT_URL_TEMPLATE.format(order_number=order_number)
    return {"payment_link": payment_link}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)