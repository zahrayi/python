INF = 99999

def floydWarshall(graph, V):

    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(V):
        for i in range(V):
            for j in range(V):

                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def printSolution(dist, V):
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print(dist[i][j], end=" ")
        print()


if __name__ == "__main__":

    N = int(input())


    graph = []
    for i in range(N):
        row = list(map(lambda x: INF if x == "INF" else int(x), input().split()))
        graph.append(row)

    result = floydWarshall(graph, N)


    printSolution(result, N)
