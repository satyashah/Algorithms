# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}


visited = set()
queue = []

def bfs(start, graph):
    visited.add(start)
    queue.append(start)

    while queue:
        m = queue.pop(0)
        print(m, end = " ")

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

start = '5'
bfs(start, graph)

