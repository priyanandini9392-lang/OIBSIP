# Customer Segmentation Analysis

## 📌 Project Overview

This project performs Customer Segmentation Analysis using K-Means Clustering. The aim is to group customers based on their age, work experience, and family size.

## 🎯 Objectives

- Understand customer characteristics.
- Preprocess and clean the customer dataset.
- Select suitable features for clustering.
- Scale the numerical features.
- Determine the optimal number of clusters using the Elbow Method.
- Apply K-Means Clustering.
- Visualize and analyze customer segments.
- Generate useful customer segmentation insights.

## 📂 Dataset

The dataset used is **Customer Segmentation.csv**.

The dataset contains customer information such as:

- Gender
- Ever Married
- Age
- Graduated
- Profession
- Work Experience
- Spending Score
- Family Size
- Other customer attributes

The columns `ID`, `Unnamed: 0`, and `Segmentation` were not used as clustering input features.

## 🛠️ Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## 🔄 Methodology

### 1. Data Loading
The customer dataset was loaded using Pandas.

### 2. Data Preprocessing
Missing values were handled using median values for the numerical clustering features.

### 3. Feature Selection
The following numerical features were selected:

- Age
- Work Experience
- Family Size

### 4. Feature Scaling
StandardScaler was used to scale the selected features.

### 5. Elbow Method
The Elbow Method was used to identify the suitable number of clusters.

The analysis indicated that **4 clusters** were suitable.

### 6. K-Means Clustering
K-Means clustering was applied with 4 clusters.

The customers were divided into:

| Cluster | Customers |
|--------:|----------:|
| 0 | 1800 |
| 1 | 2150 |
| 2 | 1883 |
| 3 | 2986 |

### 7. Cluster Analysis

The average characteristics of the clusters were:

| Cluster | Average Age | Average Work Experience | Average Family Size |
|--------:|------------:|------------------------:|--------------------:|
| 0 | 68.93 | 0.94 | 2.10 |
| 1 | 35.51 | 1.29 | 4.84 |
| 2 | 37.37 | 8.36 | 2.42 |
| 3 | 37.84 | 0.95 | 2.11 |

## 📊 Key Insights

- Cluster 0 represents older customers with smaller families.
- Cluster 1 represents younger customers with the largest average family size.
- Cluster 2 represents customers with the highest average work experience.
- Cluster 3 represents younger customers with low work experience and smaller families.
- K-Means successfully grouped the customers into four distinct clusters based on the selected features.

## 📈 Visualizations

The project includes:

- Elbow Method plot
- Customer Segmentation scatter plot
- Average Cluster Characteristics chart

## 💡 Recommendations

- Develop different strategies for different customer groups.
- Consider family size when designing offers for Cluster 1.
- Provide suitable services for older customers in Cluster 0.
- Consider the experience profile of Cluster 2 when planning targeted services.
- Use customer segmentation to improve personalized marketing strategies.

## ✅ Conclusion

K-Means Clustering was successfully used to segment customers into four groups based on age, work experience, and family size. The analysis helps identify different customer characteristics and can support better customer targeting and decision-making.

## 📁 Project Files

- `Customer_Segmentation.ipynb` – Jupyter Notebook containing the complete analysis.
- `Customer Segmentation.csv` – Dataset used for the project.
- `README.md` – Project documentation.
