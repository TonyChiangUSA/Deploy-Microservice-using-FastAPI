## Installation 

pip install flask

## Installation for FastAPI 

pip install fastapi uvicorn



from flask import request

@app.route("/", methods=["GET"])
@app.route("/", methods=["POST"])

def home():
    return {"Hello": "GET"}
  
  
 ### Fast API 
@app.get("/")
@app.post("/")

@app.delete("/")
@app.patch("/")

def home():
    return {"Hello": "GET"}
