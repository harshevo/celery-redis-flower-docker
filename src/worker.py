import os
import time
from fastapi import HTTPException
from celery import Celery

redis_url = "redis://redis:6379/0"

celery_app = Celery(
    "celery_app",
    broker=redis_url,
    backend=redis_url
)

@celery_app.task(name="task_one")
def task_one():
    try:
        with open(f"{os.getcwd()}/message.txt", "a") as f:
            for _ in range(20):
                time.sleep(1)
                print("hello")  
                f.write("Hello\n")        

    except Exception as e:
        return {"detail": f"failed to write {e}"}


