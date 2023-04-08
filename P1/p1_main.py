import time

from algorithms import dijkstra as djk
from algorithms import astar_time, astar_changes
START_STOP = "LEŚNICA"
END_STOP = "KSIĘŻE MAŁE"
TIME = "07:30:00"


if __name__ == '__main__':
    print("==================================================================================================================")
    print("      DIJKSTRA TIME CRITERION       ")
    print(f"Start stop: {START_STOP}, End Stop: {END_STOP}, Arrival time at start stop: {TIME}")
    start_time = time.time()
    cost, path = djk.dijkstra(START_STOP, END_STOP, TIME)
    end_time = time.time()
    djk.print_results(cost, path)
    execution_time_ms = (end_time - start_time) * 1000
    print("Execution time: {} ms".format(execution_time_ms))

    print("==================================================================================================================")
    print("      ASTAR TIME CRITERION       ")
    print(f"Start stop: {START_STOP}, End Stop: {END_STOP}, Arrival time at start stop: {TIME}")
    start_time = time.time()
    distances, path = astar_time.astar(START_STOP, END_STOP, TIME, heuristic=astar_time.euclidean_distance)
    end_time = time.time()
    astar_changes.print_results(START_STOP, END_STOP, distances, path)
    execution_time_ms = (end_time - start_time) * 1000
    print("Execution time: {} ms".format(execution_time_ms))

    print("==================================================================================================================")
    print("      ASTAR LINE CHANGES CRITERION       ")
    print(f"Start stop: {START_STOP}, End Stop: {END_STOP}, Arrival time at start stop: {TIME}")
    start_time = time.time()
    distances, path = astar_changes.astar(START_STOP, END_STOP, TIME, heuristic=astar_changes.euclidean_distance)
    end_time = time.time()
    astar_changes.print_results(START_STOP, END_STOP, distances, path)
    execution_time_ms = (end_time - start_time) * 1000
    print("Execution time: {} ms".format(execution_time_ms))

