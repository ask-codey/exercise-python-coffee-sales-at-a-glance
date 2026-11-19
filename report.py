# Prints Bean Street Coffee's October at a glance with your four functions from sales.py, and saves the chart.
# Ready to use. Run it with: python report.py
from sales import best_day, load_sales, save_chart, total_by_store

df = load_sales("sales.csv")
print("Bean Street Coffee: October 2026")
print(len(df), "rows")
print()
print("Sales by store:")
for store, total in total_by_store(df).items():
    print(f"  {store}: ${total:,}")
print()
print("Best day:", best_day(df))
save_chart(df, "sales-by-store.png")
print("Saved the chart as sales-by-store.png")
