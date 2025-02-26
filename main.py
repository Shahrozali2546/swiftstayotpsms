import streamlit as st
import pandas as pd
from twilio.rest import Client
import random

TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""
TWILIO_PHONE = "SWIFTSTAY"


# Initialize Twilio Client
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# OTP Sending Function
def send_otp(phone_number):
    otp = random.randint(100000, 999999)  # Generate Random OTP
    message = f"Your verification OTP is {otp}. Please don't share with anyone."
    
    try:
        sms = client.messages.create(
            body=message,
            from_=TWILIO_PHONE,
            to=phone_number
        )
        return f"📲 OTP sent to {phone_number} | SID: {sms.sid}"
    except Exception as e:
        return f"❌ Error sending OTP to {phone_number}: {str(e)}"

# Streamlit UI
st.title("📩 OTP Sender")

# Country Code Selection with Country Name
countries = {
"Afghanistan (+93)": "+93",
    "Albania (+355)": "+355",
    "Algeria (+213)": "+213",
    "Andorra (+376)": "+376",
    "Angola (+244)": "+244",
    "Argentina (+54)": "+54",
    "Armenia (+374)": "+374",
    "Australia (+61)": "+61",
    "Austria (+43)": "+43",
    "Azerbaijan (+994)": "+994",
    "Bahamas (+1-242)": "+1-242",
    "Bahrain (+973)": "+973",
    "Bangladesh (+880)": "+880",
    "Barbados (+1-246)": "+1-246",
    "Belarus (+375)": "+375",
    "Belgium (+32)": "+32",
    "Belize (+501)": "+501",
    "Benin (+229)": "+229",
    "Bhutan (+975)": "+975",
    "Bolivia (+591)": "+591",
    "Bosnia and Herzegovina (+387)": "+387",
    "Botswana (+267)": "+267",
    "Brazil (+55)": "+55",
    "Brunei (+673)": "+673",
    "Bulgaria (+359)": "+359",
    "Burkina Faso (+226)": "+226",
    "Burundi (+257)": "+257",
    "Cambodia (+855)": "+855",
    "Cameroon (+237)": "+237",
    "Canada (+1)": "+1",
    "Cape Verde (+238)": "+238",
    "Central African Republic (+236)": "+236",
    "Chad (+235)": "+235",
    "Chile (+56)": "+56",
    "China (+86)": "+86",
    "Colombia (+57)": "+57",
    "Comoros (+269)": "+269",
    "Congo (+242)": "+242",
    "Costa Rica (+506)": "+506",
    "Croatia (+385)": "+385",
    "Cuba (+53)": "+53",
    "Cyprus (+357)": "+357",
    "Czech Republic (+420)": "+420",
    "Denmark (+45)": "+45",
    "Djibouti (+253)": "+253",
    "Dominican Republic (+1-809)": "+1-809",
    "Ecuador (+593)": "+593",
    "Egypt (+20)": "+20",
    "El Salvador (+503)": "+503",
    "Estonia (+372)": "+372",
    "Eswatini (+268)": "+268",
    "Ethiopia (+251)": "+251",
    "Fiji (+679)": "+679",
    "Finland (+358)": "+358",
    "France (+33)": "+33",
    "Gabon (+241)": "+241",
    "Gambia (+220)": "+220",
    "Georgia (+995)": "+995",
    "Germany (+49)": "+49",
    "Ghana (+233)": "+233",
    "Greece (+30)": "+30",
    "Guatemala (+502)": "+502",
    "Guinea (+224)": "+224",
    "Haiti (+509)": "+509",
    "Honduras (+504)": "+504",
    "Hungary (+36)": "+36",
    "Iceland (+354)": "+354",
    "India (+91)": "+91",
    "Indonesia (+62)": "+62",
    "Iran (+98)": "+98",
    "Iraq (+964)": "+964",
    "Ireland (+353)": "+353",
    "Israel (+972)": "+972",
    "Italy (+39)": "+39",
    "Jamaica (+1-876)": "+1-876",
    "Japan (+81)": "+81",
    "Jordan (+962)": "+962",
    "Kazakhstan (+7)": "+7",
    "Kenya (+254)": "+254",
    "Kuwait (+965)": "+965",
    "Kyrgyzstan (+996)": "+996",
    "Laos (+856)": "+856",
    "Latvia (+371)": "+371",
    "Lebanon (+961)": "+961",
    "Lesotho (+266)": "+266",
    "Liberia (+231)": "+231",
    "Libya (+218)": "+218",
    "Lithuania (+370)": "+370",
    "Luxembourg (+352)": "+352",
    "Madagascar (+261)": "+261",
    "Malawi (+265)": "+265",
    "Malaysia (+60)": "+60",
    "Maldives (+960)": "+960",
    "Mali (+223)": "+223",
    "Malta (+356)": "+356",
    "Mauritania (+222)": "+222",
    "Mauritius (+230)": "+230",
    "Mexico (+52)": "+52",
    "Moldova (+373)": "+373",
    "Monaco (+377)": "+377",
    "Mongolia (+976)": "+976",
    "Montenegro (+382)": "+382",
    "Morocco (+212)": "+212",
    "Mozambique (+258)": "+258",
    "Myanmar (+95)": "+95",
    "Namibia (+264)": "+264",
    "Nepal (+977)": "+977",
    "Netherlands (+31)": "+31",
    "New Zealand (+64)": "+64",
    "Nicaragua (+505)": "+505",
    "Niger (+227)": "+227",
    "Nigeria (+234)": "+234",
    "North Korea (+850)": "+850",
    "Norway (+47)": "+47",
    "Oman (+968)": "+968",
    "Pakistan (+92)": "+92",
    "Palestine (+970)": "+970",
    "Panama (+507)": "+507",
    "Papua New Guinea (+675)": "+675",
    "Paraguay (+595)": "+595",
    "Peru (+51)": "+51",
    "Philippines (+63)": "+63",
    "Poland (+48)": "+48",
    "Portugal (+351)": "+351",
    "Qatar (+974)": "+974",
    "Romania (+40)": "+40",
    "Russia (+7)": "+7",
    "Rwanda (+250)": "+250",
    "Saudi Arabia (+966)": "+966",
    "Senegal (+221)": "+221",
    "Serbia (+381)": "+381",
    "Sierra Leone (+232)": "+232",
    "Singapore (+65)": "+65",
    "Slovakia (+421)": "+421",
    "Slovenia (+386)": "+386",
    "South Africa (+27)": "+27",
    "South Korea (+82)": "+82",
    "Spain (+34)": "+34",
    "Sri Lanka (+94)": "+94",
    "Sudan (+249)": "+249",
    "Sweden (+46)": "+46",
    "Switzerland (+41)": "+41",
    "Syria (+963)": "+963",
    "Tajikistan (+992)": "+992",
    "Tanzania (+255)": "+255",
    "Thailand (+66)": "+66",
    "Tunisia (+216)": "+216",
    "Turkey (+90)": "+90",
    "Turkmenistan (+993)": "+993",
    "Uganda (+256)": "+256",
    "Ukraine (+380)": "+380",
    "United Arab Emirates (+971)": "+971",
    "United Kingdom (+44)": "+44",
    "United States (+1)": "+1",
    "Uruguay (+598)": "+598",
    "Uzbekistan (+998)": "+998",
    "Vatican City (+379)": "+379",
    "Venezuela (+58)": "+58",
    "Vietnam (+84)": "+84",
    "Yemen (+967)": "+967",
    "Zambia (+260)": "+260",
    "Zimbabwe (+263)": "+263"
}

