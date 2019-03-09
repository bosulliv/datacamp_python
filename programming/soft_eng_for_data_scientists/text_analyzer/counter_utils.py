# Import needed functionality
from collections import Counter
import matplotlib.pyplot as plt


def plot_counter_most_common(top_items):
    top_items_dict = dict(top_items)
    sorted_top_items = sorted(top_items_dict.items(), key=lambda kv: -kv[1])
    plt.figure()
    plt.bar(range(len(sorted_top_items)), [kv[1] for kv in sorted_top_items], align='center')
    plt.xticks(range(len(sorted_top_items)), [kv[0] for kv in sorted_top_items], rotation='vertical')
    plt.tight_layout()
    plt.show()


def plot_counter(counter, n_most_common=5):
    # Subset the `n_most_common` items from the input `counter`
    top_items = counter.most_common(n_most_common)
    # Plot `top_items`
    plot_counter_most_common(top_items)


def sum_counters(counters):
    # Sum the inputted `counters`
    return sum(counters, Counter())
