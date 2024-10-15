from fastapi import FastAPI
from routes.bgt_route import router as bg_router
import uvicorn

app = FastAPI()

app.include_router(bg_router)

if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True)
