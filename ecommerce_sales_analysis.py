"""E-commerce sales analysis using Pandas and Matplotlib.

Run from the repository root with:
    python ecommerce_sales_analysis.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_PATH = BASE_DIR / "python_data_analytics_ecommerce_raw.csv"
CLEANED_DATA_PATH = BASE_DIR / "python_data_analytics_ecommerce_raw_cleaned.csv"
IMAGES_DIR = BASE_DIR / "images"


def load_and_clean_data() -> pd.DataFrame:
    """Load the included dataset and apply the notebook's cleaning workflow."""
    data = pd.read_csv(RAW_DATA_PATH)
    data = data.drop_duplicates().copy()

    for column in ("Category", "CustomerType", "Region"):
        data[column] = data[column].astype("string").str.strip().str.title()

    data["UnitPrice"] = pd.to_numeric(
        data["UnitPrice"].astype(str).str.replace("$", "", regex=False),
        errors="coerce",
    )
    data["OrderDate"] = pd.to_datetime(
        data["OrderDate"], format="mixed", errors="coerce"
    )

    for column in (
        "CustomerType",
        "Region",
        "Category",
        "ShippingMethod",
        "CustomerRating",
    ):
        data[column] = data[column].fillna("Unknown")

    data["Revenue"] = (
        data["Quantity"] * data["UnitPrice"] * (1 - data["Discount"])
    ).round(2)
    data["Month"] = data["OrderDate"].dt.to_period("M")
    return data


def calculate_insights(data: pd.DataFrame) -> dict[str, object]:
    """Calculate the business summaries used by the project."""
    total_revenue = data["Revenue"].sum()
    total_orders = data["OrderID"].nunique()
    total_customers = data["CustomerID"].nunique()

    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "total_customers": total_customers,
        "average_order_value": total_revenue / total_orders,
        "product_revenue": data.groupby("Product")["Revenue"]
        .sum()
        .sort_values(ascending=False),
        "region_revenue": data.groupby("Region")["Revenue"]
        .sum()
        .sort_values(ascending=False),
        "customer_type_revenue": data.groupby("CustomerType")["Revenue"]
        .sum()
        .sort_values(ascending=False),
        "customer_type_summary": data.groupby("CustomerType")
        .agg(
            TotalRevenue=("Revenue", "sum"),
            Orders=("OrderID", "nunique"),
            AvgOrderValue=("Revenue", "mean"),
        )
        .sort_values("TotalRevenue", ascending=False),
        "channel_summary": data.groupby("SalesChannel")["Revenue"]
        .sum()
        .sort_values(ascending=False),
        "return_summary": data.groupby("Returned").agg(
            Orders=("OrderID", "nunique"),
            Revenue=("Revenue", "sum"),
        ),
        "monthly_revenue": data.dropna(subset=["Month"])
        .groupby("Month")["Revenue"]
        .sum(),
    }


def create_visualizations(insights: dict[str, object]) -> None:
    """Save the four project charts to the images directory."""
    IMAGES_DIR.mkdir(exist_ok=True)
    monthly_revenue = insights["monthly_revenue"]
    channel_summary = insights["channel_summary"]
    product_revenue = insights["product_revenue"]
    return_summary = insights["return_summary"]

    plt.figure(figsize=(10, 5))
    plt.plot(
        monthly_revenue.index.to_timestamp(),
        monthly_revenue.values,
        marker="o",
        color="#2F6B8A",
        linewidth=2,
    )
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / "monthly_revenue_trend.png", dpi=150, bbox_inches="tight")
    plt.close()

    plt.figure(figsize=(8, 5))
    channel_summary.plot(kind="bar", color="#4C956C")
    plt.title("Revenue by Sales Channel")
    plt.xlabel("Sales Channel")
    plt.ylabel("Revenue ($)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / "revenue_by_channel.png", dpi=150, bbox_inches="tight")
    plt.close()

    top_10_products = product_revenue.head(10).sort_values()
    plt.figure(figsize=(9, 6))
    top_10_products.plot(kind="barh", color="#F4A261")
    plt.title("Top 10 Products by Revenue")
    plt.xlabel("Revenue ($)")
    plt.ylabel("Product")
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / "top_10_products.png", dpi=150, bbox_inches="tight")
    plt.close()

    order_counts = return_summary["Orders"].sort_values(ascending=False)
    plt.figure(figsize=(7, 5))
    order_counts.plot(kind="bar", color=["#577590", "#E76F51"])
    plt.title("Returned vs Non-returned Orders")
    plt.xlabel("Return Status")
    plt.ylabel("Number of Orders")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(
        IMAGES_DIR / "returned_vs_non_returned.png", dpi=150, bbox_inches="tight"
    )
    plt.close()


def print_summary(insights: dict[str, object]) -> None:
    """Print the principal business metrics and summaries."""
    print(f"Total Revenue: ${insights['total_revenue']:,.2f}")
    print(f"Total Orders: {insights['total_orders']:,}")
    print(f"Total Customers: {insights['total_customers']:,}")
    print(f"Average Order Value: ${insights['average_order_value']:,.2f}\n")
    print("Revenue by product:")
    print(insights["product_revenue"].to_string())
    print("\nRevenue by region:")
    print(insights["region_revenue"].to_string())
    print("\nRevenue by customer type:")
    print(insights["customer_type_revenue"].to_string())
    print("\nCustomer type summary:")
    print(insights["customer_type_summary"].to_string())
    print("\nRevenue by sales channel:")
    print(insights["channel_summary"].to_string())
    print("\nReturned order summary:")
    print(insights["return_summary"].to_string())
    print("\nMonthly revenue:")
    print(insights["monthly_revenue"].to_string())


def main() -> None:
    """Run the complete e-commerce analysis workflow."""
    data = load_and_clean_data()
    insights = calculate_insights(data)
    data.to_csv(CLEANED_DATA_PATH, index=False)
    create_visualizations(insights)
    print_summary(insights)
    print(f"\nSaved cleaned data to {CLEANED_DATA_PATH.name}")
    print(f"Saved visualizations to {IMAGES_DIR.relative_to(BASE_DIR)}/")


if __name__ == "__main__":
    main()
