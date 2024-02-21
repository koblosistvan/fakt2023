import graphviz
edges = [
    ["A", "B", 3],
    ["A", "C", 5],
    ["B", "D", 3],
    ["B", "E", 4],
    ["B", "C", 1],
    ["C", "D", 1],
    ["D", "E", 1],
    ["D", "G", 7],
    ["D", "F", 4],
    ["E", "G", 4],
    ["F", "G", 2]
]
distance = {}
came_from = {}

g = graphviz.Digraph()
for edge in edges:
    source, target, weight = edge
    g.edge(source, target, label=str(weight))

def calc_distance(start):
    # készítünk egy egyedi listát a csúcsokról
    nodes_to_check = []
    for edge in edges:
        if edge[0] not in nodes_to_check:
            nodes_to_check.append(edge[0])
        if edge[1] not in nodes_to_check:
            nodes_to_check.append(edge[1])
    # minden csúcsra beállítjuk a kezdőértéket: távolság=1000, honnan=None
    for node in nodes_to_check:
        distance[node] = 1000
        came_from[node] = None
    # a kezdő csúcs távolsága 0
    distance[start] = 0
    # ő lesz a vizsgált csúcs
    actual_node = start
    # kivesszük a vizsgálandók közül
    nodes_to_check.remove(start)
    # számolunk, amíg van még vizsgálandó csúcs
    while len(nodes_to_check) > 0:
        # meghatározzuk a vizsgált csúcsból kimenőú éleket
        edges_to_check = [edge for edge in edges if edge[0] == actual_node]
        # minden élre
        for edge in edges_to_check:
            # ha innen közelebb van a végpont, mint ahogy eddig tudtuk, akkor módosítjuk
            source, target, weight = edge
            if distance[actual_node] + edge[2] < distance[target]:
                # a honnan érhető el az aktuális csúcs lesz
                came_from[target] = actual_node
                # a távolság az aktuális távolsága + az él súlya
                distance[target] = distance[actual_node] + weight
        # megkeressük a legkisebb távolságú csúcsot, ő lesz az új vizsgált
        min_distance_node = nodes_to_check[0]
        for node in nodes_to_check:
            if distance[node] < distance[min_distance_node]:
                min_distance_node = node
        actual_node = min_distance_node
        remaining_distance = {k: v for k, v in distance.items() if k in nodes_to_check}
        # őt is kivesszük a vizsgálandók közül
        nodes_to_check.remove(actual_node)

def print_route(target):
    route = target

    while came_from[target] != None:
        g.edge(came_from[target], target, color='red')
        route = came_from[target] + ' - ' + route
        target = came_from[target]
    print(route)

calc_distance('A')
print_route('F')

print(g.source)