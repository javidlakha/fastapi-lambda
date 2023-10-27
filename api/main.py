import os
from typing import Union

import uvicorn
from fastapi import FastAPI
from mangum import Mangum

root_path = os.getenv("STAGE", default="")
app = FastAPI(root_path=f"/{root_path}")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


handler = Mangum(app)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
