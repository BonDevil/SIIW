import csv

def load_graph(filename):
    # Create an empty dictionary to store the graph
    graph = {}
    # Open the CSV file and read its contents
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        # Iterate through each row of the CSV file
        for row in reader:
            # Extract the relevant fields from the row
            id = int(row['id'])
            company = row['company']
            line = str(row['line'])
            departure_time = row['departure_time']
            arrival_time = row['arrival_time']
            start_stop = str(row['start_stop']).strip()
            end_stop = str(row['end_stop']).strip()
            start_stop_lat = float(row['start_stop_lat'])
            start_stop_lon = float(row['start_stop_lon'])
            end_stop_lat = float(row['end_stop_lat'])
            end_stop_lon = float(row['end_stop_lon'])

            # Create an edge tuple
            edge = (id, company, line, departure_time, arrival_time, start_stop, end_stop, start_stop_lat, start_stop_lon, end_stop_lat, end_stop_lon)
            # Add the edge to the start node's list of neighboring edges
            if start_stop not in graph:
                graph[start_stop] = [edge]
            else:
                graph[start_stop].append(edge)
    # Return the graph dictionary
    graph['Żórawina - Niepodległości (Mostek)'] = None
    return graph