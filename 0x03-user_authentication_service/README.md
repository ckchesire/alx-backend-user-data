# Flask API Basics

This project demonstrates core Flask functionalities:

- Declaring API routes
- Setting and retrieving cookies
- Handling form and JSON data
- Returning custom HTTP status codes

## Setup

1. Install requirements:

```bash
pip install flask
````

2. Run the app:

```bash
python app.py
```

## Features

### 1. Routes

```python
@app.route('/')
def home():
    return "Welcome"

@app.route('/user/<username>')
def user(username):
    return f"User: {username}"

@app.route('/submit', methods=['POST'])
def submit():
    return "Submitted"
```

### 2. Cookies

```python
@app.route('/set-cookie')
def set_cookie():
    resp = make_response("Cookie set")
    resp.set_cookie('username', 'testuser')
    return resp

@app.route('/get-cookie')
def get_cookie():
    return request.cookies.get('username', 'Not set')
```

### 3. Form and JSON Data

```python
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    return f"Logged in as {username}"

@app.route('/api/data', methods=['POST'])
def json_data():
    data = request.get_json()
    return f"Received: {data}"
```

### 4. Status Codes

```python
@app.route('/created', methods=['POST'])
def created():
    return jsonify(message="Created"), 201

@app.route('/notfound')
def not_found():
    return "Not Found", 404
```
