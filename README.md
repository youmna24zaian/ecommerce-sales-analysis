# E-commerce Sales Analysis

A practical e-commerce sales data analysis project using **Python and Pandas**, focused on data cleaning, exploratory analysis, aggregation, and extracting business-oriented insights from transactional sales data.

## Project Overview

This project analyzes an e-commerce dataset containing customer, product, sales, payment, shipping, and return information.

The analysis covers the workflow from **raw data inspection and cleaning** to **revenue analysis and business insights** using Pandas.

## Dataset

* **Initial records:** 12,500
* **Records after removing duplicates:** 12,350
* **Columns:** 16
* **Duplicate rows removed:** 150

The dataset includes information such as:

* Order ID and Order Date
* Customer ID and Customer Type
* Region and State
* Product and Category
* Quantity and Unit Price
* Discount
* Sales Channel
* Payment Method
* Shipping Method
* Return Status
* Customer Rating

## Data Cleaning & Preparation

The project includes several data preparation steps:

* Loaded the dataset using `pandas.read_csv()`
* Inspected dataset structure, dimensions, and data types
* Checked for missing values
* Identified and removed duplicate records
* Standardized categorical text using `.str.strip()` and `.str.title()`
* Converted `OrderDate` to datetime
* Handled missing categorical values using `"Unknown"`
* Cleaned and converted `UnitPrice` to numeric values
* Calculated the final `Revenue` column
* Saved the cleaned dataset as a separate CSV file

### Revenue Calculation

```python
Revenue = Quantity × UnitPrice × (1 - Discount)
```

## Business Questions

The analysis explores questions such as:

* How much revenue was generated overall?
* How many orders and unique customers were recorded?
* Which products generate the most revenue?
* Which regions contribute the most revenue?
* Which customer types generate the most revenue?
* How does revenue vary across sales channels?
* How do returned and non-returned orders compare?
* How does revenue change from month to month?

## Key Results

* **Total Revenue:** $1,756,117.01
* **Total Orders:** 12,350
* **Unique Customers:** 5,115
* **Average Order Value:** $142.20

### Key Insights

* **Returning customers generated the largest share of revenue**, contributing approximately **56.1%** of total revenue. This indicates that repeat purchases represent a substantial part of the analyzed sales activity.

* **Online sales were the largest revenue-generating channel**, accounting for approximately **46.5%** of total revenue, followed by Retail Store, Marketplace, and Corporate channels.

* **The West region generated the highest revenue** among the analyzed regions, followed by the Midwest and Southeast. The regional results show that revenue contribution was distributed across multiple regions rather than concentrated in a single market.

* **Standing Desk was the highest-revenue product**, generating approximately **$309K**, followed by Smart Watch and Office Chair.

* **Returned orders represented about 8.1% of orders** in the cleaned dataset, with 1,000 returned orders compared with 11,350 non-returned orders.

* Revenue varied across the available months in the dataset, with January 2026 recording the highest monthly revenue at $38,512.10.

## Technologies & Libraries

* Python
* Pandas
* NumPy
* Jupyter Notebook

## Pandas Concepts Practiced

* `read_csv()`
* `head()`
* `shape`
* `columns`
* `info()`
* `isnull()`
* `duplicated()`
* `drop_duplicates()`
* `value_counts()`
* `groupby()`
* `agg()`
* `nunique()`
* `sort_values()`
* `to_datetime()`
* `to_period()`
* String operations
* Data type conversion
* DataFrame aggregation

## Project Structure

```text
ecommerce-sales-analysis/
│
├── README.md
├── ecommerce_sales_analysis.ipynb
└── python_data_analytics_ecommerce_raw_cleaned.csv
```

## How to Run

1. Clone the repository.
2. Open `ecommerce_sales_analysis.ipynb` in Jupyter Notebook or VS Code.
3. Make sure the required dataset is available in the appropriate directory.
4. Run the notebook cells sequentially.
5. The cleaned dataset will be exported as:

```text
python_data_analytics_ecommerce_raw_cleaned.csv
```

## Reference

This project was practiced based on the following tutorial:

**Python for Data Analysis | Real-World Beginner Project with Pandas**

https://youtu.be/mO8j0ixh-M0

## Author

**Youmna Zaian**

GitHub: https://github.com/youmna24zaian
**Youmna Zaian**

Computer & Control Engineering Graduate | Data Science & Machine Learning

[GitHub](https://github.com/youmna24zaian)

