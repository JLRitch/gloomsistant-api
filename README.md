# Gloomsistant API
This is an API to manage data for Gloomhaven characters and play sessions.

## Setup
```powershell
# install requirements
python -m pip install -r requirements.txt

# initialize local dev db
python -m db.initialize
```

## Run the API
**Development:**
```powershell
uvicorn main:app --reload
```

You can make requests to the api endpoints such as: http://127.0.0.1:8000/players
You can see the interactive documentation at: http://127.0.0.1:8000/docs

**Test:**
```powershell
uvicorn main:app
```