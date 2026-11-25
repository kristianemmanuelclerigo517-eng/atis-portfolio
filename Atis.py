
import streamlit as st
from pathlib import Path

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Jeff Kaizah M. Atis | Portfolio",
    page_icon="🎮",
    layout="wide"
)

# FILE PATHS
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"

# CUSTOM DESIGN
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}

.stApp {
    background-color: #101311;
    color: #F2F5F0;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3, p, li, label {
    color: #F2F5F0 !important;
}

.hero {
    background: linear-gradient(120deg, #1C2820, #172019);
    border: 1px solid #344B38;
    border-radius: 22px;
    padding: 38px;
    margin-bottom: 25px;
}

.tag {
    color: #B8F36B;
    font-size: 13px;
    letter-spacing: 3px;
    font-weight: bold;
}

.hero-name {
    font-size: 48px;
    line-height: 1.1;
    font-weight: 700;
    margin-top: 12px;
}

.hero-description {
    color: #C4CEC1 !important;
    font-size: 16px;
    line-height: 1.7;
}

.section-title {
    color: #B8F36B !important;
    font-size: 25px;
    font-weight: 700;
    margin-bottom: 10px;
}

.info-card {
    background: #1A211C;
    border: 1px solid #344B38;
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 15px;
    min-height: 145px;
}

.info-card h3 {
    color: #B8F36B !important;
    margin-bottom: 8px;
}

.info-card p {
    color: #D0D8CE !important;
    line-height: 1.6;
}

.small-label {
    color: #B8F36B !important;
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: bold;
}

div[data-testid="stSidebar"] {
    background-color: #171D19;
}

div[data-testid="stSidebar"] * {
    color: #F2F5F0 !important;
}

.stButton > button {
    background-color: #B8F36B;
    color: #101311 !important;
    border: none;
    border-radius: 10px;
    font-weight: bold;
}

hr {
    border-color: #344B38;
}
</style>
""", unsafe_allow_html=True)


# IMAGE FUNCTION
def show_image(filename, caption=None, width=None):
    image_path = IMAGE_DIR / filename

    if image_path.is_file():
        if width:
            st.image(str(image_path), caption=caption, width=width)
        else:
            st.image(str(image_path), caption=caption, use_container_width=True)
    else:
        st.info(f"Add {filename} to your images folder to display it.")


# SIDEBAR
with st.sidebar:
    st.markdown("## 🎮 JKA.")
    st.caption("PERSONAL PORTFOLIO")
    st.markdown("---")

    page = st.radio(
        "EXPLORE",
        [
            "Home",
            "About Me",
            "Education",
            "My Hobbies",
            "My Perspective"
        ]
    )

    st.markdown("---")
    st.caption("JEFF KAIZAH M. ATIS")
    st.caption("© 2026")


# HOME PAGE
if page == "Home":

    left, right = st.columns([1.6, 1])

    with left:
        st.markdown("""
        <div class="hero">
            <div class="tag">WELCOME TO MY DIGITAL SPACE</div>
            <div class="hero-name">
                Jeff Kaizah<br>
                M. Atis
            </div>
            <p class="hero-description">
                A curious mind with a passion for interactive worlds
                and capturing meaningful moments through a lens.
                Every interest is another way to explore, learn,
                and express creativity.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            '<p class="small-label">PLAYER PROFILE / CREATIVE MIND</p>',
            unsafe_allow_html=True
        )

    with right:
        show_image("profile.jpg", "A little glimpse of me", 300)

    st.markdown('<div class="section-title">A LITTLE ABOUT MY WORLD</div>',
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>🎮 Gaming</h3>
            <p>
            I enjoy stepping into different virtual worlds,
            taking on challenges, and discovering new ways
            to play and improve.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>📷 Photography</h3>
            <p>
            I appreciate the beauty of ordinary moments.
            Photography allows me to preserve details,
            perspectives, and memories worth looking back on.
            </p>
        </div>
        """, unsafe_allow_html=True)


# ABOUT ME PAGE
elif page == "About Me":

    st.markdown('<div class="section-title">01 / GET TO KNOW ME</div>',
                unsafe_allow_html=True)

    st.title("Beyond the Screen and the Lens")

    st.write("""
    Hello! I am Jeff Kaizah M. Atis.

    I am someone who enjoys exploring different experiences
    and finding inspiration in the things around me. Whether
    it is through gaming or photography, I like activities
    that allow me to observe, experiment, and express myself.

    I believe that interests are more than just ways to spend
    free time. They can also help us develop patience,
    creativity, focus, and a better understanding of the world.
    """)

    st.markdown("---")

    st.markdown("### Personal Information")

    st.markdown("""
    <div class="info-card">
        <p><b>Full Name:</b> Jeff Kaizah M. Atis</p>
        <p><b>Hobbies:</b> Gaming and Photography</p>
        <p><b>Interests:</b> Digital experiences, creativity, and visual storytelling</p>
    </div>
    """, unsafe_allow_html=True)


# EDUCATION PAGE
elif page == "Education":

    st.markdown('<div class="section-title">02 / LEARNING JOURNEY</div>',
                unsafe_allow_html=True)

    st.title("Where My Journey Begins")

    st.write("""
    Education is an important part of personal growth.
    Every lesson and experience helps build knowledge,
    confidence, and skills that can be used in the future.
    """)

    show_image("engineering.jpg", "My educational journey")

    st.markdown("### Educational Attainment")

    st.markdown("""
    <div class="info-card">
        <div class="small-label">SENIOR HIGH SCHOOL</div>
        <h3>Bislig City National High School</h3>
        <p>Science, Technology, Engineering, and Mathematics (STEM) Strand</p>
    </div>

    <div class="info-card">
        <div class="small-label">COLLEGE</div>
        <h3>North Eastern Mindanao State University (NEMSU)</h3>
        <p>College Education</p>
    </div>
    """, unsafe_allow_html=True)


# HOBBIES PAGE
elif page == "My Hobbies":

    st.markdown('<div class="section-title">03 / WHAT I ENJOY</div>',
                unsafe_allow_html=True)

    st.title("Two Different Worlds. One Curious Mind.")

    st.write("""
    My hobbies give me different ways to enjoy my free time.
    One lets me explore virtual challenges, while the other
    helps me appreciate the real world around me.
    """)

    st.markdown("### 🎮 Gaming")

    show_image("hobbies.jpg", "Gaming")

    st.markdown("""
    <div class="info-card">
        <h3>More Than Just Playing</h3>
        <p>
        Gaming gives me the chance to experience different
        stories, overcome challenges, and enjoy interactive
        adventures. It is a hobby where entertainment meets
        strategy, focus, and problem-solving.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📷 Photography")

    show_image("interest.jpg", "Photography")

    st.markdown("""
    <div class="info-card">
        <h3>Finding Stories in Small Details</h3>
        <p>
        Photography helps me notice things that people might
        usually overlook. A simple view, a special moment,
        or an interesting detail can become a photograph
        worth keeping.
        </p>
    </div>
    """, unsafe_allow_html=True)


# MY PERSPECTIVE PAGE
elif page == "My Perspective":

    st.markdown('<div class="section-title">04 / PERSONAL THOUGHTS</div>',
                unsafe_allow_html=True)

    st.title("My Way of Seeing Things")

    st.write("""
    I believe that learning does not happen only inside
    a classroom. It can also happen while exploring a game,
    observing the environment, trying something unfamiliar,
    or simply paying attention to everyday experiences.
    """)

    st.markdown("""
    <div class="info-card">
        <h3>My View on Creativity</h3>
        <p>
        Creativity comes from curiosity. Sometimes, all it
        takes is a different perspective to see something
        ordinary in a completely new way.
        </p>
    </div>

    <div class="info-card">
        <h3>My View on Growth</h3>
        <p>
        Progress does not always happen all at once.
        Every small improvement, new experience, and lesson
        contributes to becoming a better version of yourself.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### THANK YOU FOR VISITING!")

    st.write("This is a small look into my interests, experiences, and personality.")


# FOOTER
st.markdown("---")
st.markdown(
    "<center style='color:#B8F36B;'>JKA. | PERSONAL PORTFOLIO © 2026</center>",
    unsafe_allow_html=True
)
