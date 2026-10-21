# Roofline Model: A Small Exploration

**Question:** When is a kernel limited by compute throughput rather than memory bandwidth?

Model the upper bound `min(peak GFLOP/s, bandwidth GB/s × FLOP/byte)`.

Run: `python experiment.py` and `python -m unittest -v`.

The CPU values are **illustrative assumptions**, not measured benchmark results.

**Read:** [Williams, Waterman & Patterson, Roofline performance model](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2008/EECS-2008-134.html).

**Next question:** How should real measurements replace the hypothetical limits?
