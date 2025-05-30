import networkx as nx
graph = nx.read_gml("network.gml")
while True:
    source = input("Enter the source region: ")
    target = input("Enter the target region: ")
    path = nx.shortest_path(graph, source, target)
    print(path)