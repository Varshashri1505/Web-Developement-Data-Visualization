Task 2 – IoT Data Visualization and Web Development

### STEP-1 Data Preparation & Visualization

###  Objective
Cleaned, standardized, and explored the IoT sensor dataset before integrating it with the backend API and React dashboard.

### What Was Done
- **Read the datasets:** `iot_dataset.csv` (main IoT readings) and `iot_dataset_mapping.csv` (sensor name mappings).
- **Inspected the data:** checked datatypes, missing values, and identified three verticals — `AQ`, `WF`, and `SL`.
- **Cleaned the dataset:**
  - Converted timestamp to `datetime`
  - Trimmed and upper-cased vertical names
  - Removed duplicates
  - Filled missing numeric values with each column’s median
- **Applied column mapping:** parsed mapping file to rename generic value columns to real sensor names (e.g., temperature, humidity, pm25 etc.).
- **Split by vertical:** created individual cleaned DataFrames for AQ, WF, and SL verticals.
- **Explored visually:** plotted two sample sensor variables per vertical to show time-based trends using Matplotlib/Seaborn.
- **Generated statistics:** summarized each vertical with `describe()` to understand sensor ranges and variability.

### Key Findings
- Minimal missing data, handled via median imputation.  
- Distinct temporal and behavioral patterns per vertical.  
- Mapping successfully aligned numeric columns to real-world sensor names.  
- Data is clean, consistent, and ready for backend API integration.

**Next Step:** Implement the backend using FastAPI + PostgreSQL to serve this cleaned data as JSON APIs.

## Step 2 — Backend API Development (FastAPI + PostgreSQL)

###  Objective
Create a FastAPI backend connected to the PostgreSQL database (`Task1_IOT_project`) that stores cleaned IoT data and serves it as JSON APIs for visualization.

---

### Components
- **`ingest.py`** → uploads each vertical’s data to PostgreSQL  
- **`main.py`** → FastAPI server exposing REST endpoints  

---

### Database Configuration
- **Database name:** `Task1_IOT_project`  
- **User:** `postgres`  
- **Password:** `Varshashri@1` (encoded as `%401` in URL)  
- **Host:** `localhost`  
- **Port:** `5432`  

**Connection string format:**


---

### `ingest.py` — Data Upload Script
**Purpose:** Read IoT datasets, split them by vertical (`AQ`, `WF`, `SL`), and push each table to PostgreSQL.

**Process Summary**
1. Load main dataset (`iot_dataset.csv`) and mapping file (`iot_dataset_mapping.csv`).  
2. Connect to PostgreSQL using SQLAlchemy `create_engine`.  
3. Split dataset by vertical and upload as individual tables:
   - `aq_data`
   - `wf_data`
   - `sl_data`
4. Replace existing tables if re-run.

**Run Command**
```bash
python ingest.py


## main.py — FastAPI Backend Summary
###  Purpose
`main.py` is the core FastAPI backend file that connects to the PostgreSQL database and exposes REST API endpoints for each IoT vertical (AQ, WF, SL).

###  Key Functionalities
- Connects to **PostgreSQL** database: `Task1_IOT_project`
- Initializes a **FastAPI** app with CORS middleware (to allow frontend access)
- Defines:
  - Root endpoint (`/`) → verifies backend–DB connection  
  - Dynamic endpoints (`/api/verticals/{vertical}`) → fetch data per vertical table

### Endpoints Overview
| Endpoint | Method | Description |
|-----------|--------|--------------|
| `/` | GET | Health check — confirms FastAPI connected to PostgreSQL |
| `/api/verticals/AQ` | GET | Fetches Air Quality data from `aq_data` table |
| `/api/verticals/WF` | GET | Fetches Water Flow data from `wf_data` table |
| `/api/verticals/SL` | GET | Fetches Smart Lighting data from `sl_data` table |

### How It Works
1. FastAPI fetches the `{vertical}` parameter from the URL.  
2. The table name is dynamically generated (e.g., `aq_data`).  
3. A SQL query is executed to read data from PostgreSQL.  
4. Missing values are handled (`fillna("NA")`).  
5. The data is returned as a JSON list to the frontend.

### To Run the Backend
```bash
uvicorn main:app --reload

#  IoT Data Visualization Dashboard — Frontend

###  Objective
This frontend visualizes IoT sensor data for **Air Quality (AQ)**, **Water Flow (WF)**, and **Smart Lighting (SL)** verticals using **React JS** and **Apache ECharts**.  
It dynamically fetches data from the FastAPI backend connected to PostgreSQL and renders interactive charts.

---

## Tech Stack
| Category | Technology |
|-----------|-------------|
| Framework | React JS |
| Charts | Apache ECharts |
| API Calls | Axios |
| Backend Source | FastAPI (localhost:8000) |
| Styling | Inline CSS + Poppins Font |


## Project Demonstration Video

Click the link below to watch the full working demonstration of the project 

**[Watch Project Video Here](##  Project Demonstration Video

Click the link below to watch the full working demonstration of the project 

**[Watch Project Video Here](https://drive.google.com/file/d/1nnGPk3sdnLSHnafjkb4DB_OQUx3GRlhd/view?usp=sharing)**  

###  Video Highlights
- Data Cleaning and Preprocessing (Python + Pandas)
- FastAPI Backend connected to PostgreSQL
- React Dashboard with Apache ECharts visualizations
- AQ, WF, and SL sensor dashboards shown live)**  

### Video Highlights
- Data Cleaning and Preprocessing (Python + Pandas)
- FastAPI Backend connected to PostgreSQL
- React Dashboard with Apache ECharts visualizations
- AQ, WF, and SL sensor dashboards shown live

### Developer
Varshashri Nagapuri
B.Tech – Artificial Intelligence & Data Science
ACE Engineering College | JNTUH
