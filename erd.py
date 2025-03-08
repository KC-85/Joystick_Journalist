import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define tables and their attributes
tables = {
    "Genre": ["id (PK)", "name"],
    "Game": ["id (PK)", "title", "release_year", "genre_id (FK -> Genre.id)"],
    "Review": ["id (PK)", "game_id (FK -> Game.id)", "reviewer_name", "rating", "comment", "review_date"],
}

# Add nodes (tables)
for table, attributes in tables.items():
    G.add_node(table, label=f"{table}\n" + "\n".join(attributes))

# Add relationships (foreign keys)
relationships = [
    ("Game", "Genre"),  # Game.genre_id -> Genre.id
    ("Review", "Game"),  # Review.game_id -> Game.id
]

for src, dest in relationships:
    G.add_edge(src, dest, label="FK")

# Draw the graph
plt.figure(figsize=(8, 5))
pos = nx.spring_layout(G, seed=42)  # Position nodes using a layout
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=3000, font_size=10, font_weight="bold")
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, font_color="red")

# Show the diagram
plt.title("Entity-Relationship Diagram for Joystick Journalist")
plt.show()
