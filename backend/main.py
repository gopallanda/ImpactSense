from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib
import numpy as np

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load pre-trained gradient boosting model (only once at startup)
model = joblib.load("gradient_boosting_model.pkl")

# Lazy load dataset only when needed
df = None


# Input schema
class InputData(BaseModel):
    magnitude: float
    depth: float
    cdi: float
    mmi: float
    sig: float


@app.post("/predict")
async def predict(data: InputData):
    # Use numpy array for faster prediction
    input_vec = np.array([[data.magnitude, data.depth, data.cdi, data.mmi, data.sig]])
    prediction = model.predict(input_vec)[0]
    return {"alert": int(prediction)}


@app.get("/dataset")
async def get_dataset_preview():
    global df
    # Lazy load dataset only when this endpoint is called
    if df is None:
        df = pd.read_csv("earthquake_alert_balanced_dataset.csv")
    return {"rows": df.to_dict(orient="records")}
