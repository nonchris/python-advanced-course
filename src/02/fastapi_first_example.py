# assuming this code is in a file named main.py
from fastapi import FastAPI

app = FastAPI(title="Demo Server", description="Simple Requests",
    version="v0.0.1", contact={
        "name": "Cyber AG",
        "url": "https://github.com/nonchris/",
    },
    terms_of_service="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
)

# routes can be defined using decorators
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# we can define path-parameters with {param} in the ressource path
# to access them we require the same-named parameter in our signature
# query parameters are required by defining them in the signature
@app.post("/api/v1/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


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
