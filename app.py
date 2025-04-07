import streamlit as st
from pathlib import Path

# ----- PATH SETTINGS -----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "HP_Resume_Final.pdf"

# ----- PAGE CONFIG -----
st.set_page_config(page_title="Het Patel | Portfolio", page_icon="📊", layout="wide")

# ----- LOAD RESUME -----
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# ----- HERO SECTION -----
st.markdown("<h1 style='text-align: center;'>Het Patel</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>📍 Data Analyst | MS in Information Technology @ WPI (2023–2025)</h5>", unsafe_allow_html=True)

# Bio Section
st.markdown("""
I'm a results-driven Data Analyst with a strong background in analytics, visualization, and automation.  
My experience spans renewable energy, finance, and e-commerce — where I've driven measurable impact
through dashboards, segmentation, predictive models, and ETL pipelines.

🔹 3 internships across US & India  
🔹 Automated PDF extraction, reduced error rates by 96%  
🔹 Built dashboards saving $55K+ in operations  
🔹 Delivered insights that increased traction and engagement by 20%+

I'm passionate about using data to drive real decisions — whether it's powering sustainability, optimizing customer journeys, or informing strategic planning.
""")

# Resume Button
st.download_button(
    label="📄 Download Resume",
    data=PDFbyte,
    file_name="Het_Patel_Resume.pdf",
    mime="application/octet-stream",
)

# ----- PROJECTS -----
st.write("---")
st.subheader("📁 Projects")

project_cols = st.columns(2)

projects = {
    "🏥 Hospital Resource Optimization Dashboard": "https://github.com/Het798/hospital_resource_dashboard",
    "🌳 Urban Green Space Optimization Dashboard": "https://github.com/Het798/urban_green_space_dashboard",
    "🌍 Global Health Dashboard": "https://github.com/Het798/Global-Health-Dashboard",
    "📈 Healthcare Cost Prediction": "https://github.com/Het798/Healthcare-Cost-Prediction",
    "💳 Retail Revenue Optimization": "https://github.com/Het798/Retail-Revenue-Optimization",
    "🏠 Real Estate Price Prediction": "https://github.com/Het798/Real-Estate-Price-Prediction"
}

for i, (project, link) in enumerate(projects.items()):
    with project_cols[i % 2]:
        st.markdown(
            f"""
            <div style="background-color:#1e1e1e;padding:15px;border-radius:10px;margin-bottom:10px">
                <h5 style="color:white;margin-bottom:5px;">{project}</h5>
                <a href="{link}" target="_blank">
                    <button style="background-color:#4CAF50;border:none;color:white;padding:6px 12px;
                    text-align:center;text-decoration:none;display:inline-block;
                    font-size:13px;border-radius:5px;">View on GitHub</button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

# ----- CONTACT -----
st.write("---")
st.subheader("📬 Get In Touch")
st.markdown(
    """
    <div style="font-size: 16px;">
    📧 Email: <a href="mailto:hhpatel@wpi.edu">hhpatel@wpi.edu</a><br>
    🔗 LinkedIn: <a href="https://www.linkedin.com/in/het-patel-854812226/" target="_blank">linkedin.com/in/het-patel-854812226</a><br>
    💻 GitHub: <a href="https://github.com/Het798" target="_blank">github.com/Het798</a>
    </div>
    """,
    unsafe_allow_html=True
)
