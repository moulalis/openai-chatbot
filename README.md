
# 🩺 Doctor Appointment Chatbot with OpenAI Function Calling

## 📌 Features

- 🤖 Chatbot interface powered by OpenAI GPT with Function Calling.
- 📅 Smart appointment booking: Only books during doctor’s available time.
- 📉 Prevents double booking by checking `appointments.json`.
- 📖 Lists doctors and their available time slots (Weekdays: 10am–1pm & 4pm–8pm).
- 🔁 Dynamic availability updated after every booking.
- ✅ Clean modular structure with `main.py` and `functions.py`.

## 🧠 How It Works

Doctors are available **Monday to Friday**, during:
- Morning: `10:00 AM` to `01:00 PM`
- Evening: `04:00 PM` to `08:00 PM`

Once a user books an appointment, that slot is removed from the availability, ensuring that no overlapping bookings can occur.

## 🧑‍💻 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/moulalis/openai-chatbot
cd openai-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your OpenAI API Key

```bash
export OPENAI_API_KEY="your-api-key-here"
```

### 4. Run the Chatbot

```bash
python main.py
```

## 📝 Example Usage

```
🤖 Welcome to Super Clinic! How can I help you today?

You: Book a cardiologist for tomorrow at 10:00 AM

🤖 Dr. Ayesha (Cardiologist) is available.
✅ Appointment booked for 2025-07-28 at 10:00 AM.
```


## 💡 Learnings

This project demonstrates how to:
- Use the **OpenAI Python SDK v1.0+** with **Function Calling**.
- Handle user intents to fetch available slots or book an appointment.
- Maintain a dynamic appointment system without hardcoding doctor availability.
