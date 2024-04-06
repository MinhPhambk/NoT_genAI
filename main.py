from fastapi import FastAPI, File, UploadFile
from read_pdf import read_pdf
from llama_parse import LlamaParse
import asyncio
import nest_asyncio
app = FastAPI()
nest_asyncio.apply()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    with open(file.filename, "wb") as buffer:
        buffer.write(await file.read())

    text = read_pdf(file.filename)
    return {"filename": file.filename,
                "content": text}
