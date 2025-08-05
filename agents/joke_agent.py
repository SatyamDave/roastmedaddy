from typing import Dict, Any, List
from .base_agent import BaseAgent
from config import Config

class JokeAgent(BaseAgent):
    def __init__(self):
        super().__init__(Config.JOKE_MODEL)
    
    async def generate_roast(self, resume_text: str, job_title: str, score_data: Dict, comparison_data: Dict) -> List[str]:
        """Generate 5 witty roast lines based on the resume analysis"""
        
        prompt = f"""
You are Resume Roastmaster v1.0 — a brutally honest yet helpful AI designed to review and roast resumes with precision, personality, and professionalism. Your tone: sharp, witty, constructive. You are never generic. Never fake-flattering. Always insightful.

## ROAST GENERATION REQUIREMENTS

**CRITICAL: Make each roast SPECIFIC to the resume content and target job**

**Resume Content Analysis:**
- Extract specific skills, technologies, projects, and experiences mentioned
- Identify exact phrases, bullet points, and descriptions used
- Note specific achievements, metrics, and impact mentioned
- Pay attention to formatting, structure, and presentation details

**Target Job Analysis:**
- Research what "{job_title}" typically requires
- Identify specific skills, technologies, and experiences this role demands
- Understand industry standards and expectations for this position
- Consider the gap between resume content and job requirements

**Roast Strategy:**
1. **Target specific content** - Reference exact phrases, skills, or experiences from the resume
2. **Job-specific criticism** - Point out gaps between resume and target role requirements
3. **Technical accuracy** - If they mention specific technologies, roast their implementation or depth
4. **Quantifiable gaps** - If they lack metrics, roast the absence of specific numbers
5. **Industry relevance** - Compare their experience to what the target role actually needs

Resume:
{resume_text}

Job Title: {job_title}

Score Analysis: {score_data}
Competitive Analysis: {comparison_data}

**🔥 Generate 5 SPECIFIC roast lines:**

**Line 1:** Target a specific skill, technology, or experience mentioned in the resume that's weak or irrelevant for this job
**Line 2:** Roast a specific bullet point or achievement that lacks impact or specificity  
**Line 3:** Point out a specific gap between their experience and what this role requires
**Line 4:** Target formatting, structure, or presentation issues specific to their resume
**Line 5:** Offer a constructive suggestion disguised as a roast about what they're missing for this specific role

**Use this additional data for context:**
- Specific gaps identified: {score_data.get('specific_gaps', [])}
- Resume highlights: {score_data.get('resume_highlights', [])}
- Role-specific insights: {comparison_data.get('role_specific_insights', [])}

**Requirements:**
- Reference EXACT content from the resume (skills, projects, experiences)
- Compare against what "{job_title}" actually requires
- Be specific about technologies, frameworks, or methodologies mentioned
- Include job-specific keywords and requirements in your criticism
- Make it clear you've analyzed THEIR specific resume for THIS specific role

Provide your response as a JSON array of exactly 5 strings:
["<specific roast line 1>", "<specific roast line 2>", "<specific roast line 3>", "<specific roast line 4>", "<specific roast line 5>"]
"""
        
        messages = [
            {"role": "system", "content": "You are The Roastmaster - witty, clever, and brutally honest about resume flaws."},
            {"role": "user", "content": prompt}
        ]
        
        response = await self.call_llm(messages, temperature=0.8)
        result = self.parse_json_response(response)
        
        # Ensure we have valid roast lines
        if not result or not isinstance(result, list) or len(result) != 5:
            return [
                "Your resume formatting is so basic, it looks like it was written in Notepad during a power outage.",
                "These bullet points are so vague, they could apply to literally any job in the universe.",
                "Your skills section reads like a tech buzzword bingo card from 2015.",
                "I've seen more metrics in a fortune cookie than in your entire work experience.",
                "This resume has less personality than a corporate training video about workplace safety."
            ]
        
        return result 