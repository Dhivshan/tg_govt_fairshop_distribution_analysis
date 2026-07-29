# Telangana Govt Ration Distribution Analysis

## 📊 Project Overview
This project analyzes ration distribution patterns across districts in Telangana using clustering techniques.  
The goal is to identify shop personas, evaluate cluster quality, and provide interactive insights via a Streamlit dashboard.

---

## 📂 Dataset
The main dataset `unified_master.csv` is too large to store directly in GitHub.  
It is hosted on Google Drive due to file size limits.

[Download here](https://drive.google.com/file/d/1gw5f9Tzpu1EcwS33Njnl7EvgWzA8ikjE/view?usp=drive_link)

Place the file inside the `data/` folder before running notebooks or the dashboard.

---

## ⚙️ Methodology
- **Feature Engineering**: Utilization ratio, rice/wheat ratio, transaction volatility, lag transactions, rolling mean (3 months), and policy flags.
- **Clustering**: MiniBatchKMeans with Incremental PCA for dimensionality reduction.
- **Evaluation Metrics**:
  - Silhouette Score & Elbow Curve → validate optimal number of clusters.
  - Cluster Purity → check alignment with Urban vs Rural districts.
  - Davies–Bouldin & Calinski–Harabasz Scores → additional cluster quality checks.

---

## 📈 Dashboard
The Streamlit app (`app.py`) provides:
- Interactive filters for district and year.
- Map visualization of ration shops by cluster.
- Shop search tool with cluster comparison.
- Cluster profile charts for quick insights.

Run locally:
```bash
streamlit run app.py
