import matplotlib.pyplot as plt
import time
from collections import deque
import matplotlib.patches as patches

def animate_maze(maze, path, visited_nodes, start, goal, title):
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
        ax.add_patch(plt.Rectangle((y, rows-1-x), 1, 1, color='gray', alpha=0.5))
        plt.pause(0.1)
    
    for (x, y) in path:
        ax.add_patch(plt.Rectangle((y, rows-1-x), 1, 1, color='blue', alpha=0.8))
        plt.pause(0.1)
    
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
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                    stack.append(((nx, ny), path + [(nx, ny)]))
    
    return None, visited_nodes  # No path found

# Example Maze (0 = Open, 1 = Wall)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

bfs_path, bfs_visited = bfs_maze_solver(maze, start, goal)
dfs_path, dfs_visited = dfs_maze_solver(maze, start, goal)

print("BFS Shortest Path:", bfs_path)
print("DFS Found Path:", dfs_path)

# Animate BFS and DFS search
animate_maze(maze, bfs_path, bfs_visited, start, goal, "BFS Pathfinding")
animate_maze(maze, dfs_path, dfs_visited, start, goal, "DFS Pathfinding")
