import ollama

messages = [
    {
        "role" : "system",
        "content" : "you are a funny friend,in one line"
    },
    {
        "role" : "user",
        "content" : "Explain about llms in one line"
    }
]
model_name = "llama3.2:latest"
response = ollama.chat(model = model_name,messages = messages)

print(response.message.content)