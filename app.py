import streamlit as st
import joblib
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="FraudShield AI",
    page_icon="💳",
    layout="wide"
)

st.markdown("""
<style>

/* Main App */
.stApp{
    background-color:#0F1117;
    color:white;
}

/* Main container */
.block-container{
    padding-top:2rem;
    padding-left:3rem;
    padding-right:3rem;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#171A21;
    border-right:1px solid #2A2E39;
}

/* Premium Metric Cards */
div[data-testid="metric-container"]{
    background:#1A1D24;
    border:1px solid #333842;
    border-radius:20px;
    padding:25px;
    box-shadow:0px 8px 25px rgba(0,0,0,.40);
    transition:all .3s ease;
}

div[data-testid="metric-container"]:hover{
    transform:translateY(-6px);
    border:1px solid #FFFFFF;
    box-shadow:0px 12px 35px rgba(255,255,255,.08);
}

.stButton>button{
    width:100%;
    height:60px;
    background:linear-gradient(90deg,#FFFFFF,#D9D9D9);
    color:#111;
    font-size:18px;
    font-weight:700;
    border:none;
    border-radius:15px;
    transition:.3s;
}

.stButton>button:hover{
    transform:scale(1.02);
    box-shadow:0px 10px 30px rgba(255,255,255,.20);
}

/* Inputs */
.stNumberInput input{
    background:#20242C;
    color:white;
    border-radius:10px;
}

/* Expanders */
.streamlit-expanderHeader{
    font-size:18px;
    font-weight:600;
}

/* Headers */
h1{
    color:white;
}

h2{
    color:white;
}

h3{
    color:white;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

b1, b2, b3, b4 = st.columns(4)

with b1:
    st.success("🟢 System Online")

with b2:
    st.info("⚡ Live Detection")

with b3:
    st.warning("🛡 Secure Monitoring")

with b4:
    st.success("🤖 AI Ready")

# Load Trained Model
model = joblib.load("MODEL/credit_card_fraud_model.pkl")

st.sidebar.success("🟢 Model Loaded Successfully")

st.sidebar.markdown("---")

st.sidebar.metric("Accuracy", "99%")
st.sidebar.metric("ROC-AUC", "94.86%")
st.sidebar.metric("Algorithm", "Logistic Regression")
st.sidebar.metric("Dataset", "284,807")

st.sidebar.markdown("---")

st.sidebar.write("👩‍💻 Developer")
st.sidebar.info("Sanyogita Sharma")

# App Title
st.markdown("""
<div style="
background:linear-gradient(135deg,#1A1D24,#0F1117);
padding:35px;
border-radius:22px;
border:1px solid #2B313A;
box-shadow:0px 8px 25px rgba(0,0,0,.4);
">

<h1 style="
color:white;
font-size:54px;
margin-bottom:8px;">
💳 FraudShield AI
</h1>

<h3 style="
color:#B8BEC9;
font-weight:400;
margin-top:0;">
Real-Time Financial Transaction Intelligence Platform
</h3>

<p style="
color:#8E96A3;
font-size:18px;">
AI-powered fraud detection for secure digital payments and intelligent transaction monitoring.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div style="
    background:#1A1D24;
    padding:22px;
    border-radius:18px;
    border:1px solid #2B313A;
    text-align:center;">
        <h3 style="color:#8E96A3;">🎯 Accuracy</h3>
        <h1 style="color:white;">99%</h1>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div style="
    background:#1A1D24;
    padding:22px;
    border-radius:18px;
    border:1px solid #2B313A;
    text-align:center;">
        <h3 style="color:#8E96A3;">📈 ROC-AUC</h3>
        <h1 style="color:white;">94.86%</h1>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div style="
    background:#1A1D24;
    padding:22px;
    border-radius:18px;
    border:1px solid #2B313A;
    text-align:center;">
        <h3 style="color:#8E96A3;">🚨 Fraud Rate</h3>
        <h1 style="color:white;">0.17%</h1>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div style="
    background:#1A1D24;
    padding:22px;
    border-radius:18px;
    border:1px solid #2B313A;
    text-align:center;">
        <h3 style="color:#8E96A3;">💳 Transactions</h3>
        <h1 style="color:white;">284K+</h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="
background:#171A21;
padding:25px;
border-radius:18px;
border:1px solid #2B313A;
margin-top:25px;">

<h2 style="color:white;">
🔍 Transaction Analysis
</h2>

<p style="color:#AAB2BF;">
Enter transaction details below to evaluate fraud probability using the trained machine learning model.
</p>

</div>
""", unsafe_allow_html=True)

# Input Fields
col1, col2 = st.columns(2)

with col1:
    time = st.number_input("Time", value=0.0)

with col2:
    amount = st.number_input("Amount", value=100.0)
   
features = []

# V1 to V28 Inputs
features = []

with st.expander("⚙ Advanced Transaction Features (V1–V28)", expanded=False):

    st.caption("""
These anonymized features are generated using PCA (Principal Component Analysis)
to protect customer privacy. They are used internally by the machine learning model.
""")

    col1, col2 = st.columns(2)

    for i in range(1, 29):

        if i % 2 == 1:
            with col1:
                value = st.number_input(
                    f"V{i}",
                    value=0.0,
                    key=f"V{i}"
                )
        else:
            with col2:
                value = st.number_input(
                    f"V{i}",
                    value=0.0,
                    key=f"V{i}"
                )

        features.append(value)

# Predict Button
if st.button("🛡 Analyze Risk", use_container_width=True):

    # Prepare Input Data
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

    st.markdown("---")
    st.subheader("📊 Prediction Report")

    result1, result2 = st.columns([2, 1])

    with result1:
        st.markdown("""
<div style="
background:linear-gradient(135deg,#1A1D24,#11151C);
padding:25px;
border-radius:18px;
border:1px solid #2B313A;
box-shadow:0px 8px 25px rgba(0,0,0,.45);
">

<h2 style="color:white;">
🛡 Transaction Security Report
</h2>

<p style="color:#B8BEC9;">
Artificial Intelligence Risk Assessment
</p>

</div>
""", unsafe_allow_html=True)

    if prediction[0] == 0:

        st.markdown("""
        <div style="
        background:#16221A;
        padding:25px;
        border-radius:20px;
        border-left:8px solid #22C55E;
        ">
        <h2 style="color:#22C55E;">✅ Genuine Transaction</h2>

        <p style="color:#D8D8D8;">
        No suspicious activity detected.
        This transaction appears safe.
        </p>

        </div>
        """, unsafe_allow_html=True)

        st.balloons()

    else:

        st.markdown("""
        <div style="
        background:#2A1717;
        padding:25px;
        border-radius:20px;
        border-left:8px solid #EF4444;
        ">
        <h2 style="color:#EF4444;">🚨 Fraud Alert</h2>

        <p style="color:#D8D8D8;">
        High probability of fraudulent activity detected.
        Immediate verification is recommended.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with result2:

        st.metric("Confidence", f"{confidence}%")

        st.progress(confidence/100)

        if prediction[0] == 0:
           st.success("LOW RISK")
        else:
           st.error("HIGH RISK")

        st.markdown("---")
        st.subheader("🎯 Confidence Gauge")

        gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=confidence,
        number={'suffix': "%"},
        title={'text': "Model Confidence"},
        gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "#22C55E" if prediction[0] == 0 else "#EF4444"},
        'steps': [
            {'range': [0, 40], 'color': "#2B2B2B"},
            {'range': [40, 70], 'color': "#4B5563"},
            {'range': [70, 100], 'color': "#D1D5DB"}
        ]
    }
))

        gauge.update_layout(
        template="plotly_dark",
        height=350,
        paper_bgcolor="#0F1117",
        font=dict(color="white")
)

        st.plotly_chart(gauge, use_container_width=True)

        st.subheader("🥧 Fraud Probability Distribution")

