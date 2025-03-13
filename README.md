# Visual-Maze-Solver-using-BFS-and-DFS

# Maze Solver using BFS and DFS

## Overview
This project visualizes the process of solving a randomly generated maze using two different pathfinding algorithms: **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**. The solution is animated side by side to compare both algorithms dynamically.

## Features
- Generates a random maze with obstacles.
- Implements **BFS** and **DFS** to find a path from start to goal.
- Visualizes both algorithms side by side for comparison.
- Uses **Matplotlib** for real-time animation.

## Installation
### Prerequisites
Ensure you have Python installed on your system. You can check by running:
```sh
python --version
```
If Python is not installed, download and install it from [python.org](https://www.python.org/).

### Install Dependencies
Run the following command to install the required libraries:
```sh
pip install matplotlib numpy
```

## Usage
Run the script with the following command:
```sh
python visualmaze.py
```
You will be prompted to enter the number of rows and columns for the maze.

### Example Output
- The **left plot** shows the BFS pathfinding process.
- The **right plot** shows the DFS pathfinding process.
- Walls are represented in **black**.
- The **start** position is **green**, and the **goal** is **red**.
- The paths explored by each algorithm are dynamically visualized.

## Contributors
1. Soujanya S P
2. Kushi M Yarnal

## Future Improvements
- Support for weighted graphs with **Dijkstra's algorithm**.
- More advanced maze generation techniques.
- Integration with **Tkinter or PyGame** for an interactive UI.

