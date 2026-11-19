# Runs before the tests. It tells matplotlib to draw charts in memory only (the "Agg" backend), so the tests never
# open a window. The tests read each chart's title, labels and bars from the Axes your function returns.
# You don't need to change this file.
import matplotlib

matplotlib.use("Agg")
