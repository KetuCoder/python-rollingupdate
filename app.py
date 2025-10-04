from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    version = os.getenv('APP_VERSION', 'v1')
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python App</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #74ebd5 0%, #9face6 100%);
                color: #333;
                text-align: center;
                padding-top: 100px;
            }}
            h1 {{
                font-size: 3em;
                color: #fff;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }}
            p {{
                font-size: 1.5em;
                color: #222;
                background: rgba(255,255,255,0.8);
                display: inline-block;
                padding: 15px 30px;
                border-radius: 12px;
                box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
            }}
        </style>
    </head>
    <body>
        <h1>🚀 Hello From Python App!</h1>
        <p><strong>VERSION:</strong> {version}</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)