# Combined Input for Country Code and Phone Number
col1, col2 = st.columns([2, 3])
with col1:
    country_name = st.selectbox("🌍 Select Country", list(countries.keys()))
    country_code = countries[country_name]
with col2:
    phone_number = st.text_input("📞 Enter Phone Number", placeholder="1234567890")

# Button to Send OTP
if st.button("🚀 Send OTP"):
    if phone_number:
        full_number = country_code + phone_number
        with st.spinner("Sending OTP... Please wait"):
            response = send_otp(full_number)
        st.write(response)
    else:
        st.error("❌ Please enter a valid phone number!")








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
# "Afghanistan (+93)": "+93",
#     "Albania (+355)": "+355",
#     "Algeria (+213)": "+213",
#     "Andorra (+376)": "+376",
#     "Angola (+244)": "+244",
#     "Argentina (+54)": "+54",
#     "Armenia (+374)": "+374",
#     "Australia (+61)": "+61",
#     "Austria (+43)": "+43",
#     "Azerbaijan (+994)": "+994",
#     "Bahamas (+1-242)": "+1-242",
#     "Bahrain (+973)": "+973",
#     "Bangladesh (+880)": "+880",
#     "Barbados (+1-246)": "+1-246",
#     "Belarus (+375)": "+375",
#     "Belgium (+32)": "+32",
#     "Belize (+501)": "+501",
#     "Benin (+229)": "+229",
#     "Bhutan (+975)": "+975",
#     "Bolivia (+591)": "+591",
#     "Bosnia and Herzegovina (+387)": "+387",
#     "Botswana (+267)": "+267",
#     "Brazil (+55)": "+55",
#     "Brunei (+673)": "+673",
#     "Bulgaria (+359)": "+359",
#     "Burkina Faso (+226)": "+226",
#     "Burundi (+257)": "+257",
#     "Cambodia (+855)": "+855",
#     "Cameroon (+237)": "+237",
#     "Canada (+1)": "+1",
#     "Cape Verde (+238)": "+238",
#     "Central African Republic (+236)": "+236",
#     "Chad (+235)": "+235",
#     "Chile (+56)": "+56",
#     "China (+86)": "+86",
#     "Colombia (+57)": "+57",
#     "Comoros (+269)": "+269",
#     "Congo (+242)": "+242",
#     "Costa Rica (+506)": "+506",
#     "Croatia (+385)": "+385",
#     "Cuba (+53)": "+53",
#     "Cyprus (+357)": "+357",
#     "Czech Republic (+420)": "+420",
#     "Denmark (+45)": "+45",
#     "Djibouti (+253)": "+253",
#     "Dominican Republic (+1-809)": "+1-809",
#     "Ecuador (+593)": "+593",
#     "Egypt (+20)": "+20",
#     "El Salvador (+503)": "+503",
#     "Estonia (+372)": "+372",
#     "Eswatini (+268)": "+268",
#     "Ethiopia (+251)": "+251",
#     "Fiji (+679)": "+679",
#     "Finland (+358)": "+358",
#     "France (+33)": "+33",
#     "Gabon (+241)": "+241",
#     "Gambia (+220)": "+220",
#     "Georgia (+995)": "+995",
#     "Germany (+49)": "+49",
#     "Ghana (+233)": "+233",
#     "Greece (+30)": "+30",
#     "Guatemala (+502)": "+502",
#     "Guinea (+224)": "+224",
#     "Haiti (+509)": "+509",
#     "Honduras (+504)": "+504",
#     "Hungary (+36)": "+36",
#     "Iceland (+354)": "+354",
#     "India (+91)": "+91",
#     "Indonesia (+62)": "+62",
#     "Iran (+98)": "+98",
#     "Iraq (+964)": "+964",
#     "Ireland (+353)": "+353",
#     "Israel (+972)": "+972",
#     "Italy (+39)": "+39",
#     "Jamaica (+1-876)": "+1-876",
#     "Japan (+81)": "+81",
#     "Jordan (+962)": "+962",
#     "Kazakhstan (+7)": "+7",
#     "Kenya (+254)": "+254",
#     "Kuwait (+965)": "+965",
#     "Kyrgyzstan (+996)": "+996",
#     "Laos (+856)": "+856",
#     "Latvia (+371)": "+371",
#     "Lebanon (+961)": "+961",
#     "Lesotho (+266)": "+266",
#     "Liberia (+231)": "+231",
#     "Libya (+218)": "+218",
#     "Lithuania (+370)": "+370",
#     "Luxembourg (+352)": "+352",
#     "Madagascar (+261)": "+261",
#     "Malawi (+265)": "+265",
#     "Malaysia (+60)": "+60",
#     "Maldives (+960)": "+960",
#     "Mali (+223)": "+223",
#     "Malta (+356)": "+356",
#     "Mauritania (+222)": "+222",
#     "Mauritius (+230)": "+230",
#     "Mexico (+52)": "+52",
#     "Moldova (+373)": "+373",
#     "Monaco (+377)": "+377",
#     "Mongolia (+976)": "+976",
#     "Montenegro (+382)": "+382",
#     "Morocco (+212)": "+212",
#     "Mozambique (+258)": "+258",
#     "Myanmar (+95)": "+95",
#     "Namibia (+264)": "+264",
#     "Nepal (+977)": "+977",
#     "Netherlands (+31)": "+31",
#     "New Zealand (+64)": "+64",
#     "Nicaragua (+505)": "+505",
#     "Niger (+227)": "+227",
#     "Nigeria (+234)": "+234",
#     "North Korea (+850)": "+850",
#     "Norway (+47)": "+47",
#     "Oman (+968)": "+968",
#     "Pakistan (+92)": "+92",
#     "Palestine (+970)": "+970",
#     "Panama (+507)": "+507",
#     "Papua New Guinea (+675)": "+675",
#     "Paraguay (+595)": "+595",
#     "Peru (+51)": "+51",
#     "Philippines (+63)": "+63",
#     "Poland (+48)": "+48",
#     "Portugal (+351)": "+351",
#     "Qatar (+974)": "+974",
#     "Romania (+40)": "+40",
#     "Russia (+7)": "+7",
#     "Rwanda (+250)": "+250",
#     "Saudi Arabia (+966)": "+966",
#     "Senegal (+221)": "+221",
#     "Serbia (+381)": "+381",
#     "Sierra Leone (+232)": "+232",
#     "Singapore (+65)": "+65",
#     "Slovakia (+421)": "+421",
#     "Slovenia (+386)": "+386",
#     "South Africa (+27)": "+27",
#     "South Korea (+82)": "+82",
#     "Spain (+34)": "+34",
#     "Sri Lanka (+94)": "+94",
#     "Sudan (+249)": "+249",
#     "Sweden (+46)": "+46",
#     "Switzerland (+41)": "+41",
#     "Syria (+963)": "+963",
#     "Tajikistan (+992)": "+992",
#     "Tanzania (+255)": "+255",
#     "Thailand (+66)": "+66",
#     "Tunisia (+216)": "+216",
#     "Turkey (+90)": "+90",
#     "Turkmenistan (+993)": "+993",
#     "Uganda (+256)": "+256",
#     "Ukraine (+380)": "+380",
#     "United Arab Emirates (+971)": "+971",
#     "United Kingdom (+44)": "+44",
#     "United States (+1)": "+1",
#     "Uruguay (+598)": "+598",
#     "Uzbekistan (+998)": "+998",
#     "Vatican City (+379)": "+379",
#     "Venezuela (+58)": "+58",
#     "Vietnam (+84)": "+84",
#     "Yemen (+967)": "+967",
#     "Zambia (+260)": "+260",
#     "Zimbabwe (+263)": "+263"
# }

# # Country and Phone Input in One Row
# col1, col2 = st.columns([1.5, 2.5])
# with col1:
#     country_name = st.selectbox("🌍 Country", list(countries.keys()))
#     country_code = countries[country_name]

# with col2:
#     phone_number = st.text_input("📞 Phone Number", placeholder="1234567890")

# # Button to Generate OTP
# if st.button("🚀 Generate OTP"):
#     if phone_number.isdigit() and len(phone_number) >= 7:  # Basic validation
#         otp = generate_otp()
#         full_number = country_code + phone_number
#         with st.spinner("📨 Sending OTP... Please wait"):  # Spinner animation
#             time.sleep(5)
#         st.success(f"✅ SwiftStay OTP Sent Successfully to {full_number}")
#     else:
#         st.error("❌ Please enter a valid phone number!")
