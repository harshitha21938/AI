from queue import PriorityQueue
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
def a_star(graph, start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start)) 
    g_score = {start: 0}
    came_from = {start: None}
    while not open_list.empty():
        current = open_list.get()[1]
        if current == goal:
            return reconstruct_path(came_from, current)
        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost 
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                open_list.put((f_score, neighbor))
                came_from[neighbor] = current
    return None  
def reconstruct_path(came_from, current):
    path = []
    while current:
        path.append(current)
        current = came_from[current]
    return path[::-1]
graph = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],
    (0, 1): [((0, 0), 1), ((1, 1), 1), ((0, 2), 1)],
    (0, 2): [((0, 1), 1), ((1, 2), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1)],
    (1, 1): [((1, 0), 1), ((0, 1), 1), ((1, 2), 1)],
    (1, 2): [((0, 2), 1), ((1, 1), 1)]
}
start = (0, 0)
goal = (1, 2)
path = a_star(graph, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found")