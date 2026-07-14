# 🕵️‍♂️ SnoopLog: Unified Threat & Fraud Detection

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.20%2B-FF4B4B)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange)

**SnoopLog** is a closed-loop Machine Learning prototype designed to solve a major blind spot in banking security: the disconnect between IT network logs (IPs, devices) and financial ledgers (transfer amounts, balances). 

By ingesting combined telemetry and utilizing an **Isolation Forest** anomaly detection algorithm, SnoopLog correlates high-risk financial transfers with suspicious network behavior to generate prioritized, human-readable alerts in a real-time dashboard.

## ✨ Core Features
* **Unsupervised Anomaly Detection:** Uses Scikit-Learn's `IsolationForest` to identify outliers in vast datasets without needing pre-labeled fraud cases.
* **Cross-Layer Correlation Engine:** Business logic that checks if a flagged financial anomaly (e.g., massive transfer) shares a timeline with a network anomaly (e.g., unrecognized IP).
* **Interactive Threat Feed:** A responsive, dark-mode-ready UI built with Streamlit for security admins to review, freeze, or dismiss alerts.

## 🛠️ Tech Stack
* **Core Logic:** Python, Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Isolation Forest)
* **Frontend Dashboard:** Streamlit

## 🚀 Quick Start Guide

### 1. Clone the repository
```bash
git clone [https://github.com/yourusername/snooplog.git](https://github.com/yourusername/snooplog.git)
cd snooplog
