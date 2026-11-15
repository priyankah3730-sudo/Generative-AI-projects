import ollama

messages = [{"role" : "system","content" : "You are a helpful assistant"}]

model_name = "llama3.2:latest"

while True:
    user_input = input("Me : ")
    user_role = {"role" : "user", "content" : user_input }
    messages.append(user_role)
    
    response = ollama.chat(model = model_name,messages = messages)
    response = response.message.content 
    print("Assistant : ",response)
    assistant_role = {"role" : "assistant", "content" : response}