import random

def generate_maze(width, height):
    """Generates a random maze using recursive backtracking."""

    maze = [['█' for _ in range(width * 2 + 1)] for _ in range(height * 2 + 1)]
    
    def carve_path(x, y):
        maze[y][x] = ' '
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < width * 2 and 0 < ny < height * 2 and maze[ny][nx] == '█':
                maze[ny - dy // 2][nx - dx // 2] = ' '
                carve_path(nx, ny)

    carve_path(1, 1)
    return maze

def print_maze(maze):
    """Prints the maze to the console."""
    for row in maze:
        print(''.join(row))

# Example usage:
width = 20
height = 10
maze = generate_maze(width, height)
print_maze(maze)