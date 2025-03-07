import streamlit as st
from password_strength_meter import analyze_password_strength, get_strength_label

# Set page config
st.set_page_config(
    page_title="Password Strength Meter",
    page_icon="🔒",
    layout="centered"
)

# Add custom CSS
st.markdown("""
<style>
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #ff6b6b, #f7b801, #4CAF50);
    }
    .feedback-box {
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("🔒 Password Strength Meter")
st.markdown("""
Check how strong your password is! Enter your password below to get:
- Strength score
- Detailed feedback
- Visual strength indicator
""")

# Password input
password = st.text_input("Enter your password:", type="password")

if password:
    # Get password analysis
    score, feedback = analyze_password_strength(password)
    strength = get_strength_label(score)
    
    # Display score with progress bar
    st.subheader("Password Strength")
    st.progress(score/100)
    
    # Display strength label with appropriate color
    color = {
        "Weak": "red",
        "Moderate": "orange",
        "Strong": "green"
    }[strength]
    
    st.markdown(f"<h3 style='color: {color};'>Score: {score}/100 ({strength})</h3>", 
                unsafe_allow_html=True)
    
    # Display feedback
    st.subheader("Feedback")
    for item in feedback:
        if "Good" in item or "!" in item:
            st.success(item)
        else:
            st.warning(item)
    
    # Additional security tips
    if score < 100:
        st.info("""
        💡 Tips for a strong password:
        - Use at least 12 characters
        - Mix uppercase and lowercase letters
        - Include numbers and special characters
        - Avoid common words and patterns
        - Don't use personal information
        """)
else:
    st.info("Enter a password above to check its strength!") 