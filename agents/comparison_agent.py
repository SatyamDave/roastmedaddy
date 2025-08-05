from typing import Dict, Any, List
from .base_agent import BaseAgent
from config import Config

class ComparisonAgent(BaseAgent):
    def __init__(self):
        super().__init__(Config.COMPARISON_MODEL)
    
    async def analyze_competitiveness(self, resume_text: str, job_title: str) -> Dict[str, Any]:
        """Analyze how the resume compares to industry standards and competition"""
        
        prompt = f"""
You are an expert recruiter who has reviewed thousands of resumes for {job_title} positions. 
Analyze this resume and compare it to industry standards and what top candidates typically present.

## COMPETITIVE ANALYSIS REQUIREMENTS

**For the target job "{job_title}":**
1. Research what this specific role requires (skills, experience, projects, technologies)
2. Understand industry standards and expectations for this position
3. Identify what top candidates typically have for this role
4. Consider company size and industry context

**Resume Analysis:**
- Extract specific skills, technologies, projects, and experiences mentioned
- Identify achievements, metrics, and impact described
- Evaluate technical depth and complexity
- Assess alignment with target role requirements

**Competitive Benchmarking:**
- Compare against typical candidates for this role
- Identify what makes them stand out (or not)
- Point out specific gaps compared to top performers
- Suggest specific improvements for this role

Resume:
{resume_text}

Job Title: {job_title}

Provide your analysis in this exact JSON format:
{{
    "market_position": "<where this resume stands compared to other candidates - bottom 25%, middle 50%, top 25%, or top 10%>",
    "strengths": ["<specific strength relevant to this role>", "<another specific strength>", "<another specific strength>"],
    "weaknesses": ["<specific weakness for this role>", "<another specific weakness>", "<another specific weakness>"],
    "missing_elements": ["<specific missing element for this role>", "<another specific missing element>"],
    "competitive_analysis": "<2-3 sentences on how this compares to top candidates SPECIFIC TO THIS ROLE>",
    "role_specific_insights": ["<specific insight about their fit for this role>", "<another role-specific insight>"]
}}
"""
        
        messages = [
            {"role": "system", "content": "You are a senior recruiter with 10+ years experience in technical hiring."},
            {"role": "user", "content": prompt}
        ]
        
        response = await self.call_llm(messages, temperature=0.4)
        result = self.parse_json_response(response)
        
        # Ensure we have valid data
        if not result or "market_position" not in result:
            return {
                "market_position": "middle 50%",
                "strengths": ["Unable to analyze strengths"],
                "weaknesses": ["Unable to analyze weaknesses"],
                "missing_elements": ["Unable to identify missing elements"],
                "competitive_analysis": "Unable to provide competitive analysis.",
                "role_specific_insights": ["Unable to provide role-specific insights"]
            }
        
        return result 