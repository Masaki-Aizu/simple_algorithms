from collections import deque

def search(name):
    queue = deque()
    queue += graph[name]
    searched = []
    while queue:
        person = queue.popleft()
        if person not in searched:
            if person_seller(person):
                print(person + ' is a mango seller')
                return True
            else:
                queue += graph[person]
                searched.append(person)
    
    return False

def person_seller(person):
    return person[-1] == 'm'

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

search('you')