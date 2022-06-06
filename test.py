from time import perf_counter
from datetime import datetime
import json

# Local imports
from generator import array_generator
from main import insertion_sort, quick_sort, bubble_sort, radix_sort_counting
from graph import graph_plotter

performance: dict = {
    insertion_sort.__name__: [],
    quick_sort.__name__: [],
    bubble_sort.__name__: [],
    radix_sort_counting.__name__: [],
}


def array_size(SIZE: str) -> array_generator:
    """INDEX FOR ARRAY SIZES:
        S_MIN = 3
        S_MAX = 21
        S_STEP = 3

        M_MIN = 100
        M_MAX = 1001
        M_STEP = 100

        L_MIN = 100_000
        L_MAX = 200_001
        L_STEP = 10_000
    """

    S_MIN = 3
    S_MAX = 21
    S_STEP = 1

    M_MIN = 100
    M_MAX = 1001
    M_STEP = 1

    L_MIN = 100_000
    L_MAX = 200_001
    L_STEP = 1

    if SIZE.upper() == "S":
        small = array_generator(S_MIN, S_MAX, S_STEP)
        return small
    if SIZE.upper() == "M":
        medium = array_generator(M_MIN, M_MAX, M_STEP)
        return medium
    if SIZE.upper() == "L":
        large = array_generator(L_MIN, L_MAX, L_STEP)
        return large


def test_sort(sort_func, arr: list, order: str) -> bool:
    """Function to test the time complexity of different sorting algorithms with different arrays"""
    s = len(arr)
    print(f"Testing {sort_func.__name__} for {s} elements of order {order}")

    # Start timer
    start = perf_counter()

    # Sort array
    sort_func(arr)

    # Stop timer
    end = perf_counter()

    # Calculate time
    print("sorted in", end - start, "seconds")
    print("-" * 40)
    t = {
        order: {
            "time": round(end - start, 6),
            "size": s}
    }
    performance[sort_func.__name__].append(t)

    return True


def main():
    """HELP :
    - order : "sorted", "reversed", "unsorted"
    """
    array_type = {
        "sorted": {"small": array_size("S").sorted(),
                   "medium": array_size("M").sorted(),
                   "large": array_size("L").sorted()},

        "reversed": {"small": array_size("S").reversed(),
                     "medium": array_size("M").reversed(),
                     "large": array_size("L").reversed()},

        "unsorted": {"small": array_size("S").unsorted(),
                     "medium": array_size("M").unsorted(),
                     "large": array_size("L").unsorted()}
    }
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    performance['info'] = now
    for order in array_type:
        for size in array_type[order]:

            test_sort(insertion_sort, array_type[order][size], order)
            test_sort(quick_sort, array_type[order][size], order)
            test_sort(bubble_sort, array_type[order][size], order)
            test_sort(radix_sort_counting, array_type[order][size], order)

    with open('performance.json', 'w') as f:
        json.dump(performance, f, indent=4)


if __name__ == "__main__":
    main()
