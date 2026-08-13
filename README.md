# ruh

Parallel computation runtime for free-threaded Python

## Operations
1. Data Parallelism - map
2. Selection - filter
3. Reduction - reduce

```bash
ruh.reduce(add, numbers)

1 ─┐
2 ─┤
3 ─┤── parallel computation ──┐
4 ─┤                           │
5 ─┘                           ▼
                              sum
                               │
                               ▼
                              15
```

## Iterators

```bash
Level 1 — Iterator mechanics
    1. Index
    2. Range
    3. Reverse

Level 2 — Lazy composition
    4. Filter
    5. Map
    6. Chain
    7. Zip

Level 3 — Stateful iteration
    8. Batch
    9. Peek
    10. Look-ahead

Level 4 — Non-linear traversal
    11. Tree DFS
    12. Tree BFS
    13. Recursive/nested

Level 5 — Parallel iteration
    14. Splittable iterator
    15. Splittable + size
    16. Parallel executor
    17. Work stealing
```

## Architecture

```python
┌─────────────────────────────────────────┐
│             User API                    │
│                                         │
│ map / filter / reduce / pipeline / fork │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│         Computation Model               │
│                                         │
│ tasks / dependencies / chunks / streams  │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│             Scheduler                   │
│                                         │
│ queues / workers / stealing / balancing │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│        Free-threaded CPython            │
│                                         │
│             actual execution            │
└─────────────────────────────────────────┘
```
