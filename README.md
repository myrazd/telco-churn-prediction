# Telco Customer Churn Prediction and Retention Strategy

## 📌 Project Overview

Customer churn is a critical challenge in the telecom industry, directly impacting revenue and customer lifetime value. This project aims to predict which customers are likely to churn using machine learning and transform those predictions into actionable retention and prioritization strategies.

Using a real-world telco dataset, this project covers the full data science workflow, including data cleaning, exploratory data analysis (EDA), feature engineering, model building, and evaluation.

Beyond prediction, the project focuses on identifying key drivers of churn and providing practical recommendations that can support customer retention strategies.

---

## 🎯 Objectives

- Analyze customer behavior and identify patterns related to churn  <br>
- Build and evaluate machine learning models to predict churn  <br>
- Identify key factors influencing customer churn  <br>
- Provide data-driven recommendations to improve customer retention

---

## 📂 Dataset

The dataset used in this project is the IBM Telco Customer Churn dataset.

You can download it from:
https://shorturl.at/bMSrL

Due to licensing considerations, the dataset is not included in this repository.

---

## ⚙️ Project Workflow

- Data overview and cleaning <br>
- Exploratory data analysis (EDA) <br>
- Data preprocessing <br>
- Feature selection and leakage removal <br>
- Model building and evaluation <br>
- Model comparison <br>
- Feature importance analysis <br>
- Customer value segmentation <br>
- ROI simulation <br>
- Customer prioritization <br>
- Business recommendations

---

## 🚀 Business-Focused Project Enhancements

To make the project more aligned with real-world business decision-making, several additional analyses were introduced beyond standard churn prediction:

- Customer value segmentation using a customer value proxy <br>
- Customer prioritization based on churn risk and estimated business value <br>
- ROI simulation for targeted retention campaigns <br>
- Recommended actions for different customer segments <br>

These enhancements help transform the project from a machine learning exercise into a practical retention decision-support framework.

---

## 🤖 Models Used

- Logistic Regression <br>
- Decision Tree <br>
- Random Forest <br>

---

## 📈 Model Evaluation Summary

Among the evaluated models, the Decision Tree model achieved the strongest recall and F1-score, making it the preferred model for identifying customers who are likely to churn.

While Logistic Regression provided a strong and interpretable baseline, the tree-based models were better at capturing more complex customer behavior patterns.

---

## 💡 Key Insights

- Customers with shorter tenure were significantly more likely to churn. <br>
- Fiber optic customers showed a higher churn tendency throughout the analysis. <br>
- Customers using electronic checks demonstrated higher churn risk. <br>
- Support-related services influenced customer retention. <br>
- High-value customers with high churn probability were identified as the most critical retention segment. <br>
- ROI simulation suggested that targeted retention campaigns may generate strong business value relative to intervention cost.

---

## 🧠 Business Recommendations

- Prioritize retention campaigns for high-value customers with high churn risk. <br>
- Encourage customers to move toward longer-term contracts through incentives and loyalty programs. <br>
- Improve onboarding and engagement for newer customers. <br>
- Review pricing and service quality for fiber optic customers. <br>
- Promote support-related services to improve customer retention. <br>
- Use lower-cost retention actions for lower-value customer segments. <br>
- Apply customer prioritization and ROI analysis before launching retention campaigns.

---

## 🛠️ Tools and Libraries

- Python <br>
- Pandas <br>
- NumPy <br>
- Matplotlib <br>
- Seaborn <br>
- Scikit-learn

---

## ✅ Conclusion

This project demonstrates an end-to-end machine learning workflow for customer churn prediction and retention strategy analysis in the telecom industry.

In addition to building predictive models, the project also incorporates customer segmentation, prioritization, and ROI simulation to support more practical business decision-making.

Overall, the project shows how machine learning can be used not only to predict churn, but also to help businesses prioritize retention efforts based on customer risk and potential value.
