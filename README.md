# Telco Customer Churn Prediction and Retention Strategy

## 📌 Project Overview

Customer churn is a major challenge in the telecommunications industry, directly impacting revenue, customer lifetime value, and long-term business growth.

This project uses machine learning to predict customer churn risk and transform those predictions into actionable retention strategies through customer segmentation, risk scoring, and business-focused decision support.

The project was developed as an end-to-end machine learning workflow covering:

- data cleaning and preprocessing <br>
- exploratory data analysis (EDA) <br>
- feature engineering <br>
- model training and evaluation <br>
- explainability analysis <br>
- customer prioritization <br>
- retention strategy simulation <br>
- dashboard deployment <br>

The final solution includes an interactive Streamlit dashboard that allows users to generate real-time churn predictions and retention recommendations.

---

## 🌐 Live Dashboard

Streamlit App: <br>
https://myrazd-telco-churn.streamlit.app/

---

## 🎯 Project Objectives

- Analyze customer behavior and identify churn-related patterns <br>
- Build and evaluate machine learning models for churn prediction <br>
- Identify the key drivers influencing customer churn <br>
- Develop customer risk scoring and prioritization frameworks <br>
- Simulate business-focused retention strategies <br>
- Deploy an interactive machine learning dashboard <br>

---

## 🚀 Dashboard Features

The deployed Streamlit dashboard allows users to:

- Input customer information <br>
- Predict customer churn probability <br>
- Generate churn risk tiers <br>
- Identify customer personas <br>
- Receive retention recommendations <br>

The dashboard was built using Streamlit and deployed through Streamlit Community Cloud.

---

## 📂 Dataset

The project uses the IBM Telco Customer Churn dataset.

Dataset source: <br>
https://shorturl.at/bMSrL

The dataset is not included in this repository due to licensing considerations.

---

## ⚙️ Project Workflow

### Phase 1: Data Preparation and Feature Engineering

- Data overview and cleaning <br>
- Exploratory data analysis (EDA) <br>
- Missing value handling <br>
- Feature selection and leakage removal <br>
- Advanced feature engineering <br>

### Phase 2: Machine Learning Modeling

- Logistic Regression <br>
- Decision Tree <br>
- Random Forest <br>
- XGBoost <br>
- LightGBM <br>
- Model comparison <br>
- Threshold tuning <br>

### Phase 3: Explainability and Business Analytics

- SHAP explainability analysis <br>
- Customer risk scoring <br>
- Customer persona analysis <br>
- Customer value segmentation <br>
- ROI simulation <br>
- Customer prioritization <br>
- Retention recommendations <br>

### Phase 4: Advanced Evaluation and Deployment

- Advanced evaluation metrics and visualizations <br>
- Hyperparameter tuning <br>
- Cross-validation <br>
- Streamlit dashboard development <br>
- Deployment preparation <br>

---

## 🤖 Models Used

- Logistic Regression <br>
- Decision Tree <br>
- Random Forest <br>
- XGBoost <br>
- LightGBM <br>

---

## 🧠 Advanced Machine Learning Techniques

The project was extended with several advanced machine learning and business analytics techniques:

- Feature engineering <br>
- Threshold tuning <br>
- Hyperparameter tuning <br>
- Cross-validation <br>
- SHAP explainability analysis <br>
- Customer risk scoring <br>
- Customer persona analysis <br>
- Customer value segmentation <br>
- ROI simulation <br>
- Retention prioritization <br>

---

## 📈 Model Evaluation Summary

Multiple machine learning models were evaluated for churn prediction performance.

Among the evaluated models, LightGBM delivered the strongest overall balance among precision, recall, and F1 Score while maintaining good generalization during cross-validation.

Threshold tuning was also applied to improve churn detection performance by balancing customer retention coverage and targeting precision.

---

## 💡 Key Insights

- Customers with shorter tenure were significantly more likely to churn. <br>
- Fiber optic customers demonstrated higher churn risk. <br>
- Electronic check payment users showed elevated churn probability. <br>
- Support-related services were associated with improved customer retention. <br>
- High-value customers with high churn probability represented the most critical retention segment. <br>
- Customer personas revealed distinct churn behaviors across customer groups. <br>
- ROI simulations suggested that targeted retention campaigns could generate substantial business value. <br>

---

## 🧠 Business Recommendations

- Prioritize retention campaigns for high-value customers with high churn risk. <br>
- Encourage customers to transition toward longer-term contracts through loyalty incentives. <br>
- Improve onboarding and engagement strategies for newer customers. <br>
- Review pricing and service quality for fiber optic customers. <br>
- Promote support-related services to improve customer retention. <br>
- Apply customer prioritization and ROI analysis before launching retention campaigns. <br>
- Use churn risk tiers to allocate retention resources more efficiently. <br>

---

## ☁️ Deployment

The final machine learning dashboard was deployed using:

- Streamlit <br>
- Streamlit Community Cloud <br>
- GitHub <br>

The deployment includes:

- serialized LightGBM model <br>
- interactive user input interface <br>
- real-time churn prediction <br>
- customer risk scoring <br>
- customer persona identification <br>
- business-focused retention recommendations <br>

---

## 🛠️ Tools and Libraries

- Python <br>
- Pandas <br>
- NumPy <br>
- Matplotlib <br>
- Seaborn <br>
- Scikit-learn <br>
- XGBoost <br>
- LightGBM <br>
- SHAP <br>
- Streamlit <br>
- Joblib <br>

---

## 🏗️ Project Architecture

```mermaid
flowchart TD
    A[IBM Telco Customer Churn Dataset] --> B[Data Cleaning & Preprocessing]
    B --> C[Feature Engineering]
    C --> D[Model Training & Comparison]
    D --> E[LightGBM Final Model]
    E --> F[Threshold Tuning]
    F --> G[Risk Scoring & Customer Personas]
    G --> H[Retention Recommendation Logic]
    H --> I[Streamlit Dashboard]
    I --> J[Deployed App on Streamlit Community Cloud]
```

---

## 📸 Dashboard Preview

### Main Dashboard

![Main Dashboard](images/dashboard_home.png)

### Prediction Results

![Prediction Results](images/prediction_results.png)

### Risk Tier and Recommendations

![Risk Tier and Recommendations](images/retention_recommendation.png)

---

## ✅ Conclusion

This project evolved beyond a standard churn prediction workflow by combining machine learning, explainability analysis, business-focused customer analytics, and interactive deployment.

In addition to predictive modeling, the project included customer segmentation, prioritization, risk scoring, retention strategy simulation, and decision-support recommendations to deliver a more practical, business-oriented solution.

Overall, the project demonstrates how machine learning can be applied not only to predict customer churn but also to support retention strategy planning and customer-focused business decision-making through an end-to-end deployed analytics workflow.
