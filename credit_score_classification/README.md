# Credit Score Classification: Project Overview

Credit scores play a vital role in determining loan eligibility and interest rates. This project aims to assist financial institutions in automating creditworthiness assessment, reducing processing time, and minimizing risks.  

## Key Features  
- Built a credit score prediction tool with **96% accuracy**, streamlining loan approval processes.  
- Automated creditworthiness evaluation using machine learning.  
- Deployed a **user-friendly Streamlit web application** for real-time predictions.  

---

## Code and Resources Used  

- **Python Version:** 3.12.3  
- **Packages:** pandas, numpy, sklearn, matplotlib, seaborn, pickle, streamlit  
- **Dataset:** [Credit Score Dataset](https://github.com/theguyoliver/machine_learning/blob/main/credit_score_classification/data/credit_score.csv)  

---

## Exploratory Data Analysis (EDA)  

Key insights included:  
- Strong correlation between homeownership and credit scores.  
- Annual income was a significant predictor of creditworthiness.  

![age vs credit score](https://github.com/theguyoliver/machine_learning/blob/main/credit_score_classification/images/age_vs_credit_score.png)
![gender vs credit score](https://github.com/theguyoliver/machine_learning/blob/main/credit_score_classification/images/gender_vs_credit_score.png)
![home ownership vs credit score](https://github.com/theguyoliver/machine_learning/blob/main/credit_score_classification/images/home_ownership_vs_credit_score.png)

---

## Feature Engineering  

- Encoded categorical features for compatibility with machine learning models.  
- Applied one-hot encoding to prevent misleading hierarchies.  

---

## Modeling  

### Models Tried:  
1. **Multiple Linear Regression (Baseline):**  
   - Pros: Easy implementation.  
   - Cons: Struggled with non-linear patterns.  

2. **Support Vector Classifier (Optimized):**  
   - Pros: Handled non-linear relationships effectively.  
   - Accuracy: **96%**  

---

## Model Performance  

| Model                     | Accuracy |  
|---------------------------|----------|  
| **Support Vector Classifier (SVC)** | 96%      |  
| **Linear Regression**          | 92%      |  

---

## Deployment  

Deployed using a Streamlit web app:  
- Users input features like income, gender, marital status, and home ownership status.  
- The app predicts credit scores in real-time.  

---

## Future Work  

- Incorporate advanced models like Gradient Boosting or Neural Networks.  
- Expand feature set by including alternative data sources.  
- Implement explainable AI techniques to enhance model transparency.  
