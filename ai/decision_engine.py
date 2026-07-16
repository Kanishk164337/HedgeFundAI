from ai.prompt_builder import PromptBuilder
from llm.groq_client import ask_groq


class DecisionEngine:

    def __init__(self):
        self.prompt_builder = PromptBuilder()

    def analyze(self, symbol, analysis):

        prompt = self.prompt_builder.build(symbol, analysis)

        response = ask_groq(prompt)

        return response