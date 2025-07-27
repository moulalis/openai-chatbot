import json
from datetime import datetime, timedelta
from pathlib import Path

DOCTORS_FILE = Path("data/doctors.json")
APPOINTMENTS_FILE = Path("data/appointments.json")

def load_json(file_path):
    if not file_path.exists():
        return []
    with open(file_path, "r") as f:
        return json.load(f)

def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

def list_doctors():
    doctors = load_json(DOCTORS_FILE)
    return {"doctors": doctors}

def is_slot_available(doctor_name, date, time_slot):
    appointments = load_json(APPOINTMENTS_FILE)
    for appt in appointments:
        if (
            appt["doctor_name"].lower() == doctor_name.lower()
            and appt["date"] == date
            and appt["time_slot"] == time_slot
        ):
            return False
    return True

def book_appointment(user_name, doctor_name, date, time_slot):
    if not user_name.strip():
        return {"status": "failed", "reason": "User name cannot be empty."}

    if not is_slot_available(doctor_name, date, time_slot):
        return {"status": "failed", "reason": f"{doctor_name} is not available on {date} at {time_slot}"}

    appointments = load_json(APPOINTMENTS_FILE)
    appointment = {
        "user_name": user_name,
        "doctor_name": doctor_name,
        "date": date,
        "time_slot": time_slot
    }
    appointments.append(appointment)
    save_json(APPOINTMENTS_FILE, appointments)
    return {"status": "success", "message": f"Appointment booked with {doctor_name} on {date} at {time_slot} for {user_name}."}

def get_functions():
    return [
        {
            "name": "list_doctors",
            "description": "List all available doctors with their specialties.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        },
        {
            "name": "book_appointment",
            "description": "Book an appointment with a doctor for a given date and time.",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_name": {
                        "type": "string",
                        "description": "Name of the user booking the appointment"
                    },
                    "doctor_name": {
                        "type": "string",
                        "description": "Name of the doctor"
                    },
                    "date": {
                        "type": "string",
                        "description": "Date of the appointment in YYYY-MM-DD format"
                    },
                    "time_slot": {
                        "type": "string",
                        "description": "Time slot for the appointment (e.g., '10:00 AM')"
                    }
                },
                "required": ["user_name", "doctor_name", "date", "time_slot"]
            }
        }
    ]
