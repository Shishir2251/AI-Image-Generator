import uvicorn
from fastapi import FastAPI
# --- FIX: IMPORT CORSMiddleware HERE ---
from fastapi.middleware.cors import CORSMiddleware 
from routes import router

app = FastAPI(title="AI Image Generator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)