import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def plot_bins(df, col, bins=10, figsize=(10, 5)):
    """
    Plot a histogram of a column in a dataframe with a specified number of bins.
    """
    fig, ax = plt.subplots(figsize=figsize)
    sns.histplot(df, x=col, bins=bins, ax=ax)
    plt.show()
    return fig, ax