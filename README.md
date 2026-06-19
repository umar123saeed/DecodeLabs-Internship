# 🌸 Data Classification Using AI (KNN on Iris Dataset)
### DecodeLabs Internship 2026 — Project 2

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Internship](https://img.shields.io/badge/DecodeLabs-2026-orange)

---

## 📌 Project Overview
This project demonstrates **K-Nearest Neighbors (KNN)** classification on the classic **Iris Dataset**. The model classifies iris flowers into three species — Setosa, Versicolor, and Virginica — based on their sepal and petal measurements.

---

## 🎯 Objective
- Load and explore the Iris dataset
- Preprocess features using Standard Scaling
- Train a KNN classifier
- Evaluate performance using F1 Score, Confusion Matrix, and Classification Report
- Find the optimal value of K using the Elbow Method

---

## 🧠 How KNN Works

```
New Data Point
      ↓
Calculate Distance to All Training Points
      ↓
Select K Nearest Neighbors
      ↓
Majority Vote → Predicted Class
```

KNN is a **lazy learner** — it memorizes the training data and makes predictions by finding the K closest points to a new data point and taking a majority vote.

---

## 📁 Project Structure

```
project2-knn-classification/
│
├── Data_Classification_Using_AI.ipynb    # Main Jupyter Notebook
└── README.md                              # Project documentation
```

---

## 📊 Dataset: Iris

| Feature | Description |
|---|---|
| sepal length (cm) | Length of the sepal |
| sepal width (cm) | Width of the sepal |
| petal length (cm) | Length of the petal |
| petal width (cm) | Width of the petal |
| **Target** | Setosa / Versicolor / Virginica |

- **Total Samples:** 150
- **Features:** 4
- **Classes:** 3

---

## ⚙️ Pipeline

| Step | Description |
|---|---|
| 1. Load Data | Load Iris dataset from scikit-learn |
| 2. Explore | Check shape, classes, and feature values |
| 3. Scale Features | StandardScaler (mean=0, variance=1) |
| 4. Train/Test Split | 80% train, 20% test (random_state=42) |
| 5. Train KNN | KNeighborsClassifier(n_neighbors=5) |
| 6. Evaluate | F1 Score, Classification Report, Confusion Matrix |
| 7. Elbow Method | Find optimal K (K=1 to 20) |

---

## 📈 Results

```
F1 Score: 1.0000

              precision    recall  f1-score   support
      setosa       1.00      1.00      1.00        10
  versicolor       1.00      1.00      1.00         9
   virginica       1.00      1.00      1.00        11

    accuracy                           1.00        30
```

✅ **Perfect F1 Score of 1.0** achieved on the test set!

---

## 🔍 Key Concepts Used

| Concept | Description |
|---|---|
| KNN Algorithm | Distance-based classification |
| StandardScaler | Feature normalization to prevent distance bias |
| Train/Test Split | 80/20 split for unbiased evaluation |
| F1 Score | Harmonic mean of precision and recall |
| Confusion Matrix | Visual representation of predictions vs actuals |
| Elbow Method | Technique to find optimal K value |

---

## 🚀 How to Run

```bash
jupyter notebook Data_Classification_Using_AI.ipynb
```

**Requirements:**
```bash
pip install numpy pandas scikit-learn matplotlib seaborn
```

---

## 🔮 Future Improvements
- Test on other datasets (Wine, Breast Cancer, etc.)
- Compare KNN with other classifiers (SVM, Decision Tree, Random Forest)
- Implement cross-validation for more robust evaluation
- Tune hyperparameters (distance metric, weights)

---

## 👤 Author
**Umar Saeed Jan**
DecodeLabs AI Internship — Batch 2026

---
*Built with ❤️ at DecodeLabs*
