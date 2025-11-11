# my_project/main.py

# Import the function from your installed package
import uvicorn
import json
from typing import Union
from datetime import date
from pydantic import BaseModel, EmailStr
from hello_package.greeter import say_hello
from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from my_project.celery.tasks import get_root, celery_app
from celery.result import AsyncResult

app = FastAPI()
class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    joined: date

@app.get('/rootuser')
async def get_root_user():
    with open("user.json", 'r', encoding="utf-8") as f:
        data =json.load(f)
    user = User(**data[0])
    return data

@app.get('/')
async def get_root_user_task():
    task = get_root.delay()
    return {"task_id": task.id, "status": "queued"}

@app.websocket("/ws/status/{task_id}")
async def websocket_endpoint(websocket: WebSocket, task_id):
    await websocket.accept()
    while True:
        task_result = AsyncResult(task_id, app=celery_app)
        if task_result.state == "SUCCESS": 
            await websocket.send_json({"status": "SUCCESS", "result": task_result.result})
            break
        elif task_result.state == "FAILURE":
            await websocket.send_json({"status": "FAILURE"})
        else:
            await websocket.send_json({"status": task_result.state})


def run_my_app():
    """
    This is the main function of your application that uses the hello_package.
    """
    print("--- Starting My Application ---")

    # Call the function from the imported package
    say_hello()

    print("--- Application Finished ---")

if __name__ == "__main__":
    run_my_app()
    uvicorn.run("main:app", port=8000, reload=True)
