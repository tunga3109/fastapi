from fastapi import FastAPI

app = FastAPI()

@app.get('/') # Точка входа
def hello():
    return 'hello world!' 