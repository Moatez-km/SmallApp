from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import User,UserBase



app =FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users =[
    {"id":1, "name": "moatez","email": "moatez@gmail.com"},
    {"id":2,"name":"asma","email":"asma@gmail.com"}
    ]

next_id =3

@app.get("/")
def root():
    return {"message": "Welcome to our Website"}

#Read all users
@app.get("/users",response_model=list[User])
def get_users():
    return users


@app.post("/users",response_model=User)
def create_user(user:UserBase):
    global next_id

    new_user={
        "id": next_id,
        "name":user.name,
        "email":user.email
    }
    users.append(new_user)
    next_id +=1

    return new_user
