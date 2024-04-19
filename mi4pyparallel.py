from mpi4py import MPI # Import MPI from mpi4py to use the Message Passing Interface for parallel programming.
import numpy as np

# Function to compute the quarter circle
# Define a function f(x) that computes the height of the quarter circle at position x using the equation y = sqrt(1 - x^2).
def f(x):
    return np.sqrt(1 - x**2)

# Set up MPI environment
comm = MPI.COMM_WORLD # Initialize the MPI environment and get the communicator object that enables communication between processes.
rank = comm.Get_rank() # Get the rank of the current process. Rank is the ID assigned to each process in the MPI pool.
size = comm.Get_size() # Get the total number of processes participating in the MPI communicator.

# Number of intervals
N = 10_500_000  # Define the number of intervals N, which determines the resolution and accuracy of the integration.

# Compute the interval size
dx = 1.0 / N # Calculate the width of each interval (dx) as 1 divided by the total number of intervals, covering the range [0, 1].

# Determine the interval for each process
local_n = N // size #Calculate the number of intervals each process should handle, which is the total number of intervals divided by the number of processes.

start = rank * local_n  #Calculate the starting index for the intervals handled by this process.

end = start + local_n if rank != size - 1 else N  #Calculate the ending index for the intervals. If this process is not the last one, it ends at start + local_n. If it is the last process, it should extend to N to cover all intervals.

# Calculate x values for local computation using Numpy
x_values = np.linspace(start * dx, end * dx, end - start, endpoint=False) # Generate an array of x values starting from start*dx to end*dx, with the number of points equal to the number of intervals this process handles. The endpoint is not included to avoid it to be computed twice

# Compute local sum using Numpy
local_sum = np.sum(f(x_values)) * dx # Compute the local sum of the function evaluations at each x value, multiplied by the interval width dx, to approximate the area under the curve for this process's portion of intervals.

# Reduce all of the local sums into the total sum
total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0) # Use MPI's reduce operation to sum up all the local sums from each process. The result will be stored in the root process (rank 0).

# The root process computes and prints the final result
if rank == 0:
    pi_approx = 4 * total_sum
        # If this is the root process, compute the approximation of pi by multiplying the total area (sum of local areas from all processes) by 4.
    print("Pi with MPI:", pi_approx)
