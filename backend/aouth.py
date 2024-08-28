from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl = "login")
class User(BaseModel):
    username: str
    fullname: str
    email: str
    disable: bool

class UserDB(User):
    password: str

users_db = {
    "sergio":{
        "username": "sergio",
        "fullname": "sergio alarcon",
        "email": "sergio.alarcon.car@gmail.com",
        "disable": False,
        "password": "121541"
    },
        "sergio_dos":{
        "username": "sergio_dos",
        "fullname": "sergio alarcon_dos",
        "email": "sergio.alarcon2.car@gmail.com",
        "disable": True,
        "password": "1541"
    }

}
async def current_user(token:str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST, datail = "la contraseña es incorrecta", headers={"www-autenticate": "bearer"}
        )
    return user


def search_user(username:str):
    if username in users_db:
        return UserDB(**users_db[username])
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not users_db:
                raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST, datail = "la contraseña es incorrecta"
        )

    user = search_user(form.username)
    if  not form.password == user.password:
                raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST, datail = "la contraseña es incorrecta"
        )
    
@app.get("/user/me")
async def me(user: User = Depends(current_user)):
    return user