from utils.llm import call_llm
from utils.prompts import review_prompt

def review_code(code):
    return call_llm(review_prompt(code))
