from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import tempfile
import shutil
from utils.file_handler import process_file
from utils.solver import solve_question


app = FastAPI(title="TDS Solver API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "TDS Solver API is running. Send POST requests to /api/"}

@app.post("/api/")
async def solve(
    question: str = Form(...),
    file: UploadFile = File(None)
):
    """
    Solves a Tools in Data Science assignment question.
    
    Parameters:
    - question: The question text from the assignment
    - file: Optional file attachment
    
    Returns:
    - JSON object with the answer field
    """
    # Create a temporary directory for file operations
    temp_dir = None
    file_path = None
    
    try:
        if file:
            # Create temporary directory
            temp_dir = tempfile.mkdtemp()
            file_path = os.path.join(temp_dir, file.filename)
            
            # Save uploaded file
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            # Process the file if necessary (e.g., extract zip)
            file_path = process_file(file_path, temp_dir)
        
        # Generate the answer based on the question and file
        answer = solve_question(question, file_path)
        
        return {"answer": answer}
    
    finally:
        # Clean up temporary files
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)