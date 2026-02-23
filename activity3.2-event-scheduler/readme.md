# Week 2 — Event Scheduler (Lazy Priority Updates & Cancellations)

## Overview

This project extends the Week 1 event scheduler to support two real-world behaviors:

1. Priority updates (events can become more urgent over time)
2. Cancellations (events can be removed before processing)

The scheduler is implemented using a **min-heap (`heapq`)**, where smaller priority values represent higher urgency.

---

## Design Strategy

### Lazy Priority Updates

Python’s heap does not support efficient in-place priority updates.  
Instead of searching the heap and modifying entries (which would be inefficient), this scheduler uses **lazy updating**:

- A new version of the event is pushed into the heap.
- The old entry remains in the heap.
- Outdated entries are discarded later when they reach the top.

This approach avoids expensive heap scanning and keeps operations efficient.

---

### Cancellation Handling

When an event is canceled:

- It is removed from the `current_version` dictionary.
- It is added to a `canceled` set.
- Any heap entries matching that event ID are skipped when processed.

This guarantees canceled events are never executed.

---

## How to Run

```bash
python event_schedule.py

Sample Output
=== Week 2 Simulation ===

[ADD]
Peek: (1, 101, 1, 'E2', 'Emergency supply: oxygen refill') 

[UPDATE] E5 priority -> 0
Peek after update: (0, 106, 2, 'E5', '[UPDATED] E5: 0')

[CANCEL] E3
Peek after cancel: (0, 106, 2, 'E5', '[UPDATED] E5: 0')

=== Final processing order ===
1. id=E5 priority=0 time=106 version=2 payload=[UPDATED] E5: 0
2. id=E2 priority=1 time=101 version=1 payload=Emergency supply: oxygen refill
3. id=E4 priority=1 time=103 version=1 payload=Public transport: dispatcher call
4. id=E6 priority=2 time=105 version=1 payload=Clinic intake: patient B
5. id=E1 priority=3 time=100 version=1 payload=Clinic intake: patient A


Runtime Analysis :- 

    The operation that dominates runtime in this scheduler is heap insertion and removal, both of which run in O(log n) time. Scanning a list to find and update or remove an event would require O(n) time per operation, which becomes inefficient as the number of events grows. Lazy updating is acceptable because it avoids expensive heap searches by inserting a new version instead of modifying the old one. Outdated entries are discarded only when they reach the top of the heap, so the cleanup cost is spread across pop operations. This approach keeps the scheduler efficient and scalable in practice.

