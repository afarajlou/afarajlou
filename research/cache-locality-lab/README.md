# Cache Locality Lab

**Question:** How does working-set size affect hit rate in a small LRU cache?

A standard-library Python simulation of a fully associative least-recently-used cache, comparing a scan of eight addresses with repeated access to a four-address working set.

Run on Windows: `python experiment.py` and `python -m unittest -v`.

**Read:** Hennessy & Patterson, *Computer Architecture: A Quantitative Approach* (memory hierarchy); [gem5 documentation](https://www.gem5.org/documentation/).

**Limitations:** This trace model does not measure actual CPU cache behavior, latency, prefetching, or realistic associativity.

**Next question:** What changes with set associativity and cache-block size?
