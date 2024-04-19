import numpy as np # Import the numpy library as np to use its mathematical functions

# Function to compute the quarter circle area using Riemann sums
def compute_pi(N):
    # Delta x, the width of each small rectangle
    delta_x = 1/N
    # Calculate the width of each rectangle (delta_x) as the interval [0,1] divided by N.

    area = 0
    # Initialize the variable 'area' to store the total area of rectangles.

    # Iterate over a range of N, where 'i' is the index from 0 to N-1 representing each rectangle.
    for i in range(N):        
        # Calculate the height of the rectangle at x = i * delta_x
        height = np.sqrt(1 - (i * delta_x)**2)
        # Compute the height of the rectangle using the circle equation x^2 + y^2 = 1.
        # Here, x is i * delta_x, and we solve for y which gives the height of the rectangle at that x.

        # Add the area of the rectangle to the total area
        area += height * delta_x  # Multiply the height by the width (delta_x) to get the area of the rectangle and add it to 'area'.

    # The area calculated is for a quarter circle, multiply by 4 for the full circle
    pi_approx = area * 4
    print("Pi with Python", pi_approx) # Print the approximate value of pi.

# Calculate pi using the function
calculated_pi = compute_pi(10_500_000)
