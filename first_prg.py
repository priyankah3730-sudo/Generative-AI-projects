import ollama
model_name = "llama3.2:latest"
prompt = "Explain about LLMs in simple words"
response = ollama.generate(model = model_name, prompt = prompt)
print(response.response)