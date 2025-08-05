import asyncio
from typing import Dict, Any, List
from agents import ScoringAgent, ComparisonAgent, JokeAgent

class RoastMaster:
    def __init__(self):
        self.scoring_agent = ScoringAgent()
        self.comparison_agent = ComparisonAgent()
        self.joke_agent = JokeAgent()
    
    async def roast_resume(self, resume_text: str, job_title: str) -> Dict[str, Any]:
        """Main method to analyze and roast a resume"""
        
        # Run all agents concurrently for better performance
        tasks = [
            self.scoring_agent.score_resume(resume_text, job_title),
            self.comparison_agent.analyze_competitiveness(resume_text, job_title)
        ]
        
        score_result, comparison_result = await asyncio.gather(*tasks)
        
        # Generate roast lines based on the analysis
        roast_lines = await self.joke_agent.generate_roast(
            resume_text, job_title, score_result, comparison_result
        )
        
        return {
            "score": score_result["total_score"],
            "verdict": score_result["verdict"],
            "summary": score_result["summary"],
            "breakdown": score_result["breakdown"],
            "specific_gaps": score_result.get("specific_gaps", []),
            "resume_highlights": score_result.get("resume_highlights", []),
            "market_position": comparison_result["market_position"],
            "strengths": comparison_result["strengths"],
            "weaknesses": comparison_result["weaknesses"],
            "missing_elements": comparison_result["missing_elements"],
            "competitive_analysis": comparison_result["competitive_analysis"],
            "role_specific_insights": comparison_result.get("role_specific_insights", []),
            "roast": roast_lines
        }
    
    def format_response(self, analysis: Dict[str, Any]) -> str:
        """Format the analysis into the required response format"""
        
        roast_text = "\n".join([f"{i+1}. {line}" for i, line in enumerate(analysis["roast"])])
        
        return f"""Score: {analysis['score']} / 100
Verdict: {analysis['verdict']}
Summary: {analysis['summary']}

🔥 Roast:
{roast_text}""" 