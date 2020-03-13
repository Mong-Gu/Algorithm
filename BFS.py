# 너비우선탐색 - BFS(Breadth-First Search)

# 사전 준비물 : Vertex List, Edge List, Graph

# Vertex(정점) 리스트 선언
vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# Edge(간선) 리스트 선언
edgeList = [(0,1), (1,2), (1,3), (3,4), (4,5), (1,6)]
# Vertex와 Edge를 튜플로 묶어 그래프 선언
graphs = (vertexList, edgeList)

# -----------------------------------------------------------------------------------------------

# BFS 함수 정의 (허민석님의 소스코드)
def bfs1(graph, start):
    vertexList, edgeList = graph
    visitedList = []                                        # 방문한 Vertex를 체크하기 위한 리스트
    queue = [start]                                         # BFS는 큐를 사용하며, 시작점을 큐에 넣고 시작
    adjacencyList = [[] for vertex in vertexList]           # 한 정점과 인접한 정점을 담기 위한 이중리스트

    # 그래프로부터 인접리스트를 채우기
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    # 실질적인 BFS 알고리즘 동작 과정
    while queue:                                            # 0. 큐가 비어있지 않을 동안 반복을 실행하며
        current = queue.pop()                               # 1. 변수 current에 큐에서 dequeue한 값을 담기
        for neighbor in adjacencyList[current]:             
            if not neighbor in visitedList:                 # 2. current로 할당된 vertex와 인접한 vertex들을 큐에 enqueue
                queue.insert(0,neighbor)                    #    단, 이때 이미 방문했던 vertex라면 enqueue하지 않는다
        visitedList.append(current)                         # 3. 모든 인접 vertex를 enqueue했다면, current에 할당된 vertex를 방문리스트에 append
    return visitedList

# -----------------------------------------------------------------------------------------------

from collections import deque
# BFS 함수 정의 (collections.deque를 활용한 내 소스코드)
# 왜 굳이 collections의 deque를 사용한 것이냐?
# 허민석님의 코드에서는 queue에 enqueue할 때 list의 insert메서드를 쓰는데 이는 큐에 들어가있는 값의 개수 N에 비례하는 O(N)의 시간복잡도를 가지고 있음
# 허민석님이 insert를 쓰는 이유는 큐의 dequeue를 list의 pop메서드로 구현하고자 했기 때문임
# 하지만 collections.deque를 쓴다면 append할 때도 O(1)의 시간복잡도를, popleft할 때도 O(1)의 시간복잡도를 가지고 있음 
# 알고리즘 테스트 문제에서는 큐가 큰 영향을 줄 정도로 길어질 일이 없겠지만, 그래도 익숙해져놓으면 좋을 것이라 판단

def bfs2(graph, start):
    vertexList, edgeList = graph
    visitedList = []                                        # 방문한 Vertex를 체크하기 위한 리스트
    q = deque([start])                                      # BFS는 큐를 사용하며, 시작점을 큐에 넣고 시작
    adjacencyList = [[] for vertex in vertexList]           # 한 정점과 인접한 정점을 담기 위한 이중리스트

    # 간선리스트를 참고하여 인접리스트를 채우기
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    # 실질적인 BFS 알고리즘 동작 과정
    while q:                                                # 0. 큐가 비어있지 않을 동안 반복을 실행하며
        current = q.popleft()                               # 1. 변수 current에 큐에서 dequeue한 값을 담기
        for neighbor in adjacencyList[current]:             
            if not neighbor in visitedList:                 # 2. current로 할당된 vertex와 인접한 vertex들을 큐에 enqueue
                q.append(neighbor)                          #    단, 이때 이미 방문했던 vertex라면 enqueue하지 않는다
        visitedList.append(current)                         # 3. 모든 인접 vertex를 enqueue했다면, current에 할당된 vertex를 방문리스트에 append
    return visitedList

print(bfs1(graphs, 0))
print(bfs2(graphs, 0))

# 소스코드 : https://github.com/minsuk-heo/problemsolving/blob/master/graph/bfs.py
# 정말 혹시라도 보게 되실 허민석님에게 - 간단명료한 설명과 좋은 코드 항상 감사합니다, 허민석님.