"""Bean Street Coffee's sales at a glance: four functions for you to finish.

The docstring under each function says what it should return, with examples.
Replace each raise NotImplementedError("Not built yet.") line with your own
code. Return each answer: the tests read what comes back, not what's printed.

A sales file has one row per store per day, under the header
date,store,cups,sales (sales are in dollars). df is the usual short name for a
DataFrame, the table pandas reads a CSV file into.
"""
import matplotlib.pyplot as plt
import pandas as pd


def load_sales(path):
    """Return the sales file at path as a pandas DataFrame.

    load_sales("sales.csv") -> a DataFrame with 93 rows (31 days, 3 stores)
    and the columns date, store, cups and sales.
    """
    raise NotImplementedError("Not built yet.")


def total_by_store(df):
    """Return each store's total sales: a Series of store name -> total.

    The stores come in A-to-Z order: Campus, Downtown, Harbor.

    For tests/sample_sales.csv:
    total_by_store(df) -> Campus 920, Downtown 1610, Harbor 1940
    """
    raise NotImplementedError("Not built yet.")


def best_day(df):
    """Return the date whose sales, all three stores added together, are the highest.

    For tests/sample_sales.csv, the three days add up to 1080 (2026-10-01),
    1660 (2026-10-02) and 1730 (2026-10-03), so:
    best_day(df) -> "2026-10-03"
    """
    raise NotImplementedError("Not built yet.")


def save_chart(df, path):
    """Draw a bar chart of each store's total sales, save it to path, and return (fig, ax).

    - One bar per store, in the order total_by_store gives them, each as
      tall as that store's total.
    - The title is "Sales by Store", the x-axis label "Store" and the
      y-axis label "Sales ($)".
    - Save the chart with fig.savefig(path), then return fig and ax
      together: return fig, ax

    save_chart(df, "sales-by-store.png") -> (fig, ax), and the file
    sales-by-store.png now exists.
    """
    raise NotImplementedError("Not built yet.")
