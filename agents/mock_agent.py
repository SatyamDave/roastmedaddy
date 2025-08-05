import random
from typing import Dict, Any, List

class MockScoringAgent:
    """Mock scoring agent that provides realistic sample responses"""
    
    def __init__(self):
        self.sample_scores = [
            {"total_score": 67, "breakdown": {"relevance": 14, "clarity": 12, "impact": 10, "ats_alignment": 15, "initiative": 16}, "summary": "Your resume shows solid technical skills but lacks quantifiable achievements and could benefit from better ATS optimization."},
            {"total_score": 82, "breakdown": {"relevance": 18, "clarity": 16, "impact": 17, "ats_alignment": 15, "initiative": 16}, "summary": "Strong resume with good technical alignment and clear achievements, though some bullet points could be more specific."},
            {"total_score": 45, "breakdown": {"relevance": 8, "clarity": 10, "impact": 7, "ats_alignment": 12, "initiative": 8}, "summary": "Resume needs significant improvement in structure, impact metrics, and relevance to the target position."},
            {"total_score": 73, "breakdown": {"relevance": 15, "clarity": 14, "impact": 13, "ats_alignment": 16, "initiative": 15}, "summary": "Good foundation with relevant skills, but missing key metrics and could use stronger action verbs."},
        ]
    
    async def score_resume(self, resume_text: str, job_title: str) -> Dict[str, Any]:
        """Return a realistic sample score"""
        return random.choice(self.sample_scores)

class MockComparisonAgent:
    """Mock comparison agent that provides realistic sample responses"""
    
    def __init__(self):
        self.sample_analyses = [
            {
                "market_position": "middle 50%",
                "strengths": ["Solid technical foundation", "Relevant project experience", "Good educational background"],
                "weaknesses": ["Lacks quantifiable achievements", "Generic bullet points", "Missing industry-specific keywords"],
                "missing_elements": ["Metrics and KPIs", "Leadership experience", "Industry certifications"],
                "competitive_analysis": "Competitive for entry-level positions but needs stronger differentiation for mid-level roles."
            },
            {
                "market_position": "top 25%",
                "strengths": ["Strong technical skills", "Quantified achievements", "Relevant industry experience"],
                "weaknesses": ["Could use more leadership examples", "Some skills need updating"],
                "missing_elements": ["Advanced certifications", "Industry-specific projects"],
                "competitive_analysis": "Strong candidate profile that stands out among peers with clear achievements and relevant experience."
            },
            {
                "market_position": "bottom 25%",
                "strengths": ["Basic technical knowledge", "Some project work"],
                "weaknesses": ["Poor formatting", "Vague descriptions", "Outdated skills"],
                "missing_elements": ["Relevant experience", "Technical depth", "Professional achievements"],
                "competitive_analysis": "Significant improvement needed to compete effectively in the current job market."
            }
        ]
    
    async def analyze_competitiveness(self, resume_text: str, job_title: str) -> Dict[str, Any]:
        """Return a realistic sample analysis"""
        return random.choice(self.sample_analyses)

class MockJokeAgent:
    """Mock joke agent that provides realistic sample roasts"""
    
    def __init__(self):
        self.sample_roasts = [
            [
                "Your bullet points are so generic, they could apply to a professional pillow fluffer.",
                "I've seen more metrics in a fortune cookie than in your entire work experience section.",
                "Your skills section reads like a tech buzzword bingo card from 2015.",
                "This formatting is so basic, it looks like it was written in Notepad during a power outage.",
                "Your resume has less personality than a corporate training video about workplace safety."
            ],
            [
                "These action verbs are so weak, they're practically in a coma.",
                "Your experience section is like reading a job description written by someone who's never had a job.",
                "The only thing more outdated than your skills is your formatting approach.",
                "Your achievements are so vague, they could be describing a day at the park.",
                "This resume has the impact of a feather falling on a pillow."
            ],
            [
                "Your technical skills are like a restaurant menu with no prices - impressive but meaningless.",
                "These bullet points are so fluffy, they could be used as insulation.",
                "Your resume formatting is giving me strong 'My First Resume' vibes.",
                "The only thing more generic than your descriptions is your LinkedIn headline.",
                "Your achievements section is like a mystery novel - lots of questions, no answers."
            ],
            [
                "This resume is so vanilla, it could be served at a corporate ice cream social.",
                "Your skills list is longer than your actual achievements - that's not a good sign.",
                "The formatting is so inconsistent, it looks like it was assembled by a committee of cats.",
                "Your experience descriptions are like reading a dictionary - technically correct but painfully boring.",
                "This resume has the personality of a spreadsheet - functional but forgettable."
            ]
        ]
    
    async def generate_roast(self, resume_text: str, job_title: str, score_data: Dict, comparison_data: Dict) -> List[str]:
        """Return realistic sample roast lines"""
        return random.choice(self.sample_roasts) 