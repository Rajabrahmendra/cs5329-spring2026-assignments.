import heapq

# entry: (priority, time, version, event_id, payload)

def create_scheduler():
    heap = []
    current_version = {}
    canceled = set()
    return heap, current_version, canceled

def add_event(heap, current_version, event_id, priority, created_time, payload):
    # add (or re-add) by bumping version
    version = current_version.get(event_id, 0) + 1
    current_version[event_id] = version
    heapq.heappush(heap, (priority, created_time, version, event_id, payload))

def update_priority(heap, current_version, event_id, new_priority, update_time):
    # lazy update: push new version; old stays and becomes stale
    version = current_version.get(event_id, 0) + 1
    current_version[event_id] = version
    heapq.heappush(heap, (new_priority, update_time, version, event_id, f"[UPDATED] {event_id}: {new_priority}"))

def cancel_event(current_version, canceled, event_id):
    # cancel forever (even if someone tries to update later)
    canceled.add(event_id)
    if event_id in current_version:
        del current_version[event_id]

def discard_stale_top(heap, current_version, canceled):
    # drop canceled/outdated entries until top is valid
    while heap:
        priority, created_time, version, event_id, payload = heap[0]
        if event_id in canceled:
            heapq.heappop(heap)
            continue
        latest = current_version.get(event_id)
        if latest is None:
            heapq.heappop(heap)
            continue
        if version != latest:
            heapq.heappop(heap)
            continue
        break

def peek_next(heap, current_version, canceled):
    # peek next valid event
    discard_stale_top(heap, current_version, canceled)
    return heap[0] if heap else None

def pop_next(heap, current_version, canceled):
    # pop next valid event
    discard_stale_top(heap, current_version, canceled)
    if not heap:
        return None
    event = heapq.heappop(heap)
    priority, created_time, version, event_id, payload = event
    if current_version.get(event_id) == version:
        del current_version[event_id]
    return event

def main():
    heap, current_version, canceled = create_scheduler()

    print("=== Week 2 Simulation ===\n")

    print("[ADD]")
    add_event(heap, current_version, "E1", 3, 100, "Clinic intake: patient A")
    add_event(heap, current_version, "E2", 1, 101, "Emergency supply: oxygen refill")
    add_event(heap, current_version, "E3", 2, 102, "IT help desk: laptop issue")
    add_event(heap, current_version, "E4", 1, 103, "Public transport: dispatcher call")
    add_event(heap, current_version, "E5", 5, 104, "Tutoring request: calculus")
    add_event(heap, current_version, "E6", 2, 105, "Clinic intake: patient B")
    print("Peek:", peek_next(heap, current_version, canceled), "\n")

    print("[UPDATE] E5 priority -> 0")
    update_priority(heap, current_version, "E5", 0, 106)
    print("Peek after update:", peek_next(heap, current_version, canceled), "\n")

    print("[CANCEL] E3")
    cancel_event(current_version, canceled, "E3")
    print("Peek after cancel:", peek_next(heap, current_version, canceled), "\n")

    print("=== Final processing order ===")
    i = 1
    while True:
        ev = pop_next(heap, current_version, canceled)
        if ev is None:
            break
        p, t, v, eid, payload = ev
        print(f"{i}. id={eid} priority={p} time={t} version={v} payload={payload}")
        i += 1

if __name__ == "__main__":
    main()