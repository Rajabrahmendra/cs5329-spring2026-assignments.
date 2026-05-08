import json
import os
import random


cats = ["compute", "io", "network"]


def save_file(name, data):
    with open(name, "w") as f:
        json.dump(data, f, indent=2)


def make_tasks(n, max_time, max_res, main_cat=None):
    tasks = []

    for i in range(n):
        start = random.randint(0, max_time - 2)
        end = random.randint(start + 1, max_time)
        weight = round(random.uniform(1.0, 100.0), 2)
        resource = random.randint(1, max_res)

        if main_cat and random.random() < 0.8:
            category = main_cat
        else:
            category = random.choice(cats)

        tasks.append({
            "id": i,
            "start": start,
            "end": end,
            "weight": weight,
            "resource": resource,
            "category": category
        })

    return tasks


def sparse():
    return {
        "resource_capacity": 15,
        "category_limit": 3,
        "tasks": make_tasks(10, 30, 4)
    }


def dense():
    tasks = []

    for i in range(50):
        start = random.randint(0, 10)
        end = random.randint(start + 1, 15)

        tasks.append({
            "id": i,
            "start": start,
            "end": end,
            "weight": round(random.uniform(5.0, 50.0), 2),
            "resource": random.randint(2, 6),
            "category": random.choice(cats)
        })

    return {
        "resource_capacity": 8,
        "category_limit": 2,
        "tasks": tasks
    }


def heavy():
    return {
        "resource_capacity": 10,
        "category_limit": 1,
        "tasks": make_tasks(30, 25, 4, "compute")
    }


# ---- ONLY THIS FUNCTION WAS CHANGED ----
def bad():
    return {
        "resource_capacity": 10,
        "category_limit": 3,
        "tasks": [
            {
                "id": 0,
                "start": 0,
                "end": 2,
                "weight": 5.0,
                "resource": 9,
                "category": "io"
            },
            {
                "id": 1,
                "start": 2,
                "end": 4,
                "weight": 5.0,
                "resource": 9,
                "category": "io"
            },
            {
                "id": 2,
                "start": 4,
                "end": 6,
                "weight": 5.0,
                "resource": 9,
                "category": "io"
            },
            {
                "id": 3,
                "start": 6,
                "end": 8,
                "weight": 5.0,
                "resource": 9,
                "category": "io"
            },
            {
                "id": 4,
                "start": 8,
                "end": 10,
                "weight": 5.0,
                "resource": 9,
                "category": "io"
            },
            {
                "id": 5,
                "start": 0,
                "end": 10,
                "weight": 100.0,
                "resource": 9,
                "category": "compute"
            }
        ]
    }
# ---- END OF CHANGE ----


def bench100():
    return {
        "resource_capacity": 20,
        "category_limit": 3,
        "tasks": make_tasks(100, 60, 6)
    }


def bench500():
    return {
        "resource_capacity": 30,
        "category_limit": 4,
        "tasks": make_tasks(500, 120, 8)
    }


def bench1000():
    return {
        "resource_capacity": 40,
        "category_limit": 5,
        "tasks": make_tasks(1000, 200, 10)
    }


def main():
    os.makedirs("testcases", exist_ok=True)
    random.seed(42)

    files = {
        "sparse.json": sparse(),
        "dense.json": dense(),
        "category_heavy.json": heavy(),
        "adversarial.json": bad(),
        "bench100.json": bench100(),
        "bench500.json": bench500(),
        "bench1000.json": bench1000()
    }

    for file_name, data in files.items():
        save_file(os.path.join("testcases", file_name), data)

    print("files created")


if __name__ == "__main__":
    main()