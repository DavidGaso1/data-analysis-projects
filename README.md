# Data Analysis Projects

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-MySQL-4479A1?logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black)
![Excel](https://img.shields.io/badge/Excel-Workbooks-217346?logo=microsoftexcel&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

A collection of end-to-end data analysis projects by **Davidson Ahuruezenma** — built with
Python, SQL, Power BI, and Excel while learning and applying data analysis.

Every project in this repository follows the same real-world workflow: **obtain data → clean it →
explore it → model or summarize it → present findings that a business can act on.**

---

## 📁 Repository Structure

| Folder | Tool | Projects inside |
| --- | --- | --- |
| `Python/` | Python (Pandas, scikit-learn, Matplotlib) | Customer Segmentation (RFM), Auto Insurance Analysis, Indian Air Quality Analysis |
| `SQL/` | MySQL | Amazon Sales Data cleaning & insight queries |
| `PowerBI/` | Microsoft Power BI | Superstore Sales interactive dashboard |
| `Excel/` | Microsoft Excel | Coffee Sales dashboard workbook |

## 🛠️ Skills Demonstrated

| Skill | Where |
| --- | --- |
| Data cleaning & preprocessing | Amazon Sales (SQL), RFM Analysis (Python) |
| Exploratory data analysis (EDA) | All Python projects |
| Customer segmentation & clustering | RFM Analysis (K-means + PCA) |
| Statistical modeling (regression, survival/hazard) | Auto Insurance Analysis |
| Geospatial analysis & mapping | Indian Air Quality Analysis |
| SQL queries for business insights | Amazon Sales Data |
| Dashboard design & data storytelling | Superstore (Power BI), Coffee Sales (Excel) |

---

## 1. Customer Segmentation — RFM Analysis <sub>(Python)</sub>

**What it does:** Segments customers by their purchase behavior using **RFM** (Recency, Frequency,
Monetary) scoring, then clusters them with K-means so marketing teams can target each group
differently.

**Pipeline:**

1. **Data preparation** — load transactions, handle missing values, fix data types.
2. **Outlier removal** — outliers skew clustering, distort means/standard deviations, and stretch
   normalized scales, so they are removed before modeling.
3. **Normalization** — brings Recency, Frequency, and Monetary values onto a common scale so each
   component carries equal weight in the clustering.
4. **RFM calculation** — Recency = days since last purchase, Frequency = number of purchases,
   Monetary = total spend.
5. **K-means clustering** — four customer segments from the normalized RFM data.
6. **Visualization** — 3D PCA plot of the clusters.

**The four segments and how to act on them:**

| Segment | Profile (R / F / M) | Recommended strategy |
| --- | --- | --- |
| **True Friends** | High / High / High | Loyalty programs, exclusive offers, personalized communication |
| **Butterflies** | High / Low / High | Limited-time promotions, remarketing, complementary product suggestions |
| **Barnacles** | High / High / Low | Upselling, product bundles, education on higher-value products, spending incentives |
| **Strangers** | Low / Low / Low | Brand awareness, engaging content, attractive entry promotions |

**Files:** `RFM_Analysis.ipynb` (full notebook), `RFM_Analysis.py` (runnable script),
`Clusters.PNG` (3D PCA cluster visualization), `requirements.txt`.

**Run it:**
```bash
pip install -r requirements.txt
jupyter notebook RFM_Analysis.ipynb     # or: python RFM_Analysis.py
```

**Dataset:** UK retailer e-commerce transactions —
[Kaggle](https://www.kaggle.com/datasets/carrie1/ecommerce-data).

---

## 2. Auto Insurance Analysis <sub>(Python)</sub>

**What it does:** Analyzes an auto insurer's operations around **customer lifetime value (CLV)**,
**churn**, and **response to new policy advertisements** — combining EDA, survival/hazard analysis,
and predictive modeling.

**Three analysis threads:**

| Thread | Approach | Business value |
| --- | --- | --- |
| **Customer Lifetime Value** | Exploratory analysis of CLV drivers + regression to predict CLV | Identify high-value segments and what makes them valuable |
| **Churn Analysis** | Hazard and survival analysis of customer attrition | Pinpoint the factors that drive customers away |
| **Ad Response** | Classification modeling of response to new-policy ads | Enable targeted, cost-efficient marketing campaigns |

**Outputs:** `AutoInsuranceAnalysis.ipynb` (full notebook), `Readme.md`, plus visual assets —
`CLV_hist.jpg`, `CLV_contribution.png`, `hazard_survival_churn_analysis.png`, `Response.png` —
and the raw data in `data/`.

---

## 3. Indian Air Quality Analysis <sub>(Python + Geospatial)</sub>

**What it does:** Analyzes pollutant levels across Indian states and cities and maps them
geographically, identifying the most polluted regions and the pollutants driving poor air quality.

**Pollutants covered:** PM2.5, NO₂, CO, PM10, SO₂, Ozone (O₃), and NH₃.

The dataset is a long-format table of station-level readings — each row records one
`pollutant_id` (PM2.5, NO2, CO, PM10, SO2, OZONE, NH3) with min/avg/max values, plus the
station's location and state.

**Key steps:**

- Load state/city pollutant readings (CSV) with geospatial reference data
  (`states_india.geojson`, `india_st.shp`).
- Aggregate per-station readings (min/avg/max) and explore pollutant distributions grouped by
  `pollutant_id`.
- Score and rank states (a top-10 most-affected states view, scored vs. not-scored).
- Map results onto India's state geometry for regional insight.

**Files:** `Indian_Air_Quality_Analysis.ipynb`, `Indian_Air_Quality_Analysis.csv`,
`Indian_States_Data.csv`, `states_india.geojson`, `india_st.shp`, `pics/`.

---

## 4. Amazon Sales Data — SQL Cleaning & Insight Queries <sub>(MySQL)</sub>

**What it does:** Shows the step-by-step SQL process used to clean raw Amazon sales records and
turn them into analysis-ready, chart-ready tables.

**Cleaning steps in `AmaSale.sql`:**

- Remove duplicate rows from the raw data.
- `ALTER TABLE` / `ALTER COLUMN` to fix data types so values sort and aggregate correctly.
- `UPDATE` statements to repair inconsistent values, including NULL handling.
- Derived time columns (`day`, `month`, `quarter`) so trends can be analyzed at any granularity.
- Aggregation queries by **category** and **product**, plus a `SUM`-based totals query.

**Files:** `AmaSale.sql` (the full script), `datasets/amazon_sales_data 2025.csv` (raw data).

---

## 5. Superstore Sales Analysis <sub>(Power BI)</sub>

**What it does:** An interactive Power BI dashboard over superstore sales data with a written
analysis report — comparing performance against targets, and slicing by category, product,
month, and state.

**Key findings (from `AnalysisWriteup.md`):**

| Category | Sales position | Profit share | Takeaway |
| --- | --- | --- | --- |
| **Technology** 💻 | Highest sales | ~51% of profit | Star category — protect and grow |
| **Furniture** 🪑 | 2nd in sales | Only ~6% profit | High volume, low margin — revisit pricing |
| **Office Supplies** 📌 | Lowest sales | ~43% profit | Efficient margin — good upsell candidate |

- **Seasonality:** notably high margin between sales and returns in **Q4** (Oct–Dec) — a strategic
  focus quarter.
- **Geography:** California and New York lead in sales; low-sales states are opportunities for
  targeted advertising.

**Files:** `SalesAnalysis.pbix` (dashboard), `SuperstoreSales.PNG` (preview),
`AnalysisWriteup.md` (full report).

**Dataset:** [Kaggle — Sales Forecasting](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting).

---

## 6. Coffee Sales Dashboard <sub>(Excel)</sub>

**What it does:** An Excel dashboard over coffee order data, letting you explore orders by
customer, product, and time period without any code.

**Files:** `coffeeOrdersData.xlsx` (order-level source data), `coffeeOrdersDashboard.xlsx`
(the dashboard workbook with charts and slicers).

---

## 📊 Datasets

| Project | Dataset | Location |
| --- | --- | --- |
| RFM Analysis | UK retailer e-commerce transactions | [Kaggle](https://www.kaggle.com/datasets/carrie1/ecommerce-data) |
| Auto Insurance | Insurance customer data | In-repo: `Python/Auto Insurance Analysis/data/` |
| Indian Air Quality | State/city pollutant measurements + geo files | In-repo: `Python/Indian_Air_Quality_Analysis/` |
| Amazon Sales | Amazon sales records (2025) | In-repo: `SQL/datasets/amazon_sales_data 2025.csv` |
| Superstore Sales | Superstore sales & returns | [Kaggle](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting) |
| Coffee Sales | Coffee order data | In-repo: `Excel/coffee-sales/` |

---

## 🚀 Getting Started

```bash
git clone https://github.com/DavidGaso1/data-analysis-projects.git
cd data-analysis-projects
```

Each project folder carries its own README or notebook with setup steps and run instructions
(`pip install -r requirements.txt` for the Python projects, MySQL for the SQL scripts, and the
`.pbix` / `.xlsx` workbooks for the dashboard projects).

## 📄 License

MIT — see [LICENSE](./LICENSE).

## 👤 Author

**Davidson Ahuruezenma** — data analyst & AI developer.
