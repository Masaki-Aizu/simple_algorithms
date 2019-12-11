def find_lowest_node(cost):
    lowest_cost = float('inf')
    lowest_node = None
    for node in cost:
        cos = cost[node]
        if cos < lowest_cost and node not in processed:
            lowest_cost = cos
            lowest_node = node
    
    return lowest_node

graph = {}
graph['start'] = {'a':6, 'b':2 }
graph['a'] = {'fin':1}
graph['b'] = {'a':3, 'fin':5}
graph['fin'] = {}

infinity = float('inf')
cost = {'a':6, 'b':2, 'fin':infinity}
# print(type(cost['a']))

parent = {'a':'start', 'b':'start', 'fin':None}

processed = []

node = find_lowest_node(cost)

while node is not None:
    num = cost[node]
    neighbor = graph[node]
    for n in neighbor.keys():
        sum_cost = num + neighbor[n]
        if cost[n] > sum_cost:
            cost[n] = sum_cost
            parent[n] = node
    processed.append(node)
    node = find_lowest_node(cost)

print(parent)