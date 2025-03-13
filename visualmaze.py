import matplotlib.pyplot as plt
import time
import random
import numpy as np
from collections import deque
from matplotlib.animation import FuncAnimation

def generate_maze(rows, cols, wall_prob=0.2):
    maze = np.zeros((rows, cols), dtype=int)
    for i in range(rows):
        for j in range(cols):
            if random.random() < wall_prob:
                maze[i, j] = 1
    
    x, y = 0, 0
    while (x, y) != (rows - 1, cols - 1):
        maze[x, y] = 0
        if x < rows - 1 and random.random() > 0.5:
            x += 1
        elif y < cols - 1:
            y += 1
    
    maze[0, 0] = 0
    maze[rows-1, cols-1] = 0
    return maze

def bfs_maze_solver(maze, start, goal):
    rows, cols = maze.shape
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    queue = deque([(start, [start])])
    visited = set()
    visited_nodes = []
    
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path, visited_nodes
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx, ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                visited_nodes.append((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    
    return None, visited_nodes

def dfs_maze_solver(maze, start, goal):
    rows, cols = maze.shape
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    stack = [(start, [start])]
    visited = set()
    visited_nodes = []
    
    while stack:
        (x, y), path = stack.pop()
        if (x, y) == goal:
            return path, visited_nodes
        
        if (x, y) not in visited:
            visited.add((x, y))
            visited_nodes.append((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx, ny] == 0 and (nx, ny) not in visited:
                    stack.append(((nx, ny), path + [(nx, ny)]))
    
    return None, visited_nodes

def visualize_side_by_side(maze, bfs_result, dfs_result):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    titles = ["BFS Pathfinding", "DFS Pathfinding"]
    colors = ['blue', 'purple']
    
    def init():
        for ax, title in zip(axes, titles):
            ax.set_xticks(range(maze.shape[1]+1))
            ax.set_yticks(range(maze.shape[0]+1))
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            ax.grid(True)
            ax.set_title(title)
            for x in range(maze.shape[0]):
                for y in range(maze.shape[1]):
                    if maze[x, y] == 1:
                        ax.add_patch(plt.Rectangle((y, maze.shape[0]-1-x), 1, 1, color='black'))
            ax.add_patch(plt.Rectangle((0, maze.shape[0]-1-0), 1, 1, color='green'))
            ax.add_patch(plt.Rectangle((maze.shape[1]-1, 0), 1, 1, color='red'))
        return axes
    
    bfs_visited, bfs_path = bfs_result
    dfs_visited, dfs_path = dfs_result
    bfs_steps = bfs_visited + bfs_path if bfs_path else bfs_visited
    dfs_steps = dfs_visited + dfs_path if dfs_path else dfs_visited
    
    def update(frame):
        if frame < len(bfs_steps):
            x, y = bfs_steps[frame]
            axes[0].add_patch(plt.Rectangle((y, maze.shape[0]-1-x), 1, 1, color='blue', alpha=0.6))
        if frame < len(dfs_steps):
            x, y = dfs_steps[frame]
            axes[1].add_patch(plt.Rectangle((y, maze.shape[0]-1-x), 1, 1, color='purple', alpha=0.6))
        return axes
    
    ani = FuncAnimation(fig, update, frames=max(len(bfs_steps), len(dfs_steps)), init_func=init, repeat=False, interval=100)
    plt.show()

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of cols: "))
maze = generate_maze(rows, cols)
start = (0, 0)
goal = (rows-1, cols-1)

bfs_result = bfs_maze_solver(maze, start, goal)
dfs_result = dfs_maze_solver(maze, start, goal)

visualize_side_by_side(maze, bfs_result, dfs_result)





