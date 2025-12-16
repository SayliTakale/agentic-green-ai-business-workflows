from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms.base import LLM

class DummyLLM(LLM):
    def _call(self, prompt, stop=None):
        return "GREEN" if "green" in prompt.lower() else "BASELINE"

    @property
    def _llm_type(self):
        return "dummy"

class GreenAIAgent:
    def __init__(self):
        self.prompt = PromptTemplate(
            input_variables=["baseline_time", "green_time"],
            template=(
                "Baseline model time: {baseline_time}\n"
                "Green model time: {green_time}\n"
                "Choose the more energy efficient model."
            ),
        )
        self.llm = DummyLLM()
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def decide(self, baseline_time, green_time):
        if green_time < baseline_time:
            return "GREEN"
        return "BASELINE"