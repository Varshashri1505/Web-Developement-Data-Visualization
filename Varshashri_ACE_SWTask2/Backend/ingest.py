#importing libraries
import pandas as pd
from sqlalchemy import create_engine

# connecting the data to postgreSQL string
DATABASE_URL = "postgresql://postgres:Varshashri%401@localhost:5432/Task1_IOT_project"
engine = create_engine(DATABASE_URL)

# Loading the datasets
df = pd.read_csv("../iot_dataset.csv")         
df_mapping = pd.read_csv("../iot_dataset_mapping.csv")  

# Split and uploading each vertical into PostgreSQL
for v in df['type'].unique():
    temp = df[df['type'] == v].copy()
    temp.to_sql(f"{v.lower()}_data", con=engine, if_exists="replace", index=False)
    print(f" Uploaded {v} → {v.lower()}_data ({temp.shape[0]} rows)")
