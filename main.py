from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(title="File Server for AuthApp")

@app.get("/getupdatefile", summary="Get Update File", description="Serves the 'update_file.zip' as a download.")
async def get_update_file():
    file_path = "update_file.zip"  # adjust file path if needed
    return FileResponse(path=file_path, filename="update_file.zip", media_type="application/octet-stream")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
