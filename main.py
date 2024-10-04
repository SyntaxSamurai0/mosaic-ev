from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

EV_API_URL = "https://data.wa.gov/resource/f6w7-q2d2.json"

@app.get("/ev-data/")
async def get_ev_data(model_year: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(EV_API_URL, params={"$limit": 1000})
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch EV data")
        
        ev_data = response.json()

        filtered_data = [car for car in ev_data if car.get("model_year") == str(model_year)]
        
        if not filtered_data:
            return {"message": f"No data found for model year {model_year}"}
        
        aggregated_data = {}
        for car in filtered_data:
            make = car.get("make")
            range_miles = car.get("electric_range", 0)
            
            if make in aggregated_data:
                aggregated_data[make]["total_vehicles"] += 1
                aggregated_data[make]["total_range"] += int(range_miles) if range_miles else 0
            else:
                aggregated_data[make] = {
                    "total_vehicles": 1,
                    "total_range": int(range_miles) if range_miles else 0
                }
        
        result = {
            make: {
                "total_vehicles": data["total_vehicles"],
                "average_range": data["total_range"] / data["total_vehicles"] if data["total_vehicles"] > 0 else 0
            }
            for make, data in aggregated_data.items()
        }
        
        return result
