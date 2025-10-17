from transformers import pipeline

 
summariser = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_summary(text):
    if not text or text.strip() == "":
        return "Summary not available"
    
    #    engaging 
    prompt = f"Write a short, engaging and slightly witty summary of this article:\n\n{text}"
    
 
    input_len = len(text.split())  
    max_len = min(60, max(15, int(input_len * 0.8)))   # max 60, min 15
    min_len = max(5, int(input_len * 0.3))            # min 5, at least 30% of input length
    
    
    summary = summariser(
        prompt,
        max_new_tokens=max_len,
        min_length=min_len,
        do_sample=False
    )
    
 
    result = summary[0]
    return result.get("generated_text") or "No summary generated."
