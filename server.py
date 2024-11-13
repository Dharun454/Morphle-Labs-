from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/')
def htop():
    # Replace 'Your Full Name' with your actual full name
    name = "Dharunraj A"  
    
    # Retrieve the system username in a safer way for Codespace
    username = os.environ.get("USER", "Default User")  
    
    # Get the current time in IST (Indian Standard Time)
    ist_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    # Get the output of the 'top' command (only the first sample)
    top_output = subprocess.getoutput('top -b -n 1')

    # Return the data in a formatted HTML structure
    return f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <p><strong>TOP output:</strong></p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run()