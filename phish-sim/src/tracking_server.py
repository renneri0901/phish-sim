from flask import Flask, send_file
import logging

# Set up logging to track when the email is opened
logging.basicConfig(filename='email_tracking.log', level=logging.INFO)

app = Flask(__name__)

@app.route('/track/<email_id>')
def track(email_id):
    # Log the event with email ID and timestamp
    logging.info(f"Email opened by: {email_id} at timestamp")
    
    # Send a transparent 1x1 pixel image
    return send_file("pixel.png", mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
