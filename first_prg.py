<<<<<<< HEAD
import ollama
model_name = "llama3.2:latest"
prompt = "Explain about LLMs in simple words"
response = ollama.generate(model = model_name, prompt = prompt)
=======
import ollama
model_name = "llama3.2:latest"
prompt = "Explain about LLMs in simple words"
response = ollama.generate(model = model_name, prompt = prompt)
>>>>>>> fd6858d5b0b529cc6ebabb389da88535ca174026
print(response.response)