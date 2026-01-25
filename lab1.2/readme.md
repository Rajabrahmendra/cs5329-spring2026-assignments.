Here’s a **complete `README.md`** for your Lab 1.2 assignment. You can save this in your repository (for example, in `cs5329-spring2026-assignments/lab1.2/README.md`):

---

````markdown
# CS5329 Spring 2026 - Lab 1.2: Linear vs Binary Search

## Description
This Python script `linear_vs_binary_search.py` compares the performance of **linear search** and **binary search** algorithms.  

The script does the following:  
1. Implements **linear search** and **binary search** functions.  
2. Performs a timing experiment to measure the execution time of both algorithms on lists of increasing size.  
3. Prints the results in a formatted manner.  
4. Provides an analysis explaining the observed growth rates of each algorithm.  

---

## Files
- `linear_vs_binary_search.py` – Python script implementing the searches, timing experiment, and analysis.  
- `README.md` – this documentation file.

---

## Usage

1. Make sure Python 3 is installed on your system.  
2. Open a terminal (PowerShell, Command Prompt, or VS Code terminal).  
3. Navigate to the project folder:

```powershell
cd cs5329-spring2026-assignments/lab1.2
````

4. Run the script:

```powershell
python linear_vs_binary_search.py
```

5. Example output (times may vary based on your computer speed):

```
n=10000: Linear search time=0.00151s, Binary search time=0.00002s
n=50000: Linear search time=0.00753s, Binary search time=0.00003s
n=100000: Linear search time=0.01510s, Binary search time=0.00003s
n=200000: Linear search time=0.03025s, Binary search time=0.00004s
```

---

## Requirements

* Python 3.x
* Standard Python libraries (`time`, `random`) – no external packages required.

---

## Analysis

* When the input size doubles, the runtime of **linear search** roughly doubles. This is because it has **O(n)** complexity — it checks each element one by one.
* The runtime of **binary search** grows very slowly, even when the input doubles. This is because it has **O(log n)** complexity — it repeatedly halves the search space.
* Linear search is simple but inefficient for large arrays. Binary search is much faster for large, sorted arrays.

---

## Author

* Raja brahmendra Veerepalli
* CS5329 - Spring 2026

```


