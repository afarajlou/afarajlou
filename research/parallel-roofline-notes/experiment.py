def roofline_gflops(intensity_flops_per_byte, peak_gflops, bandwidth_gb_per_s):
    if min(intensity_flops_per_byte, peak_gflops, bandwidth_gb_per_s) <= 0:
        raise ValueError("positive inputs required")
    return min(peak_gflops, intensity_flops_per_byte * bandwidth_gb_per_s)

if __name__ == "__main__":
    peak, bandwidth = 100.0, 20.0  # hypothetical, not measurements
    for intensity in (0.25, 0.5, 1, 2, 5, 10):
        print(f"AI={intensity:>5}: roofline bound={roofline_gflops(intensity, peak, bandwidth):.1f} GFLOP/s")
