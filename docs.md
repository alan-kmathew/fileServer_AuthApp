# File Server API Documentation

## Overview
This FastAPI application provides an endpoint to download a file.

## Endpoints

### GET /serve-file
- **Summary:** Serve File
- **Description:** Serves the `update_file.zip` as a download.
- **Response:** Returns the file with media type `application/octet-stream`.

## Running the Server
Execute the server with:
```bash
python main.py
```

Access the API docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
