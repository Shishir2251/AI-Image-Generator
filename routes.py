from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import Response
from services import process_image_with_ai

router = APIRouter()

@router.get("/")
def health_check():
    return {"status": "ok", "message": "API is ready."}

@router.post("/generate")
async def generate_endpoint(
    file: UploadFile = File(...), 
    prompt: str = Form(...)
):
    try:
        # Read the file
        file_bytes = await file.read()
        
        # Call the logic from services.py
        generated_image_bytes = process_image_with_ai(file_bytes, prompt)
        
        # Return the image
        return Response(content=generated_image_bytes, media_type="image/jpeg")

    except Exception as e:
        print(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail=str(e))