import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="FraudShield AI",
    page_icon="🛡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LOAD MODEL ---------------- #

@st.cache_resource
def load_model():
    return joblib.load("MODEL/credit_card_fraud_model.pkl")

model = load_model()
# ---------------- CSS ---------------- #

st.markdown("""
<style>
.stApp{
background:#0D1117;
color:white;
}

.block-container{
padding-top:2rem;
padding-left:3rem;
padding-right:3rem;
}

section[data-testid="stSidebar"]{
background:#151922;
border-right:1px solid #2B313A;
}

div[data-testid="metric-container"]{

background:#181C24;

border:1px solid #2B313A;

border-radius:18px;

padding:22px;

box-shadow:0px 10px 25px rgba(0,0,0,.45);

transition:.35s;

}

div[data-testid="metric-container"]:hover{

transform:translateY(-7px);

border:1px solid white;

}

.stButton>button{

width:100%;

height:60px;

border-radius:15px;

font-size:18px;

font-weight:700;

border:none;

background:white;

color:black;

}

.stButton>button:hover{

box-shadow:0px 10px 30px rgba(255,255,255,.25);

transform:scale(1.02);

}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🛡 FraudShield AI")

st.sidebar.success("🟢 AI Engine Online")

st.sidebar.markdown("---")

st.sidebar.metric("Accuracy","99%")

st.sidebar.metric("ROC-AUC","94.86%")

st.sidebar.metric("Fraud Rate","0.17%")

st.sidebar.metric("Dataset","284,807")

st.sidebar.metric("Algorithm","Logistic Regression")

st.sidebar.markdown("---")

st.sidebar.info("""

Developer

👩‍💻 Sanyogita Sharma

AI • Machine Learning

""")

st.title("🛡 FraudShield AI")

st.subheader("Enterprise Fraud Intelligence Platform")

st.write(
    "AI-powered monitoring system for detecting suspicious financial transactions in real time."
)

st.markdown("---")

st.markdown("<br>", unsafe_allow_html=True)

a,b,c,d = st.columns(4)

with a:
    st.success("🟢 System Online")

with b:
    st.info("⚡ Live Monitoring")

with c:
    st.warning("🛡 Secure")

with d:
    st.success("🤖 AI Ready")

# ==========================================================
# TRANSACTION ANALYSIS
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="
background:#181C24;
padding:25px;
border-radius:20px;
border:1px solid #2B313A;
">

<h2 style="color:white;">
📥 Transaction Analysis
</h2>

<p style="color:#AEB6C2;">
Enter transaction details below to perform AI-powered fraud analysis.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

left,right = st.columns([1,1])

with left:

    time = st.number_input(
        "⏱ Transaction Time",
        value=0.0,
        format="%.2f"
    )

with right:

    amount = st.number_input(
        "💰 Transaction Amount ($)",
        value=100.0,
        format="%.2f"
    )

st.markdown("<br>", unsafe_allow_html=True)

features=[]

with st.expander("⚙ Advanced Transaction Features (V1 - V28)"):

    st.info("""
These are anonymized PCA features from the original credit card dataset.
They help the AI model detect fraudulent transaction patterns.
""")

    c1,c2=st.columns(2)

    for i in range(1,29):

        if i%2!=0:

            with c1:

                value=st.number_input(
                    f"V{i}",
                    value=0.0,
                    key=f"v{i}"
                )

        else:

            with c2:

                value=st.number_input(
                    f"V{i}",
                    value=0.0,
                    key=f"v{i}"
                )

        features.append(value)

st.markdown("<br>", unsafe_allow_html=True)

predict = st.button(
    "🛡 Analyze Transaction",
    use_container_width=True
)

# ==========================================================
# AI PREDICTION
# ==========================================================

if predict:

    # Prepare Input
    data = [time] + features + [amount]

    columns = [
        "Time","V1","V2","V3","V4","V5","V6","V7","V8","V9",
        "V10","V11","V12","V13","V14","V15","V16","V17",
        "V18","V19","V20","V21","V22","V23","V24","V25",
        "V26","V27","V28","Amount"
    ]

    input_data = pd.DataFrame([data], columns=columns)

    # Prediction
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    genuine_prob = round(probability[0][0] * 100, 2)
    fraud_prob = round(probability[0][1] * 100, 2)
    confidence = round(max(probability[0]) * 100, 2)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="
    background:#181C24;
    padding:22px;
    border-radius:18px;
    border:1px solid #2B313A;
    ">
    <h2 style="color:white;">🤖 AI Risk Assessment</h2>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([1,1])

    # ---------------- LEFT CARD ---------------- #

    with left:

        if prediction[0] == 0:

            st.success("🟢 Safe Transaction")

        else:

            st.error("🔴 Fraud Suspected")

        st.metric(
            "Prediction Confidence",
            f"{confidence}%"
        )

        st.progress(confidence / 100)

        st.write("### Transaction Summary")

        st.write(f"💰 Amount : ${amount}")

        st.write(f"⏱ Time : {time}")

        st.write(f"📅 {datetime.now().strftime('%d %b %Y %I:%M %p')}")

    # ---------------- RIGHT CARD ---------------- #

    with right:

        gauge = go.Figure(go.Indicator(

            mode="gauge+number",

            value=confidence,

            number={'suffix':"%"},

            title={'text':"AI Confidence"},

            gauge={

                'axis':{'range':[0,100]},

                'bar':{'color':"#4ADE80"},

                'steps':[

                    {'range':[0,40],'color':"#3B0A0A"},

                    {'range':[40,70],'color':"#6B5E00"},

                    {'range':[70,100],'color':"#0F3D2E"}

                ]

            }

        ))

        gauge.update_layout(
            paper_bgcolor="#181C24",
            font_color="white",
            height=380
        )

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

# ==========================================================
# FRAUD PROBABILITY ANALYTICS
# ==========================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="
    background:#181C24;
    padding:20px;
    border-radius:18px;
    border:1px solid #2B313A;
    ">
    <h2 style="color:white;">📊 Fraud Probability Analytics</h2>
    </div>
    """, unsafe_allow_html=True)

    chart1, chart2 = st.columns([1,1])

    # ---------------- DONUT CHART ---------------- #

    with chart1:

        fig = px.pie(

            names=["Genuine","Fraud"],

            values=[genuine_prob,fraud_prob],

            hole=.70,

            color_discrete_sequence=[
                "#22C55E",
                "#EF4444"
            ]

        )

        fig.update_layout(

            paper_bgcolor="#181C24",

            plot_bgcolor="#181C24",

            font_color="white",

            title="Prediction Probability"

        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ---------------- BAR CHART ---------------- #

    with chart2:

        bar = px.bar(

            x=["Genuine","Fraud"],

            y=[genuine_prob,fraud_prob],

            color=["Genuine","Fraud"],

            color_discrete_map={
                "Genuine":"#22C55E",
                "Fraud":"#EF4444"
            }

        )

        bar.update_layout(

            paper_bgcolor="#181C24",

            plot_bgcolor="#181C24",

            font_color="white",

            title="AI Probability Distribution",

            showlegend=False

        )

        st.plotly_chart(
            bar,
            use_container_width=True
        )
# ==========================================================
# AI SUMMARY
# ==========================================================

    st.markdown("<br>", unsafe_allow_html=True)

    s1,s2,s3,s4 = st.columns(4)

    with s1:
        st.metric("Confidence",f"{confidence}%")

    with s2:
        st.metric("Genuine",f"{genuine_prob}%")

    with s3:
        st.metric("Fraud",f"{fraud_prob}%")

    with s4:

        if prediction[0]==0:
            st.metric("Risk","LOW")

        else:
            st.metric("Risk","HIGH")

            st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("""
<div style="
text-align:center;
padding:30px;
color:#8E96A3;
">

<hr style="border:1px solid #2B313A;">

<h3 style="color:white;">
🛡 FraudShield AI
</h3>

<p>
Enterprise Fraud Intelligence Platform
</p>

<p>
Developed by <b>Sanyogita Sharma</b>
</p>

<p>
Machine Learning • Streamlit • Plotly • Logistic Regression
</p>

</div>
""", unsafe_allow_html=True)