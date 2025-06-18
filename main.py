from fastapi import FastAPI

from src.huita import main

app = FastAPI()

@app.get("/")
async def get_main(input_path, output_path, yolo_path):
    return main(input_path, output_path, yolo_path)
