import matplotlib.pyplot as plt


def graph_plotter(performance: dict, title):
    """Function to draw a graph of the time complexity of different sorting algorithms"""

    for key in performance:
        plt.plot(performance[key]["size"], performance[key]["time"], label=key)

    plt.title(f"Time complexity of different sorting algorithms for {title} array")
    plt.xlabel("Array size")
    plt.ylabel("Time (seconds)")
    plt.legend()
    return plt.show