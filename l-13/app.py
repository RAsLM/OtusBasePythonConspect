from typing import Optional

import uvicorn
from fastapi import FastAPI, Body, Depends, Query
from schemas import UserIn, UserOut, User, CalcInput
import crud
from dependencies import get_user_by_token

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World!!"}


@app.get("/{user_id}/friends/")
def get_friends(user_id: int):
    return {
        "id": user_id,
        "friends": [
            {
                "id": 5343,
                "bd": None,
                "close_friends": False
            }
        ]
    }



@app.post("/items/")
def create_item(data: dict = Body(...)):
    """
    # Header
    ## Header 2
    ### Header 3

    - item
    - item
    - item

    some `code` and _some italic_

    Creates new item
    """
    return {
        "item": data,
    }


@app.get("/add/")
def add_to_numbers(a: int, b: int):
    return {"sum": a + b}

@app.get("/sub/")
def sub_to_numbers(q: Optional[str] = Query(None), calc_input: str = Query(...)):
    return {
        "q": q,
        "calc_input": calc_input
        #"sub": calc_input.a - calc_input.b,
    }


@app.get("/users/me", response_model=UserOut)
def get_me(user: User = Depends(get_user_by_token)):
    return user

@app.post("/users/", response_model=UserOut)
def create_user(user_in: UserIn):
    # return  {"data": user_in.dict()}
    # return UserOut(id=123, username=user_in.username)
    user = crud.create_user(user_in)
    return user

@app.get("/users/", response_model=list[UserOut])
def get_users():
    users = crud.list_users()
    return users
# def main():
#     uvicorn.run()
#
#
# if __name__ == '__main__':
#     main()
