import heapq
import P1.resources.load_data as load

FILENAME = f"resources/connection_graph.csv"


def get_time_diff(time1, time2):
    h1, m1, s1 = map(int, time1.split(':'))
    h2, m2, s2 = map(int, time2.split(':'))
    if h2 < h1 or (h2 == h1 and m2 < m1) or (h2 == h1 and m2 == m1 and s2 < s1):
        h2 += 24
    return (h2 - h1) * 3600 + (m2 - m1) * 60 + (s2 - s1)


def dijkstra(start, end, time):
    graph = load.load_graph(FILENAME)
    heap = [(0, start, [], time)]
    visited = {}

    # Iterate until the priority queue is empty
    while heap:
        (cost, node, path, act_time) = heapq.heappop(heap)
        # If the node has already been visited, skip it
        if node in visited:
            continue
        # Add the node and its minimum distance to the visited dictionary
        visited[node] = cost
        # If we have reached the end node, return the path
        if node == end:
            return cost, path + [node]

        # Iterate through the neighboring nodes and add them to the priority queue
        if graph[node] is not None:
            for edge in graph[node]:
                (id, company, line, departure_time, arrival_time, start_stop, end_stop, start_stop_lat, start_stop_lon,
                 end_stop_lat, end_stop_lon) = edge
                # Calculate the cost of traveling to the neighboring node
                travel_time = get_time_diff(departure_time, arrival_time) + get_time_diff(act_time, departure_time)
                new_cost = cost + travel_time
                # Add the neighboring node to the priority queue if it hasn't been visited yet
                if end_stop not in visited:
                    node_info = [start_stop + ',' + departure_time + ',' + end_stop + ',' + arrival_time + ',' + line]
                    heapq.heappush(heap, (new_cost, end_stop, path + node_info, arrival_time))
    # If we have exhausted all possible paths and haven't reached the end node, return None
    return None

def print_results(cost, path):
    for edge in path:
        tokens = str(edge).split(',')
        if len(tokens) > 1:
            print("{:<10} {:<40} {:<10} {:<45} {:<5}".format(tokens[1], tokens[0], tokens[3], tokens[2], tokens[4]))
