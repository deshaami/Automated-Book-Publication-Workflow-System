from transformers import pipeline
import torch

print("🧠 Loading Reviewer Model...")

# Load grammar correction model
model_name = "prithivida/grammar_error_correcter_v1"
device = 0 if torch.cuda.is_available() else -1

# Load the pipeline
reviewer = pipeline(
    "text2text-generation",
    model=model_name,
    tokenizer=model_name,
    device=device
)

print("🔎 Reviewer Model Loaded!")

def review_text(text):
    prompt = "grammar: " + text
    result = reviewer(prompt, max_new_tokens=128)[0]['generated_text']
    return result
