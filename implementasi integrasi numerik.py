import time
import math

def f(x):
    return 4 / (1 + x**2)

def simpson_1_3(a, b, N):
    if N % 2 == 1:
        raise ValueError("N must be an even number.")
    
    h = (b - a) / N
    S = f(a) + f(b)
    
    for i in range(1, N):
        x = a + i * h
        if i % 2 == 0:
            S += 2 * f(x)
        else:
            S += 4 * f(x)
    
    return (h / 3) * S

def calculate_rms_error(approximation, reference_value):
    return math.sqrt((approximation - reference_value) ** 2)

reference_pi = 3.14159265358979323846
N_values = [10, 100, 1000, 10000]

for N in N_values:
    start_time = time.time()
    approx_pi = simpson_1_3(0, 1, N)
    end_time = time.time()
    elapsed_time = end_time - start_time
    rms_error = calculate_rms_error(approx_pi, reference_pi)
    print(f"N = {N}, Approximation = {approx_pi}, RMS Error = {rms_error}, Time = {elapsed_time:.5f} seconds")