donut = go.Figure(data=[go.Pie(
    labels=["Genuine", "Fraud"],
    values=[genuine_prob, fraud_prob],
    hole=0.70,
    marker=dict(colors=["#22C55E", "#EF4444"]),
    textinfo="label+percent"
)])

donut.update_layout(
    template="plotly_dark",
    height=420,
    paper_bgcolor="#0F1117",
    font=dict(color="white")
)

st.plotly_chart(donut, use_container_width=True)

st.markdown("---")
st.header("📂 Batch Transaction Analysis")

uploaded_file = st.file_uploader(
    "Upload a CSV file for batch fraud prediction",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.write("### Uploaded Dataset")
    st.dataframe(df.head())

    try:
        predictions = model.predict(df)

        df["Prediction"] = [
            "Genuine" if p == 0 else "Fraud"
            for p in predictions
        ]

        st.success("✅ Prediction Completed")

        st.dataframe(df.head())

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📥 Download Results",
            csv,
            "Fraud_Predictions.csv",
            "text/csv"
        )

    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")

st.markdown("""
<div style="
text-align:center;
padding:20px;
color:#9CA3AF;
">

<h3>💳 FraudShield AI</h3>

<p>
Real-Time Financial Transaction Intelligence Platform
</p>

<hr style="border:1px solid #2B313A;">

<p>
Developed by <b>Sanyogita Sharma</b>
</p>

<p>
Machine Learning • Streamlit • Logistic Regression • Plotly
</p>

</div>
""", unsafe_allow_html=True)