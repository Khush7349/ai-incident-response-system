# 🚨 AI Incident Response System

An AI-powered security monitoring system that detects, analyzes, and explains suspicious system activity in real time using machine learning, rule-based detection, and LLM-driven reasoning.

---

## 🚀 Overview

This project simulates a **modern incident response pipeline**. System logs are streamed in real time, processed through anomaly detection models and behavioral rules, scored for risk, and explained using an LLM.

The goal is to replicate how real-world security systems identify and investigate threats.

---

## 🔥 Key Features

- ⚡ Real-time log streaming  
- 🧠 ML-based anomaly detection (Isolation Forest)  
- ⚙️ Rule-based threat detection  
  - Login spike detection  
  - IP anomaly detection  
  - Privilege misuse detection  
- 📊 Hybrid risk scoring engine (ML + rules)  
- 🤖 LLM-powered incident explanations  
- 🖥️ SOC-style dashboard for monitoring and investigation  

---

## 🧠 System Architecture

```
Log Stream
↓
Preprocessing
↓
Feature Engineering
↓
ML Detection (Isolation Forest)
↓
Rule Engine
↓
Risk Scoring
↓
LLM Explanation
↓
Dashboard
```

---

## 📁 Project Structure

```
ai-incident-response/
│
├── core/ # Pipeline + state management
├── detectors/ # ML detection layer
├── rules/ # Rule-based detection
├── scoring/ # Risk engine
├── intelligence/ # LLM + formatter
├── ingestion/ # Log generation + preprocessing
├── services/ # Utilities (logger, simulator)
├── dashboard/ # Streamlit UI
│
├── data/ # Generated logs
├── models/ # Trained ML models
│
├── train.py # Model training script
├── main.py # Real-time runner
├── config.py
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository


- git clone https://github.com/your-username/ai-incident-response-system.git

- cd ai-incident-response-system


---

### 2. Create virtual environment


- python -m venv venv
- source venv/bin/activate # macOS/Linux
- venv\Scripts\activate # Windows


---

### 3. Install dependencies


pip install -r requirements.txt


---

### 4. Generate training data


python data/generate_logs.py


---

### 5. Train model


python train.py


---

### 6. Run system (CLI mode)


python main.py


---

### 7. Launch dashboard


streamlit run dashboard/app.py


---

## 🧠 How It Works

1. Logs are generated via a simulated streaming system  
2. Data is preprocessed and converted into features  
3. ML model detects anomalies  
4. Rule engine identifies suspicious behavior patterns  
5. Risk engine computes a final threat score  
6. LLM generates a human-readable explanation  
7. Dashboard displays alerts and insights  

---

## 📊 Example Output


Incident ID: log_48291
User: user_3
Action: admin_access

Risk Score: 85
Risk Level: CRITICAL

⚠️ ALERT

Multiple rapid login attempts detected
Access from unfamiliar IP address
Suspicious admin-level activity

AI Explanation:
User exhibited unusual behavior with rapid login attempts and elevated access from a new IP, indicating potential compromise.


---

## 👤 Author

**Khushi Sharma**

---

## ⭐ If you like this project

Consider starring ⭐ the repo or contributing improvements!
