"""CSC111 Project: Job Recommendation System Visualization

Module Description
==================
This module visualizes the job-skill graph.

Copyright and Usage Information
===============================
This file is Copyright (c) 2025 CSC111 Teaching Team.
"""

import networkx as nx
import plotly.graph_objs as go
import project_2_pt_1


def visualize_graph(graph: project_2_pt_1.Graph) -> None:
    """Visualize the job-skill graph."""
    G = nx.Graph()

    for item, vertex in graph._vertices.items():
        G.add_node(item)
        for neighbor in vertex.neighbours:
            G.add_edge(item, neighbor.item, weight=vertex.weight[neighbor.item])

    pos = nx.spring_layout(G)

    edges = [(edge[0], edge[1], G.edges[edge]['weight']) for edge in G.edges]

    edge_traces = []
    for edge in edges:
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        weight = edge[2]

        edge_traces.append(go.Scatter(
            x=[x0, x1],
            y=[y0, y1],
            line=dict(width=weight / 2, color='gray'),
            mode='lines'
        ))

    node_trace = go.Scatter(
        x=[pos[node][0] for node in G.nodes],
        y=[pos[node][1] for node in G.nodes],
        mode='markers+text',
        text=[node for node in G.nodes],
        textposition="top center",
        marker=dict(size=10, color="blue")
    )

    fig = go.Figure(data=edge_traces + [node_trace])
    fig.show()


# Example Usage
if __name__ == "__main__":
    graph = project_2_pt_1.Graph()

    # Add job and skill nodes
    graph.add_vertex("Software Engineer")
    graph.add_vertex("Data Scientist")
    graph.add_vertex("Python")
    graph.add_vertex("Machine Learning")

    # Add edges with weights
    graph.add_edge("Software Engineer", "Python", 8)
    graph.add_edge("Data Scientist", "Python", 9)
    graph.add_edge("Data Scientist", "Machine Learning", 10)

    visualize_graph(graph)
