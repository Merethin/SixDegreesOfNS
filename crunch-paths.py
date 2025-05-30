import networkx as nx
import time, itertools

def allShortestPaths(gml, output):
    graph = nx.read_gml(gml)

    all_nodes = list(graph)
    processed = 0
    total_to_process = len(all_nodes)
    start = time.time()

    with open(output, "w+") as output_file:
        for batch in itertools.batched(all_nodes, 1000):
            for source in batch:
                for target, length in nx.single_source_shortest_path_length(graph, source).items():
                    output_file.write(f"[{length}] | {source} - {target}\n")
            processed += len(batch)
            current = time.time()
            print(f"{processed} regions computed out of {total_to_process} in {current-start} seconds")
            estimated_time_left = ((total_to_process-processed)/processed) * (current-start)
            print(f"Estimated time left: {estimated_time_left} seconds")