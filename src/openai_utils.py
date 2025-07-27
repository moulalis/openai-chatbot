from openai import OpenAI

import json
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


DOCTOR_FILE = 'data/doctors.json'

def load_doctors():
    with open(DOCTOR_FILE) as f:
        doctors = json.load(f)
    doctor_list = "\n".join([f"- Dr. {d['name']} ({d['specialty']})" for d in doctors])
    return doctor_list

def chat_with_openai(user_input, history=None):
    doctors_info = load_doctors()

    SYSTEM_PROMPT = f"""
You are a helpful assistant for a CLI-based Doctor Appointment Booking System.

📅 Doctor Availability:
- Days: Monday to Saturday
- Time: 10AM–1PM and 4PM–8PM

👨‍⚕️ Available Doctors:
{doctors_info}

You help users by listing doctors, showing available time slots, and guiding them to book appointments. 
Keep responses short and command-line friendly.
"""

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    if history:
        messages.extend(history)
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.4
    )

    reply = response.choices[0].message.content.strip()
    return reply

