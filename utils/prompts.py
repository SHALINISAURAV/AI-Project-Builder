# PLANNER PROMPT
def planner_prompt(user_input):
    return f"""
You are an expert AI/ML project planner.

User wants to build: {user_input}

Create:
1. Problem Statement
2. Dataset suggestions (free sources with links if possible)
3. Step-by-step approach
4. Tech stack (simple, beginner-friendly)
5. Expected output

Keep it structured and clear.
Return output in clean markdown format with headings.
"""


# CODE GENERATOR PROMPT
def code_prompt(plan):
    return f"""
You are a senior Python ML engineer.

Based on this plan:
{plan}

Generate:
- Complete Python code
- Use simple libraries (pandas, sklearn, matplotlib)
- Include comments
- Keep it beginner-friendly
- No unnecessary complexity

Also include:
- sample dataset loading
- basic visualization
- model training and evaluation

Ensure the code runs without errors and is complete.

Return output in clean markdown format with headings.
"""


# REVIEWER PROMPT
def review_prompt(code):
    return f"""
You are a professional code reviewer.

Improve this code:
{code}

Focus on:
- readability
- efficiency
- best practices
- error handling
- code structure

Ensure the final code is clean and production-ready.

Return improved version only.
Return output in clean markdown format with headings.
"""


# EXPLAINER PROMPT
def explain_prompt(code):
    return f"""
Explain this code in simple terms like teaching a beginner:

{code}

Break into:
- What each part does
- Why it's used
- Key concepts

Use simple language and examples where possible.

Return output in clean markdown format with headings.
"""
