from random import randint
from time import perf_counter
from main import insertion_sort, quick_sort, radix_sort_counting
import matplotlib.pyplot as plt
from datetime import datetime
from threading import Thread

time = {"insertion_sort": [], "quick_sort": [], "radix_sort_counting": []}
elements = []
plots = []


def clear_data():
    for key in time:
        time[key].clear()
    elements.clear()


def draw_graph(title):
    for key in time:
        plt.plot(elements, time[key], label=key)
    plt.title(f"Time complexity of different sorting algorithms for {title} array")
    plt.xlabel("Number of elements")
    plt.ylabel("Time in seconds")
    plt.legend()
    plt.savefig(f"{title}.png", dpi=300)
    clear_data()
    return plt


def plot_and_save():
    threads = []
    for plot in plots:
        threads.append(Thread(target=plot.show))
    for thread in threads:
        thread.start()


def save_results(order: str):
    with open("results.txt", "a") as file:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        file.write(f"{'#'*35}{now}{'#'*35}\n")
        for key in time:
            file.write(f"ALG={key}, SZ={elements}, ODR={order}, TIME={[round(i, 6) for i in time[key]]}\n{'-' * 70}\n")


def test_sort(sort_func, arr, order) -> None:
    print(f"Testing {sort_func.__name__} for {len(arr)} elements of order {order}")
    start = perf_counter()
    sort_func(arr)
    end = perf_counter()
    print("sorted in", end - start, "seconds")
    print("-" * 40)
    time[sort_func.__name__].append(end - start)


def call(arr, order):
    test_sort(insertion_sort, arr, order)
    test_sort(quick_sort, arr, order)
    test_sort(radix_sort_counting, arr, order)


def test_sorted():
    order = "sorted"
    for i in range(3, 21, 5):
        arr = [j for j in range(i)]
        elements.append(i)
        call(arr, order)

    for i in range(100, 501, 100):
        arr = [j for j in range(i)]
        elements.append(i)
        call(arr, order)

    for i in range(100_000, 200_001, 10_000):
        arr = [j for j in range(i)]
        elements.append(i)
        call(arr, order)


def test_sorted_reversed():
    order = "reversed"
    for i in reversed(range(3, 21, 5)):
        arr = [j for j in range(i)]
        elements.append(i)
        call(arr, order)

    for i in reversed(range(100, 501, 100)):
        arr = [j for j in range(i)]
        elements.append(i)
        call(arr, order)

    for i in reversed(range(100_000, 200_001, 10_000)):
        arr = [j for j in range(i)]
        elements.append(i)
        call(arr, order)


def test_unsorted():
    order = "unsorted"
    for i in range(3, 21, 3):
        arr = [randint(3, 21) for j in range(i)]
        elements.append(i)
        call(arr, order)

    for i in range(100, 1001, 100):
        arr = [randint(100, 501) for j in range(i)]
        elements.append(i)
        call(arr, order)

    for i in range(100_000, 200_001, 10_000):
        arr = [randint(100_000, 200_001) for j in range(i)]
        elements.append(i)
        call(arr, order)


def run(order=None, title=None):
    if order is None or title is None:
        raise Exception("Order and title must be specified")

    events = {"sorted": test_sorted, "reversed": test_sorted_reversed, "unsorted": test_unsorted}
    events[order]()
    draw_graph(title)
    save_results(order)


def main():
    run(order="sorted", title="Sorted")
    run(order="reversed", title="Reversed")
    run(order="unsorted", title="Unsorted")
    plot_and_save()


if __name__ == "__main__":
    main()
