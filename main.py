from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os

app = FastAPI()


# Root route
@app.get("/")
def read_root():
    return {"message": "Financial Analyzer Running"}


# Analyze endpoint
@app.post("/analyze")
async def analyze_file(file: UploadFile = File(...)):
    try:
        # Create uploads folder if not exists
        os.makedirs("uploads", exist_ok=True)

        file_path = f"uploads/{file.filename}"

        # Save uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 🔥 Here you can connect your agents/tools later
        # For now returning dummy response

        return {
            "status": "success",
            "filename": file.filename,
            "message": "File uploaded successfully. Analysis completed."
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )