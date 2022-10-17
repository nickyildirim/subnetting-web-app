"""
Gunicorn pointer to forward requests
"""
from subapp import app

if __name__ == "__main__":
    app.run()
