# Tests for sales.py. Run them with: pytest (in the exercise folder, with the virtual environment active).
# Each test calls one of your functions with the file in its name and checks what it returns. sample_sales.csv, in
# this folder, is three days of made-up sales small enough to add up by hand; sales.csv is the whole of October.
# A failing test says what it called, what it expected and what came back.
# You don't need to change this file.
from pathlib import Path

import matplotlib.pyplot as plt
import pytest

from sales import best_day, load_sales, save_chart, total_by_store

SAMPLE = Path(__file__).parent / "sample_sales.csv"
OCTOBER = Path(__file__).parent.parent / "sales.csv"


def check(call, got, expected):
    """Fails with a message that says what the call returned and what it should return."""
    assert got == expected, f"{call} should return {expected!r}, but it returned {got!r}."


def as_dict(result):
    """A Series (or a dictionary) as a plain dictionary of whole numbers, so a failure message reads clearly."""
    if hasattr(result, "items"):
        return {key: int(value) for key, value in result.items()}
    return result


def chart_for(tmp_path):
    """Calls save_chart on the sample file, saving into a temporary folder; gives back the path and what it returned."""
    path = tmp_path / "chart.png"
    result = save_chart(load_sales(SAMPLE), path)
    assert isinstance(result, tuple) and len(result) == 2, (
        f"save_chart(df, path) should return fig and ax together (return fig, ax), but it returned {result!r}."
    )
    fig, ax = result
    fig.canvas.draw()
    return path, fig, ax


@pytest.fixture(autouse=True)
def close_charts():
    yield
    plt.close("all")


def test_1_load_sales_sample_has_9_rows_and_4_columns():
    df = load_sales(SAMPLE)
    check("load_sales(sample_sales.csv).shape", getattr(df, "shape", df), (9, 4))


def test_2_load_sales_sample_columns_are_date_store_cups_sales():
    df = load_sales(SAMPLE)
    check("list(load_sales(sample_sales.csv).columns)", list(getattr(df, "columns", [])),
          ["date", "store", "cups", "sales"])


def test_3_load_sales_october_has_93_rows():
    df = load_sales(OCTOBER)
    check("len(load_sales(sales.csv))", len(df) if df is not None else None, 93)


def test_4_total_by_store_sample_is_campus_920_downtown_1610_harbor_1940():
    check("total_by_store(sample)", as_dict(total_by_store(load_sales(SAMPLE))),
          {"Campus": 920, "Downtown": 1610, "Harbor": 1940})


def test_5_total_by_store_october_is_campus_28486_downtown_36562_harbor_30141():
    check("total_by_store(October)", as_dict(total_by_store(load_sales(OCTOBER))),
          {"Campus": 28486, "Downtown": 36562, "Harbor": 30141})


def test_6_total_by_store_lists_campus_downtown_harbor_in_that_order():
    check("the stores in total_by_store(sample), in order", list(as_dict(total_by_store(load_sales(SAMPLE)))),
          ["Campus", "Downtown", "Harbor"])


def test_7_best_day_sample_is_2026_10_03():
    check("best_day(sample)", best_day(load_sales(SAMPLE)), "2026-10-03")


def test_8_best_day_october_is_2026_10_02():
    check("best_day(October)", best_day(load_sales(OCTOBER)), "2026-10-02")


def test_9_save_chart_saves_the_file(tmp_path):
    path, fig, ax = chart_for(tmp_path)
    check("chart.png exists after save_chart(df, path)", path.exists(), True)


def test_10_save_chart_title_is_sales_by_store(tmp_path):
    path, fig, ax = chart_for(tmp_path)
    check("ax.get_title()", ax.get_title(), "Sales by Store")


def test_11_save_chart_axis_labels_are_store_and_sales_dollars(tmp_path):
    path, fig, ax = chart_for(tmp_path)
    check("(ax.get_xlabel(), ax.get_ylabel())", (ax.get_xlabel(), ax.get_ylabel()), ("Store", "Sales ($)"))


def test_12_save_chart_sample_bars_are_campus_downtown_harbor(tmp_path):
    path, fig, ax = chart_for(tmp_path)
    check("the bar labels along the x-axis", [label.get_text() for label in ax.get_xticklabels()],
          ["Campus", "Downtown", "Harbor"])


def test_13_save_chart_sample_bar_heights_are_920_1610_1940(tmp_path):
    path, fig, ax = chart_for(tmp_path)
    check("the bars' heights", [int(bar.get_height()) for bar in ax.patches], [920, 1610, 1940])
