from fastapi import FastAPI, HTTPException
import math

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Scientific Calculator API"}

@app.get("/add")
def add(a: float, b: float):
    return {"operation": "addition", "result": a + b}

@app.get("/subtract")
def subtract(a: float, b: float):
    return {"operation": "subtraction", "result": a - b}

@app.get("/multiply")
def multiply(a: float, b: float):
    return {"operation": "multiplication", "result": a * b}

@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"operation": "division", "result": a / b}

@app.get("/sqrt")
def sqrt(x: float):
    if x < 0:
        raise HTTPException(status_code=400, detail="Cannot compute square root of a negative number")
    return {"operation": "square root", "result": math.sqrt(x)}

@app.get("/power")
def power(base: float, exponent: float):
    return {"operation": "exponentiation", "result": math.pow(base, exponent)}

@app.get("/log")
def log(x: float, base: float = 10):
    if x <= 0:
        raise HTTPException(status_code=400, detail="Logarithm undefined for non-positive numbers")
    return {"operation": "logarithm", "result": math.log(x, base)}
