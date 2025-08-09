import streamlit as st

# ---------- Page Config ----------
st.set_page_config(
    page_title="🏘️ Gurgaon Property Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Custom CSS ----------
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
            color: white;
        }
        .hero-title {
            font-size: 3.2rem;
            text-align: center;
            color: #F9A826;
            margin-top: 40px;
        }
        .hero-subtitle {
            font-size: 1.3rem;
            text-align: center;
            color: #DDDDDD;
            margin-bottom: 40px;
        }
        .feature-box {
            background-color: #1c1e26;
            padding: 25px;
            margin: 20px 0;
            border-radius: 10px;
            box-shadow: 0 0 8px rgba(255, 200, 0, 0.2);
        }
        .feature-title {
            font-size: 1.5rem;
            color: #F9A826;
        }
        .feature-text {
            font-size: 1.1rem;
            color: #CCCCCC;
            margin-top: 10px;
        }
        footer {
            margin-top: 40px;
            text-align: center;
            color: #888888;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Hero Section ----------
st.markdown('<div class="hero-title">🏠 Gurgaon Property Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Explore, Analyze, Predict & Discover the best apartments in Gurgaon — all in one place.</div>', unsafe_allow_html=True)

# ---------- Feature Highlights ----------
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-title">📍 Location-Based Apartment Search</div>
        <div class="feature-text">
            Quickly discover apartments within a specific radius of any landmark in Gurgaon. Plan your home around convenience and connectivity.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-box">
        <div class="feature-title">🏢 Similar Apartment Recommender</div>
        <div class="feature-text">
            Found an apartment you love? We’ll show you the most similar ones based on features, location, and amenities using ML algorithms.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-title">📈 Market Trend Analyzer</div>
        <div class="feature-text">
            Analyze price trends, locality popularity, and key metrics using interactive visualizations powered by real estate data.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-box">
        <div class="feature-title">💰 Price Predictor</div>
        <div class="feature-text">
            Estimate apartment prices using our trained ML model by entering details like area, location, amenities, and more.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("<footer>Made with ❤️ for Gurgaon Real Estate | Built using Streamlit, Python & Machine Learning</footer>", unsafe_allow_html=True)
