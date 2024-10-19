from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)


def get_top_output():
    process = subprocess.Popen(['top', '-b', '-n', '1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stderr:
        return f"Error: {stderr.decode()}"
    return stdout.decode()


def get_ist_time():
    ist = pytz.timezone('Asia/Kolkata')
    return datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')


def get_system_username():
    try:
        return os.getlogin()
    except OSError:
        return os.getenv('USER', 'unknown')

@app.route('/htop')
def htop():
    full_name = "Davis Joseph"  
    system_username = get_system_username()
    ist_time = get_ist_time()
    top_output = get_top_output()

    
    html = f"""
    <html>
    <head><title>System Information - /htop</title></head>
    <body>
        <h1>System Information</h1>
        <p><b>Name:</b> {full_name}</p>
        <p><b>Username:</b> {system_username}</p>
        <p><b>Server Time (IST):</b> {ist_time}</p>
        <h2>Top Output</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
