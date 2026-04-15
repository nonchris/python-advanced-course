from fastapi import FastAPI,  Request, status, HTTPException
from fastapi.responses import JSONResponse
from uuid import uuid4

app = FastAPI()

users_db = {}

@app.post("/register")
async def register(username: str):
    # Generate a UUID4
    user_id = str(uuid4())

    users_db[user_id] = username

    # Create a response JSON with success message and set the "user_id" cookie
    response = JSONResponse(content={"message": "Registration successful"}, status_code=200)
    response.set_cookie(key="user_id", value=user_id)

    return response


@app.get("/whoami")
async def whoami(req: Request):
    c = req.cookies.get("user_id")
    if not c:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="I don't know you!",
        )

    return f"Your are: {users_db[c]}!"

def start():
    """ Make the server runnable as script """
    print("Starting the arcade tournament...")
    import os
    import uvicorn
    uvicorn.run(
        app,
        host=os.getenv("HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", 3001)),
        log_level="info",
    )

if __name__ == '__main__':
    start()
