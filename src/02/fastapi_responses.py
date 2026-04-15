# assuming this code is in a file named main.py
import uuid

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()  # the main webserver

class User(BaseModel):
    name: str
    id: uuid.UUID | None = None

    def model_post_init(self, ctx):
        if self.id is None:
            self.id = uuid.uuid4()


@app.post("/api/v1/register/{u_name}")
async def read_item(request: Request):
    u = User(name=request.path_params["u_name"])
    resp = JSONResponse(content=u.model_dump_json(), status_code=200)
    return resp


def start():
    """Start the arcade tournament."""
    print("Starting the arcade tournament...")
    import os
    import uvicorn
    uvicorn.run(
        app,
        host=os.getenv("HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", 3001)),
        log_level="info"
    )


if __name__ == '__main__':
    start()
