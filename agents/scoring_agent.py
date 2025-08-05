from typing import Dict, Any
from .base_agent import BaseAgent
from config import Config

class ScoringAgent(BaseAgent):
    def __init__(self):
        super().__init__(Config.SCORING_MODEL)
    
    async def score_resume(self, resume_text: str, job_title: str) -> Dict[str, Any]:
        """Score the resume based on multiple criteria"""
        
        prompt = f"""
You are Resume Roastmaster v1.0 — a brutally honest yet helpful AI designed to review and roast resumes with precision, personality, and professionalism. You specialize in evaluating *new graduate* resumes for specific job titles.

## SCORING RUBRIC (100 Points Total)

**[1] Technical Skill Match (25 pts)**  
- Resume includes relevant programming languages, frameworks, tools listed in target job.
- Bonus for advanced knowledge or certifications.
- CRITICAL: Compare skills against what the target role actually requires.

**[2] Experience & Projects Relevance (25 pts)**  
- Past internships, class projects, or open-source work clearly relate to the job.
- Described with metrics, outcomes, or technical depth.
- CRITICAL: Evaluate how well experiences align with the specific job requirements.

**[3] Formatting & Structure (15 pts)**  
- Clean layout, consistent spacing, readable fonts.
- Proper section headers, no typos or grammatical issues.
- Professional presentation that matches industry standards.

**[4] Action + Impact Writing (15 pts)**  
- Strong action verbs: "Built," "Optimized," "Shipped," etc.
- Shows *what* was done, *how* it was done, and *why* it mattered.
- Quantifiable results and measurable impact.

**[5] ATS Keyword Coverage (10 pts)**  
- Uses keywords from common job descriptions (e.g., REST API, Agile, SQL, CI/CD, etc.)
- No fluff: avoids vague terms like "hardworking," "fast learner."
- CRITICAL: Include job-specific keywords for the target role.

**[6] Initiative & Differentiators (10 pts)**  
- Evidence of standout qualities: side projects, leadership, research, blog, GitHub, etc.
- What makes this candidate unique for THIS specific role.

## DETAILED ANALYSIS REQUIREMENTS

**For the target job "{job_title}":**
1. Research what this role typically requires (skills, experience, projects)
2. Identify specific keywords and technologies this role demands
3. Understand the industry standards and expectations
4. Consider the company size and type (startup vs enterprise)

**Resume Analysis:**
- Extract specific skills, technologies, and experiences mentioned
- Identify gaps between resume content and job requirements
- Note specific achievements, metrics, and impact
- Evaluate the storytelling and narrative quality
- Assess technical depth and complexity of projects

Resume:
{resume_text}

Job Title: {job_title}

Provide your response in this exact JSON format:
{{
    "total_score": <number 0-100>,
    "verdict": "<Choose one: 'Strong candidate' | 'Some revisions needed' | 'Unlikely to get interview without major changes'>",
    "breakdown": {{
        "technical_skills": <score 0-25>,
        "experience_projects": <score 0-25>,
        "formatting_structure": <score 0-15>,
        "action_impact": <score 0-15>,
        "ats_keywords": <score 0-10>,
        "initiative_differentiators": <score 0-10>
    }},
    "summary": "<3-5 sentence paragraph explaining where the resume shines and where it falls short, grounded in the rubric. Be specific about what's missing for THIS job title.>",
    "specific_gaps": [
        "<specific skill or experience missing for this role>",
        "<another specific gap>"
    ],
    "resume_highlights": [
        "<specific strong point from the resume>",
        "<another highlight>"
    ]
}}
"""
        
        messages = [
            {"role": "system", "content": "You are a professional resume evaluator with expertise in technical hiring."},
            {"role": "user", "content": prompt}
        ]
        
        response = await self.call_llm(messages, temperature=0.3)
        result = self.parse_json_response(response)
        
        # Ensure we have valid scores
        if not result or "total_score" not in result:
            return {
                "total_score": 50,
                "verdict": "Some revisions needed",
                "breakdown": {
                    "technical_skills": 12,
                    "experience_projects": 12,
                    "formatting_structure": 8,
                    "action_impact": 8,
                    "ats_keywords": 5,
                    "initiative_differentiators": 5
                },
                "summary": "Unable to properly analyze resume. Default score assigned.",
                "specific_gaps": ["Unable to identify specific gaps"],
                "resume_highlights": ["Unable to identify highlights"]
            }
        
        return result 