from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from datetime import datetime, timezone
from io import BytesIO

app = FastAPI()

@app.get("/email_image")
async def email_image(user_id: str, offer_id: str = "unknown"):
    # Simulate DB update
    print(f"Email opened by {user_id} for offer {offer_id} at {datetime.now(timezone.utc)}")

    # Serve a visible image
    image_bytes = open("banner.png", "rb").read()
    return StreamingResponse(BytesIO(image_bytes), media_type="image/png")
