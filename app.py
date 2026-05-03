import streamlit as st
import pandas as pd

# -------------------------
# LOAD DATA
# -------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("trending_tags_output.csv")
    return df

df = load_data()

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="ShareChat Trends", layout="centered")

# -------------------------
# USER PERSONALIZATION INPUT
# -------------------------
st.sidebar.title("⚙️ Personalization")

user_location = st.sidebar.selectbox(
    "Location", ["Delhi", "Mumbai", "UP", "Bihar", "Other"]
)

user_interest = st.sidebar.selectbox(
    "Interest", ["क्रिकेट", "समाचार", "मनोरंजन", "टेक", "मौसम"]
)

# -------------------------
# ML + PERSONALIZATION LOGIC
# -------------------------
def personalize_score(row):
    score = row["score"]

    category = str(row["category"]).strip()
    tag = str(row["tag"])

    # 🎯 1. PRIMARY: Category match (most reliable)
    if category == user_interest:
        score *= 3.0   # strong boost → ensures reorder

    # 🎯 2. SECONDARY: Hindi keyword match (optional boost)
    hindi_keywords = {
        "क्रिकेट": ["आईपीएल", "क्रिकेट", "मैच"],
        "समाचार": ["चुनाव", "सरकार", "खबर"],
        "मनोरंजन": ["फिल्म", "अभिनेता", "ओटीटी"],
        "टेक": ["टेक", "एआई", "स्टार्टअप"],
        "मौसम": ["बारिश", "गर्मी", "मौसम"]
    }

    if user_interest in hindi_keywords:
        if any(k in tag for k in hindi_keywords[user_interest]):
            score *= 1.5

    # 📍 3. Location boost (keep small)
    if user_location.lower() in tag.lower():
        score *= 1.2

    return score
df["personalized_score"] = df.apply(personalize_score, axis=1)
print(df[["tag", "score", "personalized_score"]].head(10))
df = df.sort_values(by="personalized_score", ascending=False)


# -------------------------
# SESSION STATE
# -------------------------
if "selected_tag" not in st.session_state:
    st.session_state.selected_tag = None

# -------------------------
# HOME PAGE
# -------------------------
if st.session_state.selected_tag is None:

    st.title("🔥 आपके लिए ट्रेंड्स")

    st.caption("Personalized based on your interests")

    # Top 5 personalized
    st.subheader("✨ Recommended")

    for _, row in df.head(5).iterrows():
        with st.container():
            st.markdown(f"""
                <div style="
                    background-color:#fff3cd;
                    padding:12px;
                    border-radius:12px;
                    margin-bottom:10px;
                ">
                    <b>{row['tag']}</b><br>
                    <span style="color:gray;">
                        {row['category']} | 🔥 {int(row['personalized_score'])}
                        🔥 {row['score']} → {int(row['personalized_score'])} #score added
                    </span>
                </div>
            """, unsafe_allow_html=True)

            if st.button(f"Open {row['tag']}", key=row['tag']):
                st.session_state.selected_tag = row['tag']
                st.rerun()

    st.divider()

    # All trends
    st.subheader("📊 All Trends")

    for _, row in df.iterrows():
        with st.container():
            st.markdown(f"""
                <div style="
                    background-color:white;
                    padding:10px;
                    border-radius:10px;
                    margin-bottom:8px;
                    box-shadow:0px 1px 4px rgba(0,0,0,0.1);
                ">
                    <b>{row['tag']}</b><br>
                    <span style="color:gray;">
                        {row['category']} | 🔥 {row['score']}
                    </span>
                </div>
            """, unsafe_allow_html=True)

            if st.button(f"View {row['tag']}", key=f"all_{row['tag']}"):
                st.session_state.selected_tag = row['tag']
                st.rerun()

# -------------------------
# DETAIL PAGE
# -------------------------
else:
    tag = st.session_state.selected_tag
    trend = df[df['tag'] == tag].iloc[0]

    if st.button("⬅ Back"):
        st.session_state.selected_tag = None
        st.rerun()

    st.title(trend["tag"])

    st.markdown(f"""
        <div style="color:gray;">
            {trend['category']} | 🔥 {trend['score']}
        </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.subheader("📌 Description")
    st.write(trend["description"])

    st.write("")

    st.subheader("📊 Source")
    st.write(trend["source"])

    # BONUS (high impact)
    st.write("")
    st.subheader("🧠 AI Summary")

    st.info(
        f"{trend['tag']} इस समय भारत में तेजी से ट्रेंड कर रहा है और यूज़र्स इसमें काफी एंगेज कर रहे हैं।"
    )
