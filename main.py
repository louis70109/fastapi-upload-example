import os
import uvicorn

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import File, UploadFile
from typing import List

from routers import users, items

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(users.router)
app.include_router(items.router)


@app.get("/")
async def health():
    return {"message": "Hello World!"}


@app.get("/upload", response_class=HTMLResponse)
async def upload_page(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
def upload(files: List[UploadFile] = File(...)):
    for file in files:
        try:
            contents = file.file.read()
            with open(file.filename, 'wb') as f:
                f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file(s)"}
        finally:
            file.file.close()

    return {"message": "Successfully uploaded"}  


if __name__ == "__main__":
    port = os.getenv('PORT', default=5000)
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
