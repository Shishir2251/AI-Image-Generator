# --- services.py ---
from huggingface_hub import InferenceClient
from config import settings
from PIL import Image
from io import BytesIO

# Initialize the client once (NO provider argument!)
client = InferenceClient(
    model=settings.MODEL_ID, 
    token=settings.HF_TOKEN
)

def process_image_with_ai(image_bytes: bytes, prompt: str):
    # This code is correct for the img2img task
    input_image = Image.open(BytesIO(image_bytes)).convert("RGB")
    STRENGTH = 0.8 

    generated_image = client.image_to_image(
        image=input_image, 
        prompt=prompt, 
        strength=STRENGTH
    )
    
    output_buffer = BytesIO()
    generated_image.save(output_buffer, format="JPEG")
    return output_buffer.getvalue()