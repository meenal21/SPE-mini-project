from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import math



app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any domain
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all HTTP headers
)

@app.get("/")
def render_as():
    return {"result":"Just the home page!"}

@app.get("/sqrt")
def square_root(x: float):
    if x < 0:
        raise HTTPException(status_code=400, detail="Cannot take square root of a negative number")
    return {"result": math.sqrt(x)}

@app.get("/factorial")
def factorial(x: int):
    if x < 0:
        raise HTTPException(status_code=400, detail="Factorial not defined for negative numbers")
    return {"result": math.factorial(x)}

@app.get("/ln")
def natural_log(x: float):
    if x <= 0:
        raise HTTPException(status_code=400, detail="Natural log not defined for non-positive values")
    return {"result": math.log(x)}

@app.get("/power")
def power(x: float, b: float):
    return {"result": math.pow(x, b)}


