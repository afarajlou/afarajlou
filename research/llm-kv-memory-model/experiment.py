def kv_cache_bytes(batch, context, layers, kv_heads, head_dim, bytes_per_element):
    args = (batch, context, layers, kv_heads, head_dim, bytes_per_element)
    if any(not isinstance(v, int) or v <= 0 for v in args):
        raise ValueError("all arguments must be positive integers")
    return 2 * batch * context * layers * kv_heads * head_dim * bytes_per_element

if __name__ == "__main__":
    for tokens in (1024, 4096, 8192, 16384):
        gib = kv_cache_bytes(1, tokens, 32, 8, 128, 2) / 2**30
        print(f"context={tokens:5d}, KV cache={gib:.3f} GiB")
