from fastapi import FastAPI
from blockchain import get_balance
from ml_model import train_model, predict
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

class Transaction(BaseModel):
    value: float
    gas: int
    tx_count: int


@app.get("/")
def home():
    return {"message": "BlockTraceX API running"}

@app.get("/balance/{address}")
def balance(address: str):
    return {"balance": str(get_balance(address))}

@app.get("/train")
def train():
    return {"status": train_model()}

@app.post("/detect")
def detect(tx: Transaction):
    result = predict([tx.value, tx.gas, tx.tx_count])
    return {"result": result}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)