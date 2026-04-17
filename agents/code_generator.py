from utils.llm import call_llm
from utils.prompts import code_prompt

def generate_code(plan):
    return call_llm(code_prompt(plan))
