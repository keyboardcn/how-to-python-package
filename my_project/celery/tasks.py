from celery import Celery
import time
import json
celery_app = Celery(
    "worker",
    broker = "redis://localhost:6379/0",
    backend= "redis://localhost:6379/0"
)

@celery_app.task
def get_root():
    '''
    '''
    print("will sleep 1 second")
    time.sleep(1000)
    print("wake up")
    with open("user.json", 'r', encoding="utf-8") as f:
        data =json.load(f)
    print(data)
    return data