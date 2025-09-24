from fastapi import FastAPI
from fastapi.responses import StreamingResponse, JSONResponse
from datetime import datetime, timezone
from io import BytesIO

app = FastAPI()
open_events = []  # In-memory log

@app.get("/")
def read_root():
    return {"message": "FastAPI is running on Vercel!"}
    
@app.get("/email_image")
async def email_image(user_id: str, offer_id: str = "unknown"):
    open_events.append({
        "user_id": user_id,
        "offer_id": offer_id,
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

    image_bytes = open("banner.png", "rb").read()
    return StreamingResponse(BytesIO(image_bytes), media_type="image/png")

@app.get("/get_open_events")
async def get_open_events():
    return JSONResponse(content=open_events)

@app.post("/clear_open_events")
async def clear_open_events():
    open_events.clear()
    return {"status": "cleared"}
