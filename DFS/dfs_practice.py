# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited_set = set()

def dfs(node, visited_set, graph):
    if node not in visited_set:
        print("Visited: ", node)
        visited_set.add(node)
        for node in graph[node]:
            dfs(node, visited_set, graph)
    

start_node = '5'
dfs(start_node, visited_set, graph)