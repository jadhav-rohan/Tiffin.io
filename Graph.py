import heapq

def find_safest_shortest_path(graph, start, end):
    # Priority queue: (total weight, total risk, current node, path)
    pq = [(0, 0, start, [start])]
    # Dictionary to store the best path found so far (min weight and risk)
    best_paths = {start: (0, 0)}

    while pq:
        current_weight, current_risk, current_node, path = heapq.heappop(pq)
        
        # If the end node is reached, return the path, total weight, and total risk
        if current_node == end:
            return path, current_weight, current_risk
        
        # Explore neighbors
        for neighbor, (weight, risk) in graph[current_node].items():
            new_weight = current_weight + weight
            new_risk = current_risk + risk
            if (neighbor not in best_paths or
                new_weight < best_paths[neighbor][0] or
                (new_weight == best_paths[neighbor][0] and new_risk < best_paths[neighbor][1])):
                best_paths[neighbor] = (new_weight, new_risk)
                new_path = path + [neighbor]
                heapq.heappush(pq, (new_weight, new_risk, neighbor, new_path))
    
    return None  # No path found

def main():
    # Read input
    n = int(input())  # number of routes
    graph = {}
    for _ in range(n):
        u, v, weight, risk = map(int, input().split())
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = (weight, risk)
        graph[v][u] = (weight, risk)  # Assuming undirected graph for bidirectional routes

    start_island = 0  # Assuming starting from island 0
    end_island = max(graph.keys())  # Assuming destination is the highest numbered island
    
    # Find the safest and shortest path
    result = find_safest_shortest_path(graph, start_island, end_island)
    if result:
        path, total_weight, total_risk = result
        print(f"Path: {path}")
        print(f"Total weight (distance): {total_weight}")
        print(f"Total risk: {total_risk}")
    else:
        print("No path found")

if __name__ == "__main__":
    main()
