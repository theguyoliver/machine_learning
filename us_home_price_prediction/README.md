# US Home Price Prediction: Project Overview

Accurately predicting home prices is essential for real estate professionals and financial institutions. This project leverages machine learning to create a robust tool for forecasting home prices in the United States, ensuring better decision-making and improved resource allocation.

## Key Features
- Built a predictive model for **US Home Prices**, achieving an **R² of 71% on test data**.
- Automated the prediction process using machine learning.
- Deployed a **user-friendly Flask web application** for real-time predictions hosted on **AWS EC2**.

---

## Code and Resources Used

- **Python Version:** 3.10
- **Packages:** pandas, numpy, sklearn, matplotlib, seaborn, flask
- **Dataset:** [US Home Price Dataset](https://github.com/theguyoliver/machine_learning/blob/main/us_home_price_prediction/data/data.csv)

---

## Exploratory Data Analysis (EDA)

Key insights included:
- Strong influence of location (city) and features like square footage on home prices.
- Detected and handled outliers using both **business logic** and **statistical methods**.

---

## Feature Engineering

- **One-hot Encoding:** Applied to encode city names for model compatibility.
- **Dimensionality Reduction:** Reduced the dataset to key features.
- **Outlier Removal:** 
  - Business logic (e.g., removing extreme luxury properties).
  - Statistical methods (e.g., removing values outside 3 standard deviations).

---

## Modeling

### Models Tried:
1. **Linear Regression (Selected):**  
   - Pros: Simple, interpretable, good performance.  
   - R²: **67% on training data, 71% on test data**.

2. **Lasso Regression:**  
   - Pros: Regularization helped reduce overfitting.  
   - Accuracy: **66%**.  

3. **Random Forest Regressor:**  
   - Pros: Captured non-linear relationships.  
   - Accuracy: **61%**.  

---

## Model Performance

| Model                     | Accuracy (Cross-Validation) |  
|---------------------------|-----------------------------|  
| **Linear Regression**     | 66%                        |  
| **Lasso Regression**      | 66%                        |  
| **Random Forest Regressor** | 61%                        |  

---

## Deployment

Deployed using a **Flask web application**:
- Users input features like city, square footage, and other property details.
- The app predicts home prices in real-time.

Hosted on **AWS EC2**, ensuring high availability and scalability.

---

## Future Work

- Incorporate dynamic, real-time data updates from online housing platforms.
- Explore advanced models like Gradient Boosting or Neural Networks.
- Develop an interactive dashboard for visualizing predictions and trends.