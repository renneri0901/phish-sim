from flask import Flask, redirect, request
import datetime

app = Flask(__name__)

@app.route('/track_click/<email_id>')
def track_click(email_id):
    """Log click with timestamp, IP, and email ID."""
    with open("clicks.log", "a") as f:
        f.write(f"[{datetime.datetime.now()}] Link clicked from {request.remote_addr} | Email ID: {email_id}\n")
    
    # Redirect to real or fake login page
    return redirect("YOUR_LOGIN_PAGE")  # Replace with actual login page URL or a fake one

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
