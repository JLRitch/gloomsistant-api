# Gloomsistant API
This is an API to manage data for Gloomhaven characters and play sessions.

## Setup
```powershell
# install requirements
python -m pip install -r requirements.txt

# initialize local dev db
python -m db.initialize
```

## Run the API (locally)
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

## Run the API (docker)
**Build and run the api with docker-compose up:**
```bash
# run a dev environment
docker-compose --env-file ./config/.env.dev up

# run a 'test' environment, no dev requirements install
docker-compose --env-file ./config/.env.test up
```

You can make requests to the api endpoints such as: http://localhost:8000/players

You can see the interactive documentation at: http://localhost:8000/docs

You can access the PGAdmin Interface at: http://localhost:80

### Execute Tests within docker-compose (dev environment):
```bash
docker-compose exec api sh /usr/test/test-all.sh
```
