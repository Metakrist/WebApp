import streamlit as st

# Page title
st.set_page_config(page_title="My Portfolio", layout="centered")

# Header
st.title("👋 Hello, I'm Krist")
st.subheader("Python Developer | Data Analyst | Web Scraper")

# About/Bio
st.write("""
Welcome to my portfolio! I'm passionate about building Python projects and solving problems using data.
Feel free to explore my work below!
""")

# Projects Section
st.header("🛠 Projects")

projects = {
    "Automated Data Report Generator": "https://github.com/Metakrist/github-portfolio",
    "YouTube Video Categorizer": "https://github.com/yourusername/youtube-categorizer",
    "Web Scraping Tool for Game Logs": "https://github.com/yourusername/game-log-scraper"
}

for name, link in projects.items():
    st.markdown(f"- [{name}]({link})")

# Contact Section
st.header("📫 Contact Me")

st.write("You can reach me via:")
st.markdown("""
- [GitHub](https://github.com/Metakrist)
- [LinkedIn](https://www.linkedin.com/in/kristian-m-0243b6210/)
- 📧 Email: your.email@example.com
""")
