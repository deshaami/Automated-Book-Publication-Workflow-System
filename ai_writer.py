from transformers import pipeline
import os

INPUT_FILE = "output/chapter1_text.txt"
OUTPUT_FILE = "output/chapter1_spun.txt"

# Load paraphrasing pipeline
writer = pipeline(
    "text2text-generation",
    model="ramsrigouthamg/t5_paraphraser",
    tokenizer="ramsrigouthamg/t5_paraphraser",
    device=-1  # CPU
)

# Function to paraphrase line-by-line
def spin_text(text):
    sentences = text.strip().split('.')
    result_text = ""
    for sentence in sentences:
        if sentence.strip():
            prompt = "paraphrase: " + sentence.strip()
            print("🔹Prompt:", prompt)
            result = writer(prompt, max_new_tokens=512, do_sample=True, temperature=0.6, top_k=50, top_p=0.95)[0]['generated_text']
            print("🔸Output:", result)
            result_text += result + ". "
    return result_text

# Optional duplicate remover
def remove_duplicates(text):
    sentences = text.split('. ')
    seen = set()
    unique = []
    for s in sentences:
        if s not in seen:
            seen.add(s)
            unique.append(s)
    return '. '.join(unique)

# Runner function
def run():
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Input file not found: {INPUT_FILE}")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    print("✍️ Starting spin_text...")
    spun = spin_text(text)
    spun = remove_duplicates(spun)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(spun)

    print(f"✅ Spun chapter saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    run()
