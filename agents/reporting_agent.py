import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import json
from datetime import datetime
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

# Load environment variables
load_dotenv()

class ReportingAgent:
    def __init__(self, perception: dict, reasoning: dict, criteria: dict):
        self.perception = perception
        self.reasoning = reasoning
        self.criteria = criteria
        os.makedirs("report", exist_ok=True)

    def plot_clip(self):
        if self.criteria.get("generate_summary", True):
            plt.plot(self.reasoning["clip_scores"])
            plt.title("CLIP Similarity")
            plt.savefig("report/clip_scores.png")

    def save_json(self):
        data = {
            "timestamp": datetime.now().isoformat(),
            "perception": self.perception,
            "reasoning": self.reasoning
        }
        with open("report/video_eval.json", "w") as f:
            json.dump(data, f, indent=4)

    def generate_summary(self):
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY not found in environment!")

        prompt = PromptTemplate.from_template("""
Given perception metrics:
{perception}

And reasoning metrics:
{reasoning}

Write a concise technical report summarizing:
- Temporal Coherence
- Semantic Consistency
- Scene Change Robustness

Score video out of 10.
""")
        llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.3)
        chain = LLMChain(prompt=prompt, llm=llm)
        return chain.run({"perception": self.perception, "reasoning": self.reasoning})

    def run(self):
        self.plot_clip()
        self.save_json()
        return self.generate_summary()