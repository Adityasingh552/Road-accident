# Road-accident

This project explores the **causes**, **patterns**, and **outcomes** of road accidents in Indian million-plus cities. It uses data visualization, feature analysis, and ML-based experimentation to uncover meaningful insights that can support road safety planning and policy-making.

---

## 🎯 Objective

- Analyze the distribution of road accidents across major Indian cities
- Identify the most common causes and sub-causes of road incidents
- Understand the relationship between accident causes and their outcomes (fatal/non-fatal)
- Evaluate simple ML models to experiment with accident outcome classification

---

## 📁 Dataset Description

The dataset includes the following columns:

| Column Name           | Description                                                   |
|-----------------------|---------------------------------------------------------------|
| `million_plus_cities` | City where the accident occurred                              |
| `cause_category`      | General category of the accident cause                        |
| `cause_subcategory`   | Specific sub-type of the accident cause                       |
| `outcome_of_incident` | Final outcome (e.g., Fatal / Non-Fatal)                       |
| `count`               | Number of incidents with the above characteristics            |

---

## 📊 Key Insights

- **Delhi, Chennai, and Mumbai** had the highest number of accidents.
- **Overspeeding** and **Drunk Driving** were top accident causes.
- Fatal outcomes were more likely with causes like overspeeding and vehicle failure.
- Imbalanced classes were handled using **SMOTE** for model experiments.

---

## 🔍 Analysis Highlights

- 📈 Bar plots showing distribution of accidents across cities
- 🧱 Stacked bar charts comparing accident causes vs. outcomes
- 📊 Feature importance (Random Forest)
- ✅ Evaluation of ML classifiers (Random Forest, Logistic Regression, Decision Tree)
- 📉 Underfitting detection and SMOTE application

---

## 🛠 Tools & Libraries

- Python 3.x
- pandas
- seaborn
- matplotlib
- scikit-learn
- imbalanced-learn (for SMOTE)

---

## 📂 Project Structure

```
📦 road-accident-analysis
├── data/
│   └── Road_accident.csv
├── notebooks/
│   └── Road_Accident_Analysis.ipynb
├── road_accident_model.pkl      # Optional: ML model for experimentation
├── app.py                       # (If Streamlit app used for demo)
├── requirements.txt
└── README.md
```


---

## 📉 Machine Learning (Optional)

This project includes an **exploratory use of ML classifiers** to understand how well accident features predict fatal outcomes.

- Models tried:
  - Logistic Regression ✅ (best performance)
  - Decision Tree
  - Random Forest (underfitting detected)
- Class balancing via **SMOTE**

---

## 📚 References

- [Ministry of Road Transport and Highways (MoRTH), India](https://morth.nic.in/)
- [imbalanced-learn SMOTE documentation](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)

---

## 👤 Author

**Aditya Singh**  
B.Tech CSE (AI & ML), K.R. Mangalam University  
---

