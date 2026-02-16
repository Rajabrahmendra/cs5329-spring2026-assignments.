import heapq

def create_scheduler():
    heap = []
    current_version = {}
    return heap, current_version

def add_event(heap, current_version, event_id, priority, created_time, payload):
    version = current_version.get(event_id, 0) + 1
    current_version[event_id] = version
    heapq.heappush(heap, (priority, created_time, version, event_id, payload))

def cancel_event(current_version, event_id):
    if event_id in current_version:
        del current_version[event_id]

def discard_stale_top(heap, current_version):
    while heap:
        priority, created_time, version, event_id, payload = heap[0]
        latest = current_version.get(event_id)

        if latest is None:
            heapq.heappop(heap)
            continue

        if version != latest:
            heapq.heappop(heap)
            continue

        break

def peek_next(heap, current_version):
    discard_stale_top(heap, current_version)
    if not heap:
        return None
    return heap[0]

def pop_next(heap, current_version):
    discard_stale_top(heap, current_version)
    if not heap:
        return None

    event = heapq.heappop(heap)
    priority, created_time, version, event_id, payload = event

    latest = current_version.get(event_id)
    if latest == version:
        del current_version[event_id]

    return event

def main():
    heap, current_version = create_scheduler()

    add_event(heap, current_version, "E1", 3, 100, "Clinic intake: patient A")
    add_event(heap, current_version, "E2", 1, 101, "Emergency supply: oxygen refill")
    add_event(heap, current_version, "E3", 2, 102, "IT help desk: laptop issue")
    add_event(heap, current_version, "E4", 1, 103, "Public transport: dispatcher call")
    add_event(heap, current_version, "E5", 5, 104, "Tutoring request: calculus")
    add_event(heap, current_version, "E6", 2, 105, "Clinic intake: patient B")

    add_event(heap, current_version, "E5", 0, 106, "Tutoring request: URGENT exam in 2 hrs")
    cancel_event(current_version, "E3")

    print("Peek next:")
    print(peek_next(heap, current_version))

    print("\nProcessing order:\n")

    count = 1
    while True:
        ev = pop_next(heap, current_version)
        if ev is None:
            break

        priority, created_time, version, event_id, payload = ev

        print(f"Event {count}")
        print(f"id: {event_id}")
        print(f"priority: {priority}")
        print(f"created_time: {created_time}")
        print(f"version: {version}")
        print(f"payload: {payload}")
        print("-" * 30)

        count += 1

if __name__ == "__main__":
    main()

