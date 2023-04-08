import heapq
import math

import P1.resources.load_data

FILENAME = f"resources/connection_graph.csv"


def get_time_diff(time1, time2):
    h1, m1, s1 = map(int, time1.split(':'))
    h2, m2, s2 = map(int, time2.split(':'))
    if h2 < h1 or (h2 == h1 and m2 < m1) or (h2 == h1 and m2 == m1 and s2 < s1):
        h2 += 24
    return (h2 - h1) * 3600 + (m2 - m1) * 60 + (s2 - s1)


def astar(start, end, time, heuristic):

    graph = P1.resources.load_data.load_graph(FILENAME)

    # astar: F=G+H, we name F as f_distance, G as g_distance,
    # H as heuristic
    f_distance = {node: float('inf') for node in graph}
    f_distance[start] = 0

    g_distance = {node: float('inf') for node in graph}
    g_distance[start] = 0
    came_from = {node: None for node in graph}
    came_from[start] = start

    queue = [(0, start, time)]
    while queue:
        current_f_distance, current_node, act_time = heapq.heappop(queue)
        if current_node == end:
            return f_distance, came_from

        if graph[current_node] is not None:
            for edge in graph[current_node]:
                (id, company, line, departure_time, arrival_time, start_stop, next_node, start_stop_lat, start_stop_lon,
                 end_stop_lat, end_stop_lon) = edge

                # calculating distance - time criterion
                temp_g_distance = g_distance[current_node] + get_time_diff(departure_time, arrival_time) \
                                  + get_time_diff(act_time, departure_time)

                # if new distance is better than previous distance to next node
                if temp_g_distance < g_distance[next_node]:
                    g_distance[next_node] = temp_g_distance
                    f_distance[next_node] = temp_g_distance + heuristic(start_stop_lat, start_stop_lon, end_stop_lat, end_stop_lon)
                    came_from[next_node] = current_node + ", " + line + ", " + departure_time + \
                                           ", " + next_node + ", " + arrival_time
                    heapq.heappush(queue, (f_distance[next_node], next_node, arrival_time))


def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2) * 100)


def manhattan_distance(x1, y1, x2, y2):
    return 100 * int(100 * (abs(x1 - x2) + abs(y1 - y2)))


def print_results(start_stop, end_stop, distances, path):
    curr_node = end_stop
    result = []
    while curr_node is not start_stop:
        result.append(curr_node)
        curr_node = path[curr_node.split(',')[0]]

    for edge in result[::-1]:
        tokens = str(edge).split(',')
        if len(tokens) > 1:
            print("{:<10} {:<40} {:<10} {:<45} {:<5}".format(tokens[2], tokens[0], tokens[4], tokens[3], tokens[1]))
