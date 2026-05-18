# E-commerce Return Rate Reduction Analysis

## Project Objective
This project analyzes customer return behavior in an e-commerce business to identify why products are returned and how return rates vary by category, geography, supplier, and marketing channel.

The project also uses Logistic Regression to predict the probability of product returns and builds an interactive Power BI dashboard for return risk analysis.

## Tools Used
- SQL
- Python (Pandas, Scikit-learn, Matplotlib)
- Power BI
- GitHub

## Dataset
The dataset contains order and return information including:

- Order ID
- Customer ID
- Product Category
- Supplier
- Region / Geography
- Marketing Channel
- Price
- Quantity
- Delivery Days
- Return Status

## Project Workflow

### 1. Data Cleaning
- Removed missing values
- Cleaned order and return data
- Prepared dataset for analysis

### 2. SQL Analysis
Performed analysis to identify:

- Return percentage by category
- Return percentage by supplier
- Return trend by geography
- Marketing channel return analysis

### 3. Python Analysis
Used Python for:

- Data preprocessing
- Feature encoding
- Logistic Regression model building
- Return prediction analysis
- Accuracy evaluation

### 4. Power BI Dashboard
Created an interactive dashboard including:

- Return % by Category
- Supplier Return Analysis
- Region-wise Returns
- Marketing Channel Performance
- Return Risk Score
- Monthly Return Trend

## Project Structure
Ecommerce_Return_Analysis/
dataset/
* orders.csv
  ** returns.csv

* sql
  ** ecommers.sql.sql

* python
  **project.py

* powerbi
  **data.png

* README.md


## Key Insights
- Identified categories with high return rates
- Found suppliers contributing to more returns
- Analyzed regional return patterns
- Evaluated marketing channels with high return risk
- Predicted customer return probability using Logistic Regression

## Deliverables
- SQL Queries
- Python Prediction Model
- Power BI Interactive Dashboard
- Project Documentation
- GitHub Repository

## Conclusion
This project helps understand customer return behavior and provides data-driven insights to reduce return rates and improve business performance.
