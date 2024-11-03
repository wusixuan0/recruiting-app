### Get Started
```
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
mkdir -p .streamlit/ && touch .streamlit/secrets.toml
```
Add `BACKEND_URL="YOUR_BACKEND_URL"` to `.streamlit/secrets.toml`
```
streamlit run app.py
```
Local URL: http://localhost:8501

### To Deploy
https://share.streamlit.io/new

https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app