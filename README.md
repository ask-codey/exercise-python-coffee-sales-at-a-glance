# Exercise: Coffee Sales at a Glance

Exercise code for the lesson **Exercise: Coffee Sales at a Glance** in the Python in Depth course on [ask-codey.com](https://www.ask-codey.com).

Bean Street Coffee, a small chain with three stores, has a month of sales in a CSV file and an owner with three questions: how much did each store sell, which day was the busiest, and can I see it as a chart? You'll write the four functions in `sales.py` that answer them with pandas and matplotlib, and tests call each function to check what it returns.

## What's here

- `sales.py`: the four functions, `load_sales`, `total_by_store`, `best_day` and `save_chart`. Each one stops with `NotImplementedError: Not built yet.` for now. The docstring under each says what it should return, with examples. For you to finish.
- `report.py`: prints October at a glance with your four functions and saves the chart as `sales-by-store.png`, so you can see them at work. Ready to use.
- `sales.csv`: Bean Street's sales for October 2026, one row per store per day under the header `date,store,cups,sales` (sales are in dollars). Our own made-up data. `report.py` and the tests read it.
- `tests/test_sales.py`: tests that call your functions and check what comes back. You don't need to change this file.
- `tests/sample_sales.csv`: three days of sales, small enough to add up by hand. The tests use it.
- `tests/conftest.py`: tells matplotlib to draw the tests' charts in memory only, so no window opens. Ready to use.
- `requirements.txt`: the packages this exercise needs, each at an exact version: pytest, pandas and matplotlib. Ready to use.
- `pytest.ini`: tells pytest where the tests are and where to find `sales.py`. Ready to use.
- `.gitignore`: tells Git to leave out the virtual environment, the files Python and pytest make as they run, and the chart `report.py` saves. Ready to use.

## Before you start

pandas, matplotlib and pytest go in a virtual environment: a private set of packages for this folder only. In VS Code's terminal, in this folder, run these three commands.

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

On a Mac (zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- The first command makes the virtual environment, in a folder named `.venv`.
- The second turns it on for this terminal: the prompt starts with `(.venv)` from then on.
- The third installs the packages `requirements.txt` lists into it: pytest, pandas and matplotlib (pip adds the packages they need, such as NumPy). It takes a minute or two.

*Virtual Environments and pip* explains all three. The `.venv` folder is in `.gitignore`, so Git leaves it out: these commands make it again on any computer.

If PowerShell answers that running scripts is disabled on this system, run this once, then run the second command again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Each new terminal starts with the virtual environment off. If the prompt doesn't start with `(.venv)`, run the second command again. (VS Code often turns it on for you.)

## Check your work

```bash
pytest
```

At first every test fails: that is expected, because each function stops with a `NotImplementedError` for now. Each function you finish turns its tests green. A failing test's message says what it called, what it expected and what came back, for example *best_day(sample) should return '2026-10-03', but it returned 8.* That 8 is a row number, not a date: the row with the biggest single sale.

To see your functions at work, run:

```bash
python report.py
```

Then open `sales-by-store.png` in VS Code to see your chart.

## The rules

- Keep each function's name and parameters as they are.
- Return each answer; don't print it. The tests read what your functions return.
- `save_chart` saves the chart to the path it's given and returns `fig, ax`, so the tests can read its title, labels and bars.
- Don't change the tests, `report.py` or the CSV files.

## Tips

- `pd.read_csv(path)` reads a CSV file into a DataFrame.
- `df.groupby("store")["sales"].sum()` totals the sales for each store, and gives the stores in A-to-Z order.
- A total for each day works the same way, grouped by `"date"`. `.idxmax()` then gives the label of the largest total: here, the date.
- A function can call another one. `save_chart` needs each store's total, and `total_by_store` already works them out.
- `fig, ax = plt.subplots()` starts a chart; `ax.bar(labels, heights)` draws the bars; `ax.set_title`, `ax.set_xlabel` and `ax.set_ylabel` add the words; `fig.savefig(path)` saves it.

## Hand it in

When it works, push your solution to a public repo of your own on GitHub, then paste that repo's address into **Submit your exercise** on the lesson page at [ask-codey.com](https://www.ask-codey.com). That's what completes the lesson. The lesson page shows the Git commands, step by step.
