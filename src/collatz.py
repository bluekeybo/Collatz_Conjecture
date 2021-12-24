import networkx as nx

for nodes in [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
    edges = set()
    for i in range(2, nodes):
        n = m = i
        while n > 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1
            tup = (int(m), int(n))
            if tup in edges:
                break
            else:
                edges.add(tup)
            m = n

    G = nx.DiGraph()
    G.add_nodes_from([(1, {"color": "red"})])
    G.add_edges_from(edges)
    p = nx.drawing.nx_pydot.to_pydot(G)
    p.write_svg(f"collatz_{nodes}.svg")
