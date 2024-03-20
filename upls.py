from fastapi import FastAPI, File, UploadFile
import pathlib
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File()):
    pathlib.Path("uploads").mkdir(exist_ok=True)
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"file_path": file_path}


app.mount("/static", StaticFiles(directory="static"), name="static")
