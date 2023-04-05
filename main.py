from fastapi import FastAPI

app = FastAPI(
    title='Trading App'
)

@app.get('/') # Точка входа
def hello():
    return 'hello world!' 