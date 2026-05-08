
# Task Scheduling Assignment

## Project overview

This project is about scheduling tasks using three methods:

- greedy1
- greedy2
- brute force

Each task has a start time, end time, weight, resource value, and category.

The goal is to choose a set of tasks with high total weight while following these rules:

- total resource use must stay within the resource capacity
- category overlap must stay within the category limit
- tasks cannot be partially scheduled

## Files in the project

- `scheduler.py` - main program
- `test_generator.py` - creates generated test files
- `testcases/` - input JSON files
- `results/` - output JSON files
- `analysis.md` - written analysis and reflection
- `README.md` - instructions to run the project

## Python version

This project uses Python 3.

## How to generate test files

Run this command:

```bash
python3 test_generator.py
````

This creates generated test files inside the `testcases` folder, such as:

* `sparse.json`
* `dense.json`
* `category_heavy.json`
* `adversarial.json`
* `bench100.json`
* `bench500.json`
* `bench1000.json`

## How to run the program

### Run greedy1

```bash
python3 scheduler.py testcases/sparse.json --strategy greedy1 --output results/sparse_greedy1.json
```

### Run greedy2

```bash
python3 scheduler.py testcases/sparse.json --strategy greedy2 --output results/sparse_greedy2.json
```

### Run brute force

```bash
python3 scheduler.py testcases/sparse.json --strategy brute --output results/sparse_brute.json
```

## Example with a small custom file

```bash
python3 scheduler.py testcases/simple.json --strategy greedy1 --output results/simple_greedy1.json
```

## Benchmark examples

### For 100 tasks

```bash
python3 scheduler.py testcases/bench100.json --strategy greedy1 --output results/bench100_greedy1.json
python3 scheduler.py testcases/bench100.json --strategy greedy2 --output results/bench100_greedy2.json
```

### For 500 tasks

```bash
python3 scheduler.py testcases/bench500.json --strategy greedy1 --output results/bench500_greedy1.json
python3 scheduler.py testcases/bench500.json --strategy greedy2 --output results/bench500_greedy2.json
```

### For 1000 tasks

```bash
python3 scheduler.py testcases/bench1000.json --strategy greedy1 --output results/bench1000_greedy1.json
python3 scheduler.py testcases/bench1000.json --strategy greedy2 --output results/bench1000_greedy2.json
```

## Important note

Brute force should only be used for small inputs. It is not practical for large test cases.

## Output

Each output JSON file includes:

* strategy name
* selected task ids
* total weight
* execution time
* utilization timeline

## Short explanation of the methods

* `greedy1` chooses tasks based on earliest finish time
* `greedy2` chooses tasks based on weight per resource
* `brute` checks all possible valid combinations for small cases


