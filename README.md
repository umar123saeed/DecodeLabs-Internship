# 🎯 AI Job Recommendation System
### DecodeLabs Internship 2026 — Project 3

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Internship](https://img.shields.io/badge/DecodeLabs-2026-orange)

---

## 📌 Project Overview
A **Content-Based AI Recommendation System** that matches a user's skills to the most relevant job roles using **TF-IDF Vectorization** and **Cosine Similarity**. Built on a real-world Kaggle dataset of 1.6 million job postings across 376 unique roles.

---

## 🎯 Objective
- Load and explore a large-scale job descriptions dataset
- Clean and group skills by job role
- Convert skill text to numerical vectors using TF-IDF
- Recommend top-N matching job roles based on user's input skills
- Demonstrate content-based filtering using mathematical similarity

---

## 🧠 How It Works

```
User Skills Input (min. 3)
         ↓
  TF-IDF Vectorization
  (same vocabulary as dataset)
         ↓
  Cosine Similarity
  (user vector vs all 376 job role vectors)
         ↓
  Sort by Score (descending)
         ↓
  Top-N Job Recommendations
```

---

## 📁 Project Structure

```
project3-ai-recommendation-system/
│
├── recommendation.ipynb        # Main Jupyter Notebook (complete project)
├── kaggle_skills_clean.csv     # Processed dataset (generated at runtime)
└── README.md                   # Project documentation
```

> **Note:** `job_descriptions.csv` (Kaggle dataset) must be in the same folder to run the notebook.

---

## 📊 Dataset

| Property | Value |
|---|---|
| Source | Kaggle — Job Descriptions Dataset |
| Raw Size | 1,615,940 rows × 23 columns |
| After Cleaning | 376 unique job roles |
| Key Columns Used | `Role`, `skills` |

---

## ⚙️ Pipeline

| Step | Description |
|---|---|
| 1. Load Data | Import Kaggle job descriptions CSV |
| 2. Clean | Extract `Role` and `skills` columns, drop nulls |
| 3. Group | Combine all skill mentions per role into one profile |
| 4. TF-IDF | Vectorize skill profiles (376 roles × 1327 skill terms) |
| 5. User Input | Collect minimum 3 skills from user |
| 6. Similarity | Cosine Similarity: user vector vs all role vectors |
| 7. Output | Display Top-N ranked job recommendations |

---

## 🔑 Key Concepts

| Concept | Description |
|---|---|
| Content-Based Filtering | Recommends based on item attributes, not other users' behavior |
| TF-IDF | Weights skills by frequency and rarity across all roles |
| Cosine Similarity | Measures angle between vectors — ignores magnitude, focuses on direction |
| Top-N Filtering | Returns only the highest-scoring matches to prevent choice overload |

---

## 💬 Sample Output

```
==================================================
   AI JOB RECOMMENDATION SYSTEM - DecodeLabs
==================================================

Enter your skills one by one (minimum 3 required)
Type 'done' when finished

Enter skill 1: Python
  Added: Python

Enter skill 2: Machine Learning
  Added: Machine Learning

Enter skill 3: SQL
  Added: SQL

Enter skill 4: done

How many job recommendations do you want? (1-10): 5

Your Skills: ['Python', 'Machine Learning', 'SQL']
==================================================
       TOP JOB RECOMMENDATIONS FOR YOU
==================================================
 Rank                  Job Role  Match Score
    1 Machine Learning Engineer       0.6270
    2            Data Scientist       0.3520
    3     Backend Web Developer       0.1762
    4    Instructional Designer       0.1527
    5      Training Coordinator       0.1364

==================================================
Powered by DecodeLabs | AI Recommendation System
==================================================
```

---

## 🚀 How to Run

**Requirements:**
```bash
pip install pandas numpy scikit-learn
```

**Steps:**
1. Download `job_descriptions.csv` from Kaggle
2. Place it in the same folder as the notebook
3. Run the notebook:
```bash
jupyter notebook recommendation.ipynb
```

---

## 🔮 Future Improvements
- Add collaborative filtering (user-user or item-item)
- Integrate with live job APIs (LinkedIn, Indeed)
- Build a web interface using Flask or Streamlit
- Add experience level and location filters
- Use sentence transformers for semantic similarity

---

## 👤 Author
**Umar Saeed Jan**
DecodeLabs AI Internship — Batch 2026

---
*Built with ❤️ at DecodeLabs*
