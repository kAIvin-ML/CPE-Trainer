import google.generativeai as genai

try:
    genai.configure()
except Exception as e:
    print(e)
    
def tryyy(word):
    model = genai.GenerativeModel('gemini-2.5-pro')
    prompt = f"Provide a concise definition that serves as a hint for the word '{word}' without explicitly stating the word."
    response = model.generate_content(prompt)
    return response.text.strip()

print(tryyy("apple"))