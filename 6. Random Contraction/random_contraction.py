import random


def load_graph(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = list(map(int, line.split()))
            vertex = parts[0]
            edges = parts[1:]
            graph[vertex] = edges
    return graph


def choose_random_edge(graph):
    v1 = random.choice(list(graph.keys()))
    v2 = random.choice(graph[v1])
    return v1, v2


def contract_edge(graph, v1, v2):
    graph[v1].extend(graph[v2])

    for vertex in graph[v2]:
        graph[vertex] = [v1 if x == v2 else x for x in graph[vertex]]

    graph[v1] = [x for x in graph[v1] if x != v1]
    del graph[v2]


def karger_min_cut(graph):
    while len(graph) > 2:
        v1, v2 = choose_random_edge(graph)
        contract_edge(graph, v1, v2)

    remaining_edges = list(graph.values())[0]
    return len(remaining_edges)


def run_karger_algorithm(file_path, iterations):
    min_cut = -1
    for _ in range(iterations):
        graph = load_graph(file_path)
        cut = karger_min_cut(graph)
        if min_cut == -1 or cut < min_cut:
            min_cut = cut
    return min_cut


if __name__ == "__main__":
    file_path = 'kargerMinCut.txt'
    iterations = 100
    res = run_karger_algorithm(file_path, iterations)
    print(res)
