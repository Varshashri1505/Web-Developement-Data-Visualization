#importing Apis required
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
import pandas as pd

# connection to PostgreSQL 

DATABASE_URL = "postgresql://postgres:Varshashri%401@localhost:5432/Task1_IOT_project"
engine = create_engine(DATABASE_URL)

# Initialization of FastAPI app

app = FastAPI(title="IoT Sensor Data API - Task 2")

# Enabling the frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
# checking the backend connection

@app.get("/")
def home():
    return {"message": "FastAPI connected successfully to Task1_IOT_project database!"}

#fetching the data by verticals (AQ, WF, SL)
@app.get("/api/verticals/{vertical}")
def get_vertical_data(vertical: str):
    table_name = f"{vertical.lower()}_data"
    try:
        query = text(f"SELECT * FROM {table_name}")
        df = pd.read_sql(query, engine)

        # Handling the missing values
        df.fillna("NA", inplace=True)

        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error fetching data for {vertical}: {e}")
