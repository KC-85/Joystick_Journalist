import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes (tables)
G.add_node("Genre", shape="box", style="filled", fillcolor="lightblue")
G.add_node("Game", shape="box", style="filled", fillcolor="lightgreen")
G.add_node("Review", shape="box", style="filled", fillcolor="lightcoral")

# Add relationships (foreign keys)
G.add_edge("Genre", "Game", label="1 → many")
G.add_edge("Game", "Review", label="1 → many")

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightgray", font_size=10, edge_color="gray")
edge_labels = nx.get_edge_attributes(G, "label")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

# Save ER diagram as an image
plt.savefig("erd_diagram.png")  # Save to file
print("✅ ER Diagram saved as 'erd_diagram.png'")  # Notify user
