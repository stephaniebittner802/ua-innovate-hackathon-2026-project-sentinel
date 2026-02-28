# UAInnovate2026


To set up .venv: 

cd fastapi_project
python3 -m venv .venv
source .venv/bin/activate
pip install "fastapi[standard]"


To run: 

in fastapi_project folder, run: 
uvicorn main:app --reload

backend is runnong on http://127.0.0.1:8000 