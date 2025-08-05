#!/usr/bin/env python3
"""
Test script for ResumeRoast - The Roastmaster
Demonstrates the multi-agent resume analysis system
"""

import asyncio
from roast_master import RoastMaster

# Sample resume for testing
SAMPLE_RESUME = """
JOHN DOE
Software Engineer
john.doe@email.com | (555) 123-4567 | linkedin.com/in/johndoe

EDUCATION
Bachelor of Science in Computer Science
University of Technology | Graduated: 2022 | GPA: 3.2

EXPERIENCE
Software Developer Intern | Tech Startup Inc. | June 2021 - August 2021
• Worked on web development projects
• Used various programming languages
• Collaborated with team members
• Learned new technologies

Student Assistant | University IT Department | September 2020 - May 2022
• Helped students with computer problems
• Maintained computer lab equipment
• Assisted with software installation

PROJECTS
Personal Website | HTML, CSS, JavaScript
• Created a personal portfolio website
• Used responsive design principles
• Deployed on GitHub Pages

Weather App | Python, APIs
• Built a weather application
• Integrated with weather API
• Displayed current weather data

SKILLS
Programming Languages: Java, Python, JavaScript, HTML, CSS
Tools & Technologies: Git, VS Code, Eclipse, Windows, Mac
Soft Skills: Teamwork, Communication, Problem Solving
"""

SAMPLE_JOB_TITLE = "Software Engineer"

async def test_roast():
    """Test the resume roasting functionality"""
    
    print("🔥 ResumeRoast - The Roastmaster 🔥")
    print("=" * 50)
    print(f"Testing with job title: {SAMPLE_JOB_TITLE}")
    print()
    
    # Initialize RoastMaster
    roast_master = RoastMaster()
    
    try:
        print("🤖 Analyzing resume with multi-agent system...")
        print("   - Scoring Agent: Evaluating criteria...")
        print("   - Comparison Agent: Analyzing competitiveness...")
        print("   - Joke Agent: Crafting witty roasts...")
        print()
        
        # Get the roast
        analysis = await roast_master.roast_resume(SAMPLE_RESUME, SAMPLE_JOB_TITLE)
        
        # Display results
        print("📊 ANALYSIS RESULTS")
        print("=" * 50)
        print(f"Score: {analysis['score']} / 100")
        print(f"Verdict: {analysis['verdict']}")
        print(f"Summary: {analysis['summary']}")
        print()
        
        print("📈 SCORE BREAKDOWN")
        print("-" * 30)
        breakdown = analysis['breakdown']
        print(f"Technical Skills: {breakdown['technical_skills']}/25")
        print(f"Experience & Projects: {breakdown['experience_projects']}/25")
        print(f"Formatting & Structure: {breakdown['formatting_structure']}/15")
        print(f"Action & Impact: {breakdown['action_impact']}/15")
        print(f"ATS Keywords: {breakdown['ats_keywords']}/10")
        print(f"Initiative & Differentiators: {breakdown['initiative_differentiators']}/10")
        print()
        
        print("🏆 COMPETITIVE ANALYSIS")
        print("-" * 30)
        print(f"Market Position: {analysis['market_position']}")
        print(f"Competitive Analysis: {analysis['competitive_analysis']}")
        print()
        
        print("✅ STRENGTHS")
        for strength in analysis['strengths']:
            print(f"  • {strength}")
        print()
        
        print("⚠️  AREAS FOR IMPROVEMENT")
        for weakness in analysis['weaknesses']:
            print(f"  • {weakness}")
        print()
        
        print("➕ MISSING ELEMENTS")
        for element in analysis['missing_elements']:
            print(f"  • {element}")
        print()
        
        print("🔥 THE ROAST 🔥")
        print("=" * 50)
        for i, roast in enumerate(analysis['roast'], 1):
            print(f"{i}. {roast}")
        print()
        
        print("📝 FORMATTED RESPONSE")
        print("=" * 50)
        formatted = roast_master.format_response(analysis)
        print(formatted)
        
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # Run the test
    asyncio.run(test_roast()) 