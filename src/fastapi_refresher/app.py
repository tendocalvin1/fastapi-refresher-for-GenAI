from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
async def home():
    return {"message": "Tendo Calvin, here! I am learning FastAPI for GenAI engineering."}