# 🧠 Resume Roastmaster

A brutally honest AI-powered resume reviewer that provides detailed analysis, scoring, and witty roasts for new graduate job applications.

## 🔐 Security Features

### ✅ Security Checklist Applied

- **Input Sanitization**: All text inputs are HTML-escaped and validated
- **File Upload Security**: 
  - MIME type validation
  - File size limits (10MB max)
  - Extension whitelist (.pdf, .docx, .txt only)
  - Filename validation (alphanumeric + safe chars)
- **XSS Prevention**: 
  - HTML escaping on all outputs
  - Script tag removal
  - Dangerous protocol filtering
- **API Security**:
  - Environment variable configuration
  - No hardcoded secrets
  - Input length limits
  - Error message sanitization
- **Headers & CSP**:
  - Content Security Policy
  - X-Frame-Options: DENY
  - X-Content-Type-Options: nosniff
  - X-XSS-Protection enabled
- **CORS & Trusted Hosts**: Configurable middleware
- **Rate Limiting**: Built into FastAPI (configurable)

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenRouter API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SatyamDave/roastmedaddy.git
   cd roastmedaddy
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your OpenRouter API key
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

5. **Access the application**
   - Web UI: http://localhost:8000
   - API: http://localhost:8000/api/roast

## 📦 Deployment

### Vercel Deployment

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Deploy**
   ```bash
   vercel --prod
   ```

3. **Set environment variables in Vercel dashboard**
   - `OPENROUTER_API_KEY`: Your OpenRouter API key
   - `SITE_URL`: Your production domain

### Environment Variables

```env
# Required
OPENROUTER_API_KEY=your_openrouter_api_key_here

# Optional
SITE_URL=https://your-domain.com
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
CORS_ORIGINS=https://your-domain.com,https://www.your-domain.com
```

## 🏗️ Architecture

### Multi-Agent System
- **ScoringAgent**: Evaluates resume against job requirements
- **ComparisonAgent**: Analyzes competitiveness vs other candidates  
- **JokeAgent**: Generates witty, specific roasts

### Security Architecture
- **Input Validation**: Multi-layer validation (client + server)
- **File Processing**: Secure extraction with sanitization
- **Output Escaping**: XSS prevention on all rendered content
- **Error Handling**: Sanitized error messages

## 🔧 API Usage

### POST /roast
Submit a resume for analysis:

```bash
curl -X POST "http://localhost:8000/roast" \
  -F "job_title=Software Engineer" \
  -F "resume_text=Your resume content here"
```

### GET /api/roast
API endpoint for programmatic access:

```bash
curl "http://localhost:8000/api/roast?job_title=Software%20Engineer&resume_text=Your%20resume%20content"
```

## 📊 Scoring System

The system evaluates resumes across 6 categories:

1. **Technical Skill Match** (25 pts)
2. **Experience & Projects Relevance** (25 pts)  
3. **Formatting & Structure** (15 pts)
4. **Action + Impact Writing** (15 pts)
5. **ATS Keyword Coverage** (10 pts)
6. **Initiative & Differentiators** (10 pts)

## 🛡️ Security Best Practices

### For Production Deployment

1. **Environment Variables**: Never commit API keys
2. **HTTPS Only**: Use SSL/TLS in production
3. **Rate Limiting**: Implement request throttling
4. **Monitoring**: Set up error tracking and logging
5. **Regular Updates**: Keep dependencies updated

### File Upload Safety

- Files are processed in memory (not saved to disk)
- All extracted text is sanitized before processing
- MIME type validation prevents malicious uploads
- File size limits prevent DoS attacks

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details

## 🆘 Support

- **Issues**: Report bugs on GitHub
- **Security**: Email security@yourdomain.com for vulnerabilities
- **API**: Check OpenRouter documentation for API limits

---

**Built with ❤️ and 🔥 by the Resume Roastmaster team** 