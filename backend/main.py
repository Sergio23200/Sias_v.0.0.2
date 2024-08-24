from datetime import date
from fastapi import FastAPI, Request
import models
app = FastAPI
model = models
@app.post("/login")