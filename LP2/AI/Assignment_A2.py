# Romania map with cities and heuristic values
romania_map = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

# Heuristic values for each city (straight-line distance to Bucharest)
heuristics = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Rimnicu Vilcea': 193,
    'Fagaras': 176,
    'Pitesti': 100,
    'Bucharest': 0,
    'Giurgiu': 77,
    'Urziceni': 80,
    'Vaslui': 199,
    'Iasi': 226,
    'Neamt': 234
}

def a_star_search(start, goal):
    open_set = {start}
    closed_set = set()
    g_scores = {city: float('inf') for city in romania_map}
    # print(g_scores)
    g_scores[start] = 0
    f_scores = {city: float('inf') for city in romania_map}
    # print(f_scores)
    f_scores[start] = heuristics[start]

    while open_set:
        current = min(open_set, key=lambda city: f_scores[city])
        if current == goal:
            path = reconstruct_path(goal, came_from)
            return path

        open_set.remove(current)
        closed_set.add(current)

        for neighbor, cost in romania_map[current].items():
            if neighbor in closed_set:
                continue

            tentative_g_score = g_scores[current] + cost

            if neighbor not in open_set or tentative_g_score < g_scores[neighbor]:
                open_set.add(neighbor)
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g_score
                f_scores[neighbor] = g_scores[neighbor] + heuristics[neighbor]

    return None

def reconstruct_path(current, came_from):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path

# Example usage
start_city = 'Arad'
goal_city = 'Bucharest'
came_from = {}
path = a_star_search(start_city, goal_city)

if path:
    print(f"Shortest path from {start_city} to {goal_city}: {path}")
else:
    print(f"No path found from {start_city} to {goal_city}")
