import random
import math
import multiprocessing
import sys


def estimate_pi(points):
    inside_circle = 0
    total_points = points

    for _ in range(points):
        x = random.random()
        y = random.random()

        if math.sqrt(x**2 + y**2) <= 1:
            inside_circle += 1

    pi_estimate = 4 * (inside_circle / total_points)
    return pi_estimate


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        num_points = int(sys.argv[1])
    except ValueError:
        print("Invalid number of points. Please enter an integer.")
        sys.exit(1)

    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)

    chunk_size = num_points // num_processes
    
    results = pool.map(estimate_pi, [chunk_size] * num_processes)
    pool.close()
    pool.join()

    estimated_pi = sum(results) / num_processes
    print(f"Оценка числа π: {estimated_pi}")