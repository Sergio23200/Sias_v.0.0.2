from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl = "login")