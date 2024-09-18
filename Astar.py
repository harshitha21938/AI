# Function to check if the current color assignment is valid
def is_safe(node, graph, colors, color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

# Backtracking function to assign colors to the nodes
def map_coloring(graph, m, colors, node):
    # If all nodes have been assigned a color, return True
    if node == len(graph):
        return True

    # Try different colors for the current node
    for color in range(1, m + 1):
        # Check if assignment of color is safe
        if is_safe(node, graph, colors, color):
            colors[node] = color
            # Recursively assign colors to the remaining nodes
            if map_coloring(graph, m, colors, node + 1):
                return True
            # If assigning this color doesn't lead to a solution, backtrack
            colors[node] = 0

    return False

# Function to solve the map coloring problem
def solve_map_coloring(graph, m):
    # Initialize all nodes with no color (0)
    colors = [0] * len(graph)

    # Call the backtracking function to solve the problem
    if not map_coloring(graph, m, colors, 0):
        return "No solution exists"
    
    # Return the solution
    return colors

# Example usage:

# Define the adjacency list for the graph (map)
graph = {
    0: [1, 2],  # Node 0 is connected to nodes 1 and 2
    1: [0, 2, 3],  # Node 1 is connected to nodes 0, 2, and 3
    2: [0, 1, 3],  # Node 2 is connected to nodes 0, 1, and 3
    3: [1, 2]   # Node 3 is connected to nodes 1 and 2
}

# Number of colors (e.g., 3 colors)
m = 3

# Solve the map coloring problem
solution = solve_map_coloring(graph, m)

# Print the solution
print("Assigned Colors:", solution)