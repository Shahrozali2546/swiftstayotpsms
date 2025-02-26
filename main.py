# import streamlit as st
# import pandas as pd
# from twilio.rest import Client
# import random

# TWILIO_SID = ""
# TWILIO_AUTH_TOKEN = ""
# TWILIO_PHONE = "SWIFTSTAY"


# # Initialize Twilio Client
# client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# # OTP Sending Function
# def send_otp(phone_number):
#     otp = random.randint(100000, 999999)  # Generate Random OTP
#     message = f"Your verification OTP is {otp}. Please don't share with anyone."
    
#     try:
#         sms = client.messages.create(
#             body=message,
#             from_=TWILIO_PHONE,
#             to=phone_number
#         )
#         return f"📲 OTP sent to {phone_number} | SID: {sms.sid}"
#     except Exception as e:
#         return f"❌ Error sending OTP to {phone_number}: {str(e)}"

# # Streamlit UI
# st.title("📩 OTP Sender")

# # Country Code Selection with Country Name
# countries = {
#     "Afghanistan (+93)": "+93",
#     "Albania (+355)": "+355",
#     "Algeria (+213)": "+213",
#     "Argentina (+54)": "+54",
#     "Australia (+61)": "+61",
#     "Brazil (+55)": "+55",
#     "Canada (+1)": "+1",
#     "China (+86)": "+86",
#     "France (+33)": "+33",
#     "Germany (+49)": "+49",
#     "India (+91)": "+91",
#     "Indonesia (+62)": "+62",
#     "Italy (+39)": "+39",
#     "Japan (+81)": "+81",
#     "Mexico (+52)": "+52",
#     "Pakistan (+92)": "+92",
#     "Russia (+7)": "+7",
#     "Saudi Arabia (+966)": "+966",
#     "South Africa (+27)": "+27",
#     "Spain (+34)": "+34",
#     "United Arab Emirates (+971)": "+971",
#     "United Kingdom (+44)": "+44",
#     "United States (+1)": "+1"
# }

# # Combined Input for Country Code and Phone Number
# col1, col2 = st.columns([2, 3])
# with col1:
#     country_name = st.selectbox("🌍 Select Country", list(countries.keys()))
#     country_code = countries[country_name]
# with col2:
#     phone_number = st.text_input("📞 Enter Phone Number", placeholder="1234567890")

# # Button to Send OTP
# if st.button("🚀 Send OTP"):
#     if phone_number:
#         full_number = country_code + phone_number
#         with st.spinner("Sending OTP... Please wait"):
#             response = send_otp(full_number)
#         st.write(response)
#     else:
#         st.error("❌ Please enter a valid phone number!")















# import time
# import streamlit as st
# import random

# # OTP Sending Function (Without SMS)
# def generate_otp():
#     return random.randint(100000, 999999)  # Random 6-digit OTP

# # Streamlit UI
# st.title("📩 SWIFTSTAY SMS OTP Generator")

# # Country Code Selection
# countries = {
#     "Afghanistan (+93)": "+93",
#     "Albania (+355)": "+355",
#     "Algeria (+213)": "+213",
#     "Argentina (+54)": "+54",
#     "Australia (+61)": "+61",
#     "Brazil (+55)": "+55",
#     "Canada (+1)": "+1",
#     "China (+86)": "+86",
#     "France (+33)": "+33",
#     "Germany (+49)": "+49",
#     "India (+91)": "+91",
#     "Indonesia (+62)": "+62",
#     "Italy (+39)": "+39",
#     "Japan (+81)": "+81",
#     "Mexico (+52)": "+52",
#     "Pakistan (+92)": "+92",
#     "Russia (+7)": "+7",
#     "Saudi Arabia (+966)": "+966",
#     "South Africa (+27)": "+27",
#     "Spain (+34)": "+34",
#     "United Arab Emirates (+971)": "+971",
#     "United Kingdom (+44)": "+44",
#     "United States (+1)": "+1"
# }

# col1, col2 = st.columns([2, 3])
# with col1:
#     country_name = st.selectbox("🌍 Select Country", list(countries.keys()))
#     country_code = countries[country_name]
# with col2:
#     phone_number = st.text_input("📞 Enter Phone Number", placeholder="1234567890")

# # Button to Generate OTP
# if st.button("🚀 Generate OTP"):
#     if phone_number:
#         otp = generate_otp()
#         full_number = country_code + phone_number
#         with st.spinner("📨 Sending OTP... Please wait"):  # Spinner animation
#             time.sleep(5)
#         st.success(f"✅ SwiftStay OTP Send Succesfully to your phone number")
      
#     else:
#         st.error("❌ Please enter a valid phone number!")




import time
import streamlit as st
import random

# OTP Sending Function (Without SMS)
def generate_otp():
    return random.randint(100000, 999999)  # Random 6-digit OTP

# Streamlit UI
st.title("📩 SWIFTSTAY SMS OTP Generator")

# Country Code Selection
countries = {
    "Afghanistan (+93)": "+93",
    "Albania (+355)": "+355",
    "Algeria (+213)": "+213",
    "Argentina (+54)": "+54",
    "Australia (+61)": "+61",
    "Brazil (+55)": "+55",
    "Canada (+1)": "+1",
    "China (+86)": "+86",
    "France (+33)": "+33",
    "Germany (+49)": "+49",
    "India (+91)": "+91",
    "Indonesia (+62)": "+62",
    "Italy (+39)": "+39",
    "Japan (+81)": "+81",
    "Mexico (+52)": "+52",
    "Pakistan (+92)": "+92",
    "Russia (+7)": "+7",
    "Saudi Arabia (+966)": "+966",
    "South Africa (+27)": "+27",
    "Spain (+34)": "+34",
    "United Arab Emirates (+971)": "+971",
    "United Kingdom (+44)": "+44",
    "United States (+1)": "+1"
}

# Country selection dropdown
country_name = st.selectbox("🌍 Select Country", list(countries.keys()))
country_code = countries[country_name]

# Phone number input (without country code)
phone_number = st.text_input("📞 Enter Phone Number", placeholder="1234567890")

# Button to Generate OTP
if st.button("🚀 Generate OTP"):
    if phone_number.isdigit() and len(phone_number) >= 7:  # Basic validation
        otp = generate_otp()
        full_number = country_code + phone_number
        with st.spinner("📨 Sending OTP... Please wait"):  # Spinner animation
            time.sleep(5)
        st.success(f"✅ SwiftStay OTP Sent Successfully to {full_number}")
    else:
        st.error("❌ Please enter a valid phone number!")
