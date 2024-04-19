from multiprocessing import Pool # Import the Pool class from the multiprocessing module to manage a pool of worker processes.
import numpy as np

# Function to integrate
def f(x):
    return np.sqrt(1 - x**2) # Define a function f(x) which calculates the square root of (1 - x^2), used to determine the height of rectangles in numerical integration.

# Function that each worker will execute. Now it takes a range and computes the sum over that range.

def chunk_integration(chunk):
    start, end, dx = chunk     # Define the function chunk_integration which takes a tuple 'chunk' containing start and end indices, and the width of intervals (dx).
    
    # Create an array 'x' of values from start*dx to end*dx with a length equal to (end - start). 
    # This represents the x-coordinates of the left edges of the rectangles.
    x = np.linspace(start * dx, end * dx, end - start, endpoint=False)
    
    return np.sum(f(x))     # Return the sum of the values of f(x) for these x-coordinates. This represents the sum of the areas of rectangles in the given chunk.

# Main function using multiprocessing for the numerical integration
def compute_pi_parallel(n_processes, n_intervals):
    dx = 1.0 / n_intervals     # Calculate the width of each interval (dx) as the interval [0,1] divided by the number of intervals (n_intervals).
    
    # Determine the number of intervals each process should handle, dividing the total number of intervals by the number of processes.
    chunk_size = n_intervals // n_processes
    chunks = [(i * chunk_size, (i + 1) * chunk_size, dx) for i in range(n_processes)]     # Create a list of tuples, each representing the start and end indices for the intervals a process will handle, and the interval width.

    # Handle any leftover intervals
    # If the total number of intervals isn't evenly divisible by the number of processes, add the remainder as an additional chunk.
    if n_intervals % n_processes != 0:
        chunks.append((n_processes * chunk_size, n_intervals, dx))

    # Create a pool of worker processes and distribute the function chunk_integration over the chunks. Collect the results.
    with Pool(processes=n_processes) as pool:
        results = pool.map(chunk_integration, chunks)

    # Sum the areas computed by each process, multiply by the width of each rectangle (dx), and then by 4 to scale up for the full circle.
    pi_approx = 4 * dx * sum(results)
    print("Pi using multiprocessing:", pi_approx)

n_processes = 4  # Number of processes to use
n_intervals = 10_500_000  # Number of intervals

# Call the function to compute pi
compute_pi_parallel(n_processes, n_intervals)