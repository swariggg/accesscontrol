from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class loginnuser(BaseModel):
    email:str
    contra:str
user_dtb={
    "email":"arianaremache2007@gmail.com",
    "contraseña":"AeI546"
}
@app.get("/login")
def login(user:loginnuser):
    if user==user_dtb["email"] and user.contra ==user_dtb["contraseña"]:
        return {"mensaje":"login exitosos"}
    else:
        return {"mensaje":"login fallido"}
