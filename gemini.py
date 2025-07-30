import google.generativeai as genai

try:
    genai.configure()
except Exception as e:
    print(e)


# Rate the results with reinforcement learning
def rate_prompt_result():
    pass


# Helper function
def prompt_gemini(prompt):
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
    response = model.generate_content(prompt)
    return response


# Prompting kinds
def generate_hint(word, word_type, level):
    prompt = f"Provide a concise definition that serves as a hint for the word '{word}' without explicitly stating the word."
    response = prompt_gemini(prompt)
    return response.text, response.usage_metadata.prompt_token_count, response.usage_metadata.candidates_token_count

def generate_synonyms(word, word_type, level):
    prompt = f"Provide 3 more-or-less synonyms of the word '{word}'."
    response = prompt_gemini(prompt)
    return response.text, response.usage_metadata.prompt_token_count, response.usage_metadata.candidates_token_count

def generate_antonyms(word, word_type, level):
    prompt = f"Provide 3 more-or-less antonyms of the word '{word}'."
    response = prompt_gemini(prompt)
    return response.text, response.usage_metadata.prompt_token_count, response.usage_metadata.candidates_token_count

def modify_word_type(word, word_type, level):
    prompt = f"Provide the same word ({word}) as a different word type (not {word_type})."
    response = prompt_gemini(prompt)
    return response.text, response.usage_metadata.prompt_token_count, response.usage_metadata.candidates_token_count

