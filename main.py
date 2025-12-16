from models.email_classification import classify_email
from analysis.energy_analysis import estimate_energy
from agent.langchain_agent import GreenAIAgent

text = "Customer is unhappy with delayed delivery"

baseline_model = "bert-base-uncased"
green_model = "distilbert-base-uncased"

baseline_result, baseline_time = classify_email(text, baseline_model)
green_result, green_time = classify_email(text, green_model)

agent = GreenAIAgent()
decision = agent.decide(baseline_time, green_time)

baseline_energy = estimate_energy(baseline_time)
green_energy = estimate_energy(green_time)

print("Decision:", decision)
print("Baseline Energy:", baseline_energy)
print("Green Energy:", green_energy)
