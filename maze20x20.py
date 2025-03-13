import matplotlib.pyplot as plt
import time
import random
from collections import deque
import matplotlib.patches as patches

def generate_maze(rows, cols, wall_prob=0.2):  # Reduced wall probability
    maze = [[0 if random.random() > wall_prob else 1 for _ in range(cols)] for _ in range(rows)]
    maze[0][0] = 0  # Ensure start is open
    maze[rows-1][cols-1] = 0  # Ensure goal is open
    
    # Ensure at least one clear path by carving a simple corridor
    for i in range(min(rows, cols)):
        maze[i][0] = 0
    return maze

def print_maze(maze):
    for row in maze:
        print("".join(['█' if cell == 1 else ' ' for cell in row]))

def animate_maze(maze, path, visited_nodes, start, goal, title, path_color):
    if path is None:
        print(f"No path found for {title}")
        return
    
    rows, cols = len(maze), len(maze[0])
    fig, ax = plt.subplots()
    ax.set_xticks(range(cols+1))
    ax.set_yticks(range(rows+1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True)
    ax.set_title(title)
    
    for x in range(rows):
        for y in range(cols):
            if maze[x][y] == 1:
                ax.add_patch(plt.Rectangle((y, rows-1-x), 1, 1, color='black'))
    
    ax.add_patch(plt.Rectangle((start[1], rows-1-start[0]), 1, 1, color='green'))
    ax.add_patch(plt.Rectangle((goal[1], rows-1-goal[0]), 1, 1, color='red'))
    
    plt.ion()
    for (x, y) in visited_nodes:
        ax.add_patch(plt.Rectangle((y, rows-1-x), 1, 1, color='lightgray', alpha=0.5))
        plt.pause(0.005)  # Reduced delay
    
    for (x, y) in path:
        ax.add_patch(plt.Rectangle((y, rows-1-x), 1, 1, color=path_color, alpha=0.8))
        plt.pause(0.02)  # Reduced delay
    
    plt.ioff()
    plt.show()

def bfs_maze_solver(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    directions = [(0,1), (0,-1), (1,0), (-1,0)]  # Right, Left, Down, Up
    queue = deque([(start, [start])])  # Store (position, path)
    visited = set()
    visited_nodes = []
    
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path, visited_nodes  # Return the shortest path
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                visited_nodes.append((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    
    return None, visited_nodes  # No path found

def dfs_maze_solver(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    directions = [(0,1), (0,-1), (1,0), (-1,0)]  # Right, Left, Down, Up
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
            # Sort directions based on proximity to goal (prioritize shorter paths)
            sorted_directions = sorted(directions, key=lambda d: abs((x + d[0]) - goal[0]) + abs((y + d[1]) - goal[1]))
            for dx, dy in sorted_directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                    stack.append(((nx, ny), path + [(nx, ny)]))
    
    return None, visited_nodes  # No path found

# Generate a larger random maze
rows, cols = 20, 20  # Increased maze size
maze = generate_maze(rows, cols)
print_maze(maze)  # Debugging: Print the maze

start = (0, 0)
goal = (rows-1, cols-1)

bfs_path, bfs_visited = bfs_maze_solver(maze, start, goal)
dfs_path, dfs_visited = dfs_maze_solver(maze, start, goal)

print("BFS Shortest Path:", bfs_path if bfs_path else "No path found")
print("DFS Found Path:", dfs_path if dfs_path else "No path found")

# Animate BFS and DFS search
animate_maze(maze, bfs_path, bfs_visited, start, goal, "BFS Pathfinding", "blue")
animate_maze(maze, dfs_path, dfs_visited, start, goal, "DFS Pathfinding", "purple")

 
