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
