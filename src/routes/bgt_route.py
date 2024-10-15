from fastapi import APIRouter, status
from worker import task_one

router = APIRouter()


@router.get("/write")
def write_to_file():
    result = task_one.delay()
    return result.id
