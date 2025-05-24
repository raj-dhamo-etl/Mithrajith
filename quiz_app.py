
import streamlit as st

# App Title and Introduction
st.set_page_config(page_title="10 Years of You Quiz", layout="centered")
st.title("🎉 10 Years of You 🎉")
st.subheader("Test your memory and see how well you remember your amazing journey!")

# Quiz Questions
quiz_data = [
    {
        "question": "What is your favorite cartoon show?",
        "options": ["Pokemon", "Avengers", "Tom & Jerry", "Ben 10"],
        "answer": "Tom & Jerry"
    },
    {
        "question": "Where did we go for vacation in 2022?",
        "options": ["Goa", "Singapore", "Shimla", "Dubai"],
        "answer": "Singapore"
    },
    {
        "question": "What's your favorite food?",
        "options": ["Pizza", "Biryani", "Pasta", "Dosa"],
        "answer": "Pizza"
    },
    {
        "question": "What's the name of your school?",
        "options": ["Sunshine Academy", "Happy Valley School", "Greenwood High", "Oakridge"],
        "answer": "Greenwood High"
    },
    {
        "question": "Which toy did you love most as a baby?",
        "options": ["Teddy", "Car", "Train", "Doll"],
        "answer": "Teddy"
    },
    {
        "question": "What is your favorite color?",
        "options": ["Red", "Blue", "Green", "Yellow"],
        "answer": "Blue"
    },
    {
        "question": "What do you want to be when you grow up?",
        "options": ["Scientist", "Cricketer", "Artist", "Engineer"],
        "answer": "Scientist"
    },
    {
        "question": "What game do you love most?",
        "options": ["Minecraft", "FIFA", "Roblox", "Ludo"],
        "answer": "Minecraft"
    },
    {
        "question": "Who is your best friend?",
        "options": ["Aarav", "Kavin", "Neha", "Sara"],
        "answer": "Kavin"
    },
    {
        "question": "What was your first word as a baby?",
        "options": ["Mama", "Papa", "Ball", "Car"],
        "answer": "Papa"
    }
]

score = 0

for q in quiz_data:
    st.write(f"**{q['question']}**")
    choice = st.radio("Choose one:", q["options"], key=q['question'])
    if choice == q["answer"]:
        score += 1
        st.success("🎉 Correct!")
    else:
        st.error("Oops! Not quite right.")

st.markdown("---")
st.markdown(f"### 🏆 Final Score: {score} / {len(quiz_data)}")

if score == len(quiz_data):
    st.balloons()
    st.success("You're a Memory Master! 🧠✨")
elif score >= 7:
    st.success("Great Job! You're amazing!")
else:
    st.info("Keep practicing! You’re doing awesome!")


from fpdf import FPDF
import base64

def create_certificate(name, score):
    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("Arial", 'B', 28)
    pdf.set_text_color(0, 102, 204)
    pdf.cell(0, 40, "🎉 10 Years of You - Certificate 🎉", ln=True, align='C')

    pdf.set_font("Arial", '', 20)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 20, f"This certificate is awarded to", ln=True, align='C')
    pdf.set_font("Arial", 'B', 24)
    pdf.cell(0, 20, f"{name}", ln=True, align='C')
    pdf.set_font("Arial", '', 18)
    pdf.cell(0, 20, f"For scoring {score} out of 10 in the Memory Quiz", ln=True, align='C')

    pdf.output("certificate.pdf")

    with open("certificate.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    return base64_pdf

# Name input and download button
st.markdown("---")
name = st.text_input("Enter your name for the certificate:")
if st.button("🎓 Generate My Certificate"):
    if name.strip() != "":
        pdf_data = create_certificate(name, score)
        href = f'<a href="data:application/pdf;base64,{pdf_data}" download="10YearCertificate.pdf">📄 Click here to download your certificate</a>'
        st.markdown(href, unsafe_allow_html=True)
    else:
        st.warning("Please enter your name to generate the certificate.")
