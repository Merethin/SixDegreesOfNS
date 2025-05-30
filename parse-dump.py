import xml.etree.ElementTree as ET
import networkx as nx
import typing

def parseRegionData(filename: str, exclude_list: typing.List[str]):
    tree = ET.parse(filename)
    root = tree.getroot()

    regions = []
    embassies = []

    for region in root.findall("./REGION"):
        name = region.find("NAME")
        if(name.text in exclude_list):
            print(f"Skipped {name.text}")
            continue

        embassy_list = []

        for child in region.find("EMBASSIES"):
            if(child.text in exclude_list):
                print(f"Skipped embassy {child.text}")
                continue
            if("type" in child.attrib.keys()):
                if(child.attrib["type"] in ["denied", "requested", "rejected", "pending", "invited"]):
                    print(f"Embassy between {name.text} and {child.text} skipped because it's {child.attrib["type"]}.")
                    continue
            embassy_list.append(child.text)

        regions.append(name.text)
        embassies.append((name.text, embassy_list))

    return (regions, embassies)

def generateEmbassyGraph(regions, embassies) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(regions)

    for region in embassies:
        name = region[0]
        embassy_list = region[1]

        for embassy in embassy_list:
            graph.add_edge(name, embassy)

    print(f"Number of regions: {graph.number_of_nodes()}")
    print(f"Number of embassies: {graph.number_of_edges()}")

    return graph

exclude_file = open("exclude.txt")
exclude_list = [region.rstrip() for region in exclude_file.readlines()]
print(f"Skipping the following regions: {exclude_list}")
(regions, embassies) = parseRegionData("regions.xml", exclude_list)
graph = generateEmbassyGraph(regions, embassies)
nx.write_gml(graph, "network.gml")