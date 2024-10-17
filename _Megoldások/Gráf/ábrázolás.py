import random as r
from pyvis.network import Network

net = Network()  # create graph object

# add nodes
for i in range(10):
    net.add_node(i, label=str(i), color='#' + ''.join([r.choice('ABCDEF0123456789') for i in range(6)]))

for _ in range(30):
    net.add_edge(r.randint(0, 9), r.randint(0, 9))

node = 0
visited = [0]
queue = [node for edge in net.edges if edge['from'] == ]
while len(visited) < len(net.nodes) and
net.show('graph.html', notebook=False)  # save visualization in 'graph.html'
