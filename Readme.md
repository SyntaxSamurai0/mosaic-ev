# Mosaic EV Aggregation API
## Requirements
- `Python 3.7+`
- `FastAPI`
- `httpx`
- `uvicorn`

## Setup
1. Clone the Repository.
```bash
git clone https://github.com/devsaud247/mosaic-ev.git
cd mosaic-ev
```

2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate 
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Run the application
```bash
uvicorn main:app --reload
```

###### The API will be accessible at http://127.0.0.1:8000

5. Endpoint `GET /ev-data/`

- Description: Fetches and aggregates electric vehicle data by the specified model year.
- Query Parameter: model_year: The year of the vehicle model.
- Response: Returns the total number of vehicles and the average electric range, grouped by vehicle make.

##### Example Request:

`http://127.0.0.1:8000/ev-data/?model_year=2020`

##### Example Response:
```json
{
    "Tesla": {
        "total_vehicles": 200,
        "average_range": 250
    },
    "Nissan": {
        "total_vehicles": 150,
        "average_range": 200
    }
}
```

