import networkx as nx
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)

G = nx.DiGraph()
G.add_edge(
    "$ax^2 + bx + c$", "$a(x - x_0)^2 + y_0$", label="Fullstendige kvadraters metode"
)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue")
nx.draw_networkx_edge_labels(
    G, pos, edge_labels={(u, v): d["label"] for u, v, d in G.edges(data=True)}
)

plt.show()
