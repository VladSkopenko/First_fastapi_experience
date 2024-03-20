from fastapi import FastAPI, File, UploadFile
import pathlib

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File()):
    pathlib.Path("uploads").mkdir(exist_ok=True)
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"file_path": file_path}
