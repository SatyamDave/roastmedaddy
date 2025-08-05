from fastapi import FastAPI, Request, Form, UploadFile, File, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import uvicorn
from roast_master import RoastMaster
from utils import FileProcessor
import asyncio
import re
import html
from typing import Optional

app = FastAPI(title="ResumeRoast - The Roastmaster", version="1.0.0")

# Security middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"]  # Configure appropriately for production
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Initialize RoastMaster
roast_master = RoastMaster()

# Security validation functions
def sanitize_input(text: str) -> str:
    """Sanitize user input to prevent XSS"""
    if not text:
        return ""
    # HTML escape
    text = html.escape(text)
    # Remove potentially dangerous patterns
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'javascript:', '', text, flags=re.IGNORECASE)
    text = re.sub(r'data:', '', text, flags=re.IGNORECASE)
    return text.strip()

def validate_job_title(job_title: str) -> str:
    """Validate and sanitize job title"""
    if not job_title or len(job_title.strip()) == 0:
        raise HTTPException(status_code=400, detail="Job title is required")
    
    if len(job_title) > 200:
        raise HTTPException(status_code=400, detail="Job title too long")
    
    # Only allow alphanumeric, spaces, and common punctuation
    if not re.match(r'^[a-zA-Z0-9\s\-_.,&()]+$', job_title):
        raise HTTPException(status_code=400, detail="Invalid job title format")
    
    return sanitize_input(job_title)

def validate_resume_text(resume_text: Optional[str]) -> Optional[str]:
    """Validate and sanitize resume text"""
    if not resume_text:
        return None
    
    if len(resume_text) > 50000:  # 50KB limit
        raise HTTPException(status_code=400, detail="Resume text too long")
    
    return sanitize_input(resume_text)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/roast")
async def roast_resume(
    request: Request, 
    resume_text: str = Form(None), 
    job_title: str = Form(...),
    resume_file: UploadFile = File(None)
):
    """Roast a resume"""
    try:
        # Validate and sanitize inputs
        job_title = validate_job_title(job_title)
        resume_text = validate_resume_text(resume_text)
        
        # Handle file upload or text input
        if resume_file and resume_file.filename:
            # Process uploaded file
            file_content = await resume_file.read()
            extracted_text = FileProcessor.process_uploaded_file(file_content, resume_file.filename)
            if not extracted_text:
                raise HTTPException(status_code=400, detail="Could not extract text from uploaded file")
            resume_text = extracted_text
        elif resume_text:
            # Use text input
            pass
        else:
            raise HTTPException(status_code=400, detail="Either resume text or file must be provided")
        
        # Analyze the resume
        analysis = await roast_master.roast_resume(resume_text, job_title)
        
        return templates.TemplateResponse("result.html", {
            "request": request,
            "analysis": analysis,
            "resume_text": resume_text,
            "job_title": job_title
        })
    except HTTPException:
        raise
    except Exception as e:
        return templates.TemplateResponse("error.html", {
            "request": request,
            "error": "An error occurred while processing your request"
        })

@app.get("/api/roast")
async def api_roast(resume_text: str, job_title: str):
    """API endpoint for resume roasting"""
    try:
        # Validate and sanitize inputs
        job_title = validate_job_title(job_title)
        resume_text = validate_resume_text(resume_text)
        
        if not resume_text:
            raise HTTPException(status_code=400, detail="Resume text is required")
        
        analysis = await roast_master.roast_resume(resume_text, job_title)
        return {
            "success": True,
            "data": analysis,
            "formatted_response": roast_master.format_response(analysis)
        }
    except HTTPException:
        raise
    except Exception as e:
        return {
            "success": False,
            "error": "An error occurred while processing your request"
        }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 