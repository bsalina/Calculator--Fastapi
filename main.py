from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from fastapi.staticfiles import StaticFiles

if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")
    
app.mount("/static", StaticFiles(directory="static"), name="static")

app = FastAPI()

class Operation(BaseModel):
    a: float
    b: float

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/add")
def add(op: Operation):
    return {"result": op.a + op.b}

@app.post("/subtract")
def subtract(op: Operation):
    return {"result": op.a - op.b}

@app.post("/multiply")
def multiply(op: Operation):
    return {"result": op.a * op.b}

@app.post("/divide")
def divide(op: Operation):
    if op.b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": op.a / op.b}




