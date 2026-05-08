import json
import time
import itertools
import argparse
from collections import defaultdict


def read_file(name):
    with open(name, "r") as f:
        return json.load(f)


def write_file(name, data):
    with open(name, "w") as f:
        json.dump(data, f, indent=2)


def get_times(tasks):
    times = set()

    for task in tasks:
        times.add(task["start"])
        times.add(task["end"])

    return sorted(times)


def get_running(tasks, a, b):
    running = []

    for task in tasks:
        if task["start"] < b and task["end"] > a:
            running.append(task)

    return running


def get_weight(tasks):
    total = 0.0

    for task in tasks:
        total += task["weight"]

    return total


def is_ok(chosen, r, k):
    if not chosen:
        return True

    times = get_times(chosen)

    for i in range(len(times) - 1):
        a = times[i]
        b = times[i + 1]

        running = get_running(chosen, a, b)

        used = 0
        cats = defaultdict(int)

        for task in running:
            used += task["resource"]
            cats[task["category"]] += 1

        if used > r:
            return False

        for c in cats:
            if cats[c] > k:
                return False

    return True


def make_timeline(chosen):
    if not chosen:
        return {}

    out = {}
    times = get_times(chosen)

    for i in range(len(times) - 1):
        a = times[i]
        b = times[i + 1]

        running = get_running(chosen, a, b)

        used = 0
        cats = defaultdict(int)

        for task in running:
            used += task["resource"]
            cats[task["category"]] += 1

        out[f"{a}-{b}"] = {
            "resource_used": used,
            "categories": dict(cats)
        }

    return out


# greedy 1

def greedy1(data):
    r = data["resource_capacity"]
    k = data["category_limit"]
    tasks = data["tasks"]

    tasks = sorted(tasks, key=lambda x: (x["end"], x["start"], x["id"]))
    chosen = []

    t1 = time.perf_counter()

    for task in tasks:
        test = chosen + [task]

        if is_ok(test, r, k):
            chosen.append(task)

    t2 = time.perf_counter()

    return {
        "strategy_name": "greedy1",
        "selected_tasks": [x["id"] for x in chosen],
        "total_weight": round(get_weight(chosen), 2),
        "execution_time_seconds": round(t2 - t1, 6),
        "utilization_timeline": make_timeline(chosen)
    }


# greedy 2

def greedy2(data):
    r = data["resource_capacity"]
    k = data["category_limit"]
    tasks = data["tasks"]

    tasks = sorted(
        tasks,
        key=lambda x: (-(x["weight"] / x["resource"]), x["end"], x["id"])
    )

    chosen = []

    t1 = time.perf_counter()

    for task in tasks:
        test = chosen + [task]

        if is_ok(test, r, k):
            chosen.append(task)

    t2 = time.perf_counter()

    return {
        "strategy_name": "greedy2",
        "selected_tasks": [x["id"] for x in chosen],
        "total_weight": round(get_weight(chosen), 2),
        "execution_time_seconds": round(t2 - t1, 6),
        "utilization_timeline": make_timeline(chosen)
    }


# brute force method

def brute(data):
    r = data["resource_capacity"]
    k = data["category_limit"]
    tasks = data["tasks"]

    if len(tasks) > 15:
        raise ValueError("brute only for n <= 15")

    best = []
    best_w = 0.0

    t1 = time.perf_counter()

    for size in range(len(tasks) + 1):
        for part in itertools.combinations(tasks, size):
            part = list(part)

            if is_ok(part, r, k):
                w = get_weight(part)

                if w > best_w:
                    best_w = w
                    best = part

    t2 = time.perf_counter()

    return {
        "strategy_name": "brute",
        "selected_tasks": [x["id"] for x in best],
        "total_weight": round(best_w, 2),
        "execution_time_seconds": round(t2 - t1, 6),
        "utilization_timeline": make_timeline(best)
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("input_file")
    p.add_argument("--strategy", required=True, choices=["greedy1", "greedy2", "brute"])
    p.add_argument("--output", required=True)

    args = p.parse_args()

    data = read_file(args.input_file)

    if args.strategy == "greedy1":
        ans = greedy1(data)
    elif args.strategy == "greedy2":
        ans = greedy2(data)
    else:
        ans = brute(data)

    print(json.dumps(ans, indent=2))
    write_file(args.output, ans)


if __name__ == "__main__":
    main()