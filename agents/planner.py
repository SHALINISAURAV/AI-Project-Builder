from utils.llm import call_llm
from utils.prompts import planner_prompt

def planner(user_input):
    return call_llm(planner_prompt(user_input))
