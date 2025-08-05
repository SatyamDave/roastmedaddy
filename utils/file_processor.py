import PyPDF2
import io
import mimetypes
import magic
from docx import Document
from typing import Optional
import re

class FileProcessor:
    """Utility class to process uploaded files and extract text"""
    
    @staticmethod
    def extract_text_from_pdf(file_content: bytes) -> Optional[str]:
        """Extract text from PDF file content"""
        try:
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_content))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text.strip()
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
            return None
    
    @staticmethod
    def extract_text_from_docx(file_content: bytes) -> Optional[str]:
        """Extract text from DOCX file content"""
        try:
            doc = Document(io.BytesIO(file_content))
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text.strip()
        except Exception as e:
            print(f"Error extracting text from DOCX: {e}")
            return None
    
    @staticmethod
    def extract_text_from_txt(file_content: bytes) -> str:
        """Extract text from plain text file content"""
        try:
            return file_content.decode('utf-8').strip()
        except UnicodeDecodeError:
            try:
                return file_content.decode('latin-1').strip()
            except:
                return file_content.decode('cp1252').strip()
    
    @staticmethod
    def validate_file(file_content: bytes, filename: str) -> bool:
        """Validate file type and content"""
        # Check file size (max 10MB)
        if len(file_content) > 10 * 1024 * 1024:
            raise ValueError("File size exceeds 10MB limit")
        
        # Validate filename
        if not re.match(r'^[a-zA-Z0-9._-]+$', filename):
            raise ValueError("Invalid filename")
        
        # Check file extension
        allowed_extensions = {'pdf', 'docx', 'txt'}
        file_extension = filename.lower().split('.')[-1]
        if file_extension not in allowed_extensions:
            raise ValueError(f"Unsupported file type: {file_extension}")
        
        # Validate MIME type
        try:
            mime_type = magic.from_buffer(file_content, mime=True)
            allowed_mimes = {
                'application/pdf',
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                'text/plain'
            }
            if mime_type not in allowed_mimes:
                raise ValueError(f"Invalid MIME type: {mime_type}")
        except Exception:
            # Fallback to extension-based validation
            pass
        
        return True
    
    @staticmethod
    def sanitize_text(text: str) -> str:
        """Sanitize extracted text to prevent XSS"""
        # Remove potentially dangerous characters
        text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.IGNORECASE | re.DOTALL)
        text = re.sub(r'<[^>]*>', '', text)  # Remove HTML tags
        text = re.sub(r'javascript:', '', text, flags=re.IGNORECASE)
        text = re.sub(r'data:', '', text, flags=re.IGNORECASE)
        return text.strip()
    
    @staticmethod
    def process_uploaded_file(file_content: bytes, filename: str) -> Optional[str]:
        """Process uploaded file and return extracted text"""
        # Validate file first
        FileProcessor.validate_file(file_content, filename)
        
        file_extension = filename.lower().split('.')[-1]
        
        try:
            if file_extension == 'pdf':
                text = FileProcessor.extract_text_from_pdf(file_content)
            elif file_extension == 'docx':
                text = FileProcessor.extract_text_from_docx(file_content)
            elif file_extension == 'txt':
                text = FileProcessor.extract_text_from_txt(file_content)
            else:
                raise ValueError(f"Unsupported file type: {file_extension}")
            
            # Sanitize the extracted text
            if text:
                return FileProcessor.sanitize_text(text)
            return None
            
        except Exception as e:
            raise ValueError(f"Error processing file: {str(e)}") 