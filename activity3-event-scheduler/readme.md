# Activity 3 – Event Scheduler

## Description

This project implements a basic event scheduler using a heap-based priority queue in Python. The scheduler models real-world event-driven systems where the most urgent request must always be processed next.

Examples include clinic intake queues, IT support tickets, transportation dispatch systems, and emergency coordination systems.

The scheduler ensures that the most urgent valid event is always selected efficiently.

---

## How Events Are Stored

Each event is stored in the heap as a tuple:

```
(priority, created_time, version, event_id, payload)
```

* Lower `priority` value = higher urgency
* `created_time` ensures fair tie-breaking
* `version` prevents outdated entries from being processed
* `event_id` uniquely identifies the event
* `payload` stores event details

Python automatically orders these tuples correctly inside the heap.

---

## Data Structures Used

* **Min-Heap (`heapq`)** – maintains events ordered by priority
* **Dictionary (`current_version`)** – tracks the latest valid version of each event

The dictionary allows cancelled or outdated events to be skipped efficiently.

---

## Supported Operations

* Add event
* Update event (by versioning)
* Cancel event
* Peek next event
* Pop next event
* Automatically discard stale events

---

## Why a Heap Is Better Than a List

A heap allows inserting and removing events in **O(log n)** time while always keeping the most urgent event accessible in **O(1)** time.

If a list or array were used instead, selecting the next highest-priority event would require scanning the entire structure (O(n)) or repeatedly sorting (O(n log n)), which does not scale well.

Since a scheduler repeatedly performs the operation "get next event", using a heap significantly improves efficiency.

---

## Dominant Operation

The operation performed repeatedly in this system is:

> Selecting and removing the next highest-priority event.

This operation dominates runtime in event-driven systems, which is why an efficient priority queue structure is necessary.

---

## Sample Output

Below is sample output produced by running:

```
python event_scheduler.py
```

```
Peek next:
(0, 106, 2, 'E5', 'Tutoring request: URGENT exam in 2 hrs')

Processing order:

Event 1
id: E5
priority: 0
created_time: 106
version: 2
payload: Tutoring request: URGENT exam in 2 hrs
------------------------------
Event 2
id: E2
priority: 1
created_time: 101
version: 1
payload: Emergency supply: oxygen refill
------------------------------
Event 3
id: E4
priority: 1
created_time: 103
version: 1
payload: Public transport: dispatcher call
------------------------------
Event 4
id: E6
priority: 2
created_time: 105
version: 1
payload: Clinic intake: patient B
------------------------------
Event 5
id: E1
priority: 3
created_time: 100
version: 1
payload: Clinic intake: patient A
------------------------------
```

The output demonstrates:

* Correct priority ordering
* Proper tie-breaking by `created_time`
* Updated events replacing older versions
* Cancelled events being skipped automatically

---

## How to Run

From the project folder:

```
python event_scheduler.py
```

---

## Conclusion

This implementation demonstrates how choosing the correct data structure directly impacts system efficiency. A heap-based scheduler ensures scalable and predictable performance for priority-based event processing.
