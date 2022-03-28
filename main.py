import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"key": "Hello"}


@app.post("/slot/")
def create_file(num: int):
    r = range(1, 1 + num)
    t = str(list(r))

    with open("f.txt", "w") as f:
        f.write(t)

    return {"message": "file_unloaded"}


@app.get("/slot/")
def return_file(num: int):
    with open("f.txt", "r") as f:
        ini_list = f.read().strip('][').split(', ')

    return {"message": ini_list}


@app.delete("/slot/")
def delete_file():
    p = os.path.abspath("f.txt")
    os.remove(p)

    return {"message": "deletede file"}

