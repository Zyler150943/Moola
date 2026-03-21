from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv
import os
import uvicorn

dotenv_path = find_dotenv()

if dotenv_path:
    load_dotenv(dotenv_path)
else:
    print("Файл .env не найден")

password = os.getenv("DB_PASSWORD")

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
