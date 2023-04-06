from fastapi import FastAPI, Response, Path
from fastapi.responses import FileResponse

app = FastAPI()

@app.get('/file', response_class=FileResponse)
def read_root():
    return 'index.html'