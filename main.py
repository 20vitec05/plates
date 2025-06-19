import os
from fastapi import FastAPI

from src.huita import main

app = FastAPI()

yolo_path = "../weights/YOLO/best.pt"
input_path = "../datatest/origin"
output_path = "../datatest/processed"

@app.get("/")
async def get_main(input_path=input_path, output_path = output_path, yolo_path=yolo_path):
    for image in os.walk(input_path):
        return main(image, output_path, yolo_path)
