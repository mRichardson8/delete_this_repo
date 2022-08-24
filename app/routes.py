from app import app

@app.route('/')
def index():
    return f"Hello index route"
