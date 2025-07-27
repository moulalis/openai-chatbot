import json
from functions import list_doctors, book_appointment, get_functions
from datetime import datetime
from openai import OpenAI
import os

# Load API key securely (from env or config)
# openai_client = OpenAI()
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



SYSTEM_PROMPT = """
You are a helpful assistant for booking doctor appointments.
Doctors are available Mon–Sat: 10am–1pm and 4pm–8pm.
List available doctors from doctors.json and book based on availability.
Always collect user name and appointment details before booking.
"""

def run_chat():
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    print("🤖 Welcome to Super Clinic! How can I help you today?")
    while True:
        user_input = input("👤 You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        messages.append({"role": "user", "content": user_input})

        response = openai_client.chat.completions.create(
            model="gpt-4-0613" ,
            messages=messages,
            functions=get_functions(),
            function_call="auto"
        )

        response_message = response.choices[0].message

        if response_message.function_call:
            func_name = response_message.function_call.name
            args = json.loads(response_message.function_call.arguments)

            if func_name == "list_doctors":
                result = list_doctors()
            elif func_name == "book_appointment":
                result = book_appointment(**args)
            else:
                result = {"error": f"Function {func_name} not implemented"}

            messages.append({
                "role": "function",
                "name": func_name,
                "content": json.dumps(result)
            })
        else:
            content = response_message.content
            if content:
                print(f"🤖 {content}")
                messages.append({"role": "assistant", "content": content})

if __name__ == "__main__":
    run_chat()
