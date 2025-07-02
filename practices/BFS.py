def build_map():
    with open("graph.txt", "r", encoding="utf-8-sig") as file:
        content = [line.strip() for line in file]

    graph = {}

    for line in content: 
        if len(line) == 1: 
            graph[line] = []
        else: 
            key, children = line.split()
            graph[key] = tuple(children)   

    return graph

def get_BFS_path(graph, start, goal): 
    queue = [(start, [start])]
    visited_set = set()

    while queue:
        current, path = queue.pop(0)

        if current == goal:
            return path

        if current not in visited_set:
            visited_set.add(current)
            for neighbor in graph.get(current, []):
                if neighbor not in visited_set:
                    queue.append((neighbor, path + [neighbor]))

    return None

print(get_BFS_path(build_map(), "H", "A"))