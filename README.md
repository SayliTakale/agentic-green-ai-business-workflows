# Agentic AI for Sustainable Deployment of AI Models

## Overview
This project implements an **agentic AI system** that integrates with enterprise-style business workflows (CRM/ERP) to promote **Green AI** practices.  
A **LangChain-based agent** analyzes AI model usage and replaces heavy AI models with **lightweight, energy-efficient alternatives** without affecting task performance.

Workflow automation is simulated using **Zapier**, and sustainability impact is visualized using a **Streamlit dashboard**.

---

## Objectives
- Optimize AI models used in business workflows
- Reduce compute and energy consumption
- Maintain acceptable performance
- Visualize sustainability improvements

---

## System Flow
CRM/ERP Workflow → Zapier Trigger → LangChain Agent
→ Baseline / Green AI Models
→ Energy Analysis → Streamlit Dashboard

---

## Tech Stack
- **Language:** Python  
- **Agent Framework:** LangChain  
- **AI Models:** HuggingFace (lightweight models)  
- **Automation:** Zapier (simulated)  
- **Visualization:** Streamlit  
- **Infrastructure:** Terraform (dummy)

---

## Dashboard Outputs
1. **Current vs. Optimized Energy Usage**  
2. **Suggested Model Swaps**  
3. **Impact Over Time**

---

## How to Run
```bash
pip install -r requirements.txt
python main.py
streamlit run dashboard/app.py





Key Outcome: 
Reduced estimated energy usage (~40–50%)
Successful replacement of heavy models with greener alternatives
Clear visualization of sustainability impact




Author
Sayli Takale
