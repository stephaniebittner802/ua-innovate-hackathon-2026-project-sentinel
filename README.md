# Project Sentinel - UA Innovate Hackathon 2026

**Project Sentinel** is a full-stack intelligence dashboard designed to monitor resource levels across multiple locations. It displays trends in an interactive chart, forecasts future shortages via a simple machine-learning algorithm, and extracts data from reports via a Large Language Model.

---

## Demo

<p align="center">
  <img src="assets/demo_projectSentinel.gif" alt="Project Sentinel Demo" />
</p>

---

## Features

**Interactive Dashboard**
  - Visualize historical stock trends across multiple locations
  - View the 20 most recent intelligence entries
  - Select and filter by specific locations (Wakanda, New Asgard, Sokovia, Sanctum Sanctorum, Avengers Compound)
  - Adjust the number of historical days displayed to analyze short-term or long-term trends (7 days, 30 days, 90 days, all)

**Machine Learning Forecasting**
  - Uses StatsModels (OLS Regression) to forecast stock depletion
  - Predicts when a resource is projected to reach zero

**Summary of Resources Out**
  - Provides a table of resources that are currently depleted
  - Highlights critical locations where stock levels have reached zero

**Live Intelligence Table**
  - Displays when a report was submitted, the affected location, the resource mentioned, and the status.

**Live Intelligence Report Submission**
  - Submit raw text reports through a frontend form

**AI-Powered Data Extraction**
  - Uses the OpenAI API (gpt-4.1-mini) to extract:
    - Location
    - Resource
    - Quantity level (scale 0–4; 0 = none, 4 = high)
  - Then saved in the Live Intelligence Table

**Redaction Layer**
  - Redacts sensitive information before AI processing
  - Ensures secure data handling

---

## Tech Stack

### Frontend
- Languages: HTML + CSS + JavaScript
- Framework: React
- Vite
- Styling System: Tailwind CSS
- Libraries: Recharts (Data Visualization), Radix UI (Dropdown Menu)

### Backend
- Language: Python
- Framework: FastAPI
- Containerization: Docker
- Database: PostgreSQL
- ASGI Web Server: Uvicorn
- Libraries: Sqlmodel, Polars (Data Processing), StatsModels (OLS Regression), OpenAI API (LLM Structured Extraction)


## **Setup Instructions**

### 1. **Clone the repository**

```bash
git clone https://github.com/stephaniebittner802/ua-innovate-hackathon-2026-project-sentinel.git
cd ua-innovate-hackathon-2026-project-sentinel
```

### 2. **Set up Frontend**

```bash
cd project-sentinel-frontend
npm install
npm run dev
```
The frontend is locally hosted at: http://localhost:5173/

### 3. **Set up Backend**

To set up .venv: 

```bash
cd fastapi_project
python3 -m venv .venv
source .venv/bin/activate
pip install "fastapi[standard]"
```

Make sure you have the **OpenAI API** keys set up in your environment. To do this, create a `.env` file in the `backend` directory with the following:

```env
OPENAI_API_KEY=your_openai_api_key
```

To run: 
```bash
in fastapi_project folder, run: 
uvicorn app.main:app --reload
```
Note that the backend is running on http://127.0.0.1:8000

To add historic data, add the csv to fastapi_project/data and run the following command in the fastapi_project directory:
```bash
python -m scripts.import_historic_stock_data --file data/filename.csv
```

Note that the Docker environment must be running before you do this. To do that, you run the command: 
```bash
docker compose up -d
```

## **License**

This project is open-source and available under the MIT License.
