from utils.llm import call_llm
from utils.prompts import explain_prompt

def explain_code(code):
    return call_llm(explain_prompt(code))
