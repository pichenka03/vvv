
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

catalog = pd.read_csv("full_hearing_aids_catalog.csv")

@app.post("/extract")
async def extract():
    return {"right": {"500": 40, "1000": 45, "2000": 50},
            "left": {"500": 35, "1000": 40, "2000": 45}}

@app.post("/match")
async def match():
    return catalog.head(5).to_dict(orient="records")
