
# Parallel Programming with Python

This repository contains a collection of Python scripts and a Jupyter notebook demonstrating different approaches to parallel programming. These examples showcase methods to compute an approximation of π (pi) using numerical integration with varying degrees of parallelization.

## Repository Contents

- `basicpython.py`: A script using pure Python (no parallelism) to approximate the value of π using Riemann sums. It demonstrates a simple numerical integration to compute the area of a quarter circle.

- `multiprocess.py`: This script utilizes the Python `multiprocessing` library to parallelize the computation of π. It demonstrates how to distribute computations across multiple processes to utilize multiple CPU cores.

- `mi4pyparallel.py`: A more advanced parallelization script using the MPI (Message Passing Interface) via `mpi4py`. This approach is suitable for distributed computing environments and demonstrates splitting the computational task across multiple nodes.

- `Parallel Programing with Python.ipynb`: A Jupyter notebook that provides an educational overview of parallel programming concepts in Python, including examples and explanations of the techniques used in the scripts.

## Setup and Running the Programs

### Prerequisites

Ensure you have Python installed on your system, along with the following packages:
- numpy
- mpi4py (for `mi4pyparallel.py`)
- Jupyter (to run the notebook)

You can install these using pip:
```bash
pip install numpy mpi4py 
```

### Running the Scripts

To run any of the Python scripts, use the following command in your terminal:
```bash
python <script_name>.py
```
Replace `<script_name>` with the name of the script you want to run (`basicpython.py`, `multiprocess.py`, or `mi4pyparallel.py`).

### Using the Jupyter Notebook

To explore the notebook:
1. Navigate to the repository directory.
2. Run the following command to start Jupyter:
```bash
jupyter notebook
```
3. Open the `Parallel Programing with Python.ipynb` file from the Jupyter interface.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
