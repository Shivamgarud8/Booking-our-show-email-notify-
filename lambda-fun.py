import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import random

def generate_seat_numbers(seat_count):
    """Generate seat numbers like A1, A2, A3..."""
    seats = []
    for i in range(seat_count):
        seats.append(f"A{i+1}")
    return ", ".join(seats)

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        name = body.get("name")
        email = body.get("email")
        phone = body.get("phone")
        date = body.get("date")
        seats = int(body.get("seats", 0))

        if not all([name, email, phone, date, seats]):
            return {
                "statusCode": 400,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                },
                "body": json.dumps({"message": "Missing required fields"})
            }

        # Seat number generator
        seat_numbers = generate_seat_numbers(seats)

        # Email credentials (from Lambda environment variables)
        sender_email = os.environ.get("EMAIL_USER")
        sender_password = os.environ.get("EMAIL_PASS")
        admin_email = os.environ.get("ADMIN_EMAIL")  # Your email

        # --- SMTP Setup ---
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # --- Email to User ---
        user_subject = "🎟️ Your Seat Confirmation - BookMySeat"
        user_body = f"""
        Hello {name},

        ✅ Your booking has been successfully confirmed!

        Booking Details:
        📅 Date: {date}
        💺 Seats: {seat_numbers}
        📞 Phone: {phone}
        📧 Email: {email}

        Thank you for choosing BookMySeat!
        """

        user_msg = MIMEMultipart()
        user_msg["From"] = sender_email
        user_msg["To"] = email
        user_msg["Subject"] = user_subject
        user_msg.attach(MIMEText(user_body, "plain"))

        server.sendmail(sender_email, email, user_msg.as_string())

        # --- Email to Admin ---
        admin_subject = f"📩 New Booking from {name}"
        admin_body = f"""
        New booking received!

        👤 Name: {name}
        📧 Email: {email}
        📞 Phone: {phone}
        📅 Date: {date}
        💺 Seats: {seat_numbers}

        Please confirm the booking in your dashboard if needed.
        """

        admin_msg = MIMEMultipart()
        admin_msg["From"] = sender_email
        admin_msg["To"] = admin_email
        admin_msg["Subject"] = admin_subject
        admin_msg.attach(MIMEText(admin_body, "plain"))

        server.sendmail(sender_email, admin_email, admin_msg.as_string())

        server.quit()

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
            },
            "body": json.dumps({"message": "Booking confirmed! Emails sent to user and admin."})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
            },
            "body": json.dumps({"message": "Internal Server Error", "error": str(e)})
        }
