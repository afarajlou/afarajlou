from collections import OrderedDict

def simulate(trace, capacity):
    if capacity < 1:
        raise ValueError("capacity must be positive")
    cache = OrderedDict()
    hits = 0
    for address in trace:
        if address in cache:
            hits += 1
            cache.move_to_end(address)
        else:
            if len(cache) == capacity:
                cache.popitem(last=False)
            cache[address] = None
    n = len(trace)
    return {"accesses": n, "hits": hits, "misses": n - hits, "hit_rate": hits/n if n else 0}

if __name__ == "__main__":
    for name, trace in [("sequential_scan", [i for _ in range(4) for i in range(8)]), ("small_working_set", [i % 4 for i in range(32)])]:
        print(name, simulate(trace, capacity=4))
