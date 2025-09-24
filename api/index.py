from flask import Flask, request, send_file
from io import BytesIO
from datetime import datetime, timezone

app=Flask(__name__)

@app.route('email_image')
def email_image():
    user_id=request.args.get('user_id')
    offer_id=request.args.get('offer_id','unknown'
    
    print(f"Email opened by {user_id} fr offer {offer_id} at {datetime.now(timezone.utc)}"))
    return send_file("banner.png",mimetype="image/png")
    