# LLM KV-Cache Memory Model

**Question:** How does context length affect transformer inference KV-cache capacity?

For uncompressed attention, estimate `2 × batch × tokens × layers × KV heads × head dimension × bytes per element`.

Run: `python experiment.py` and `python -m unittest -v`.

**Read:** [vLLM / PagedAttention](https://arxiv.org/abs/2309.06180) and [FlashAttention](https://arxiv.org/abs/2205.14135). Compare capacity with bandwidth and allocation overhead; they are different problems.

**Limitations:** Analytical capacity only, with illustrative parameters; no allocator overhead, fragmentation, accuracy, or hardware benchmarking.

**Next question:** How does grouped-query attention affect cache growth?
