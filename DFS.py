# 깊이우선탐색 - DFS(Depth-First Search)

# 사전 준비물 : Vertex List, Edge List, Graph

# Vertex(정점) 리스트 선언
vertexList = ['0', '1', '2', '3', '4', '5', '6']
# Edge(간선) 리스트 선언
edgeList = [(0,1), (0,2), (1,0) , (1,3) , (2,0) , (2,4) , (2,5) , (3,1), (4,2) , (4,6), (5,2), (6,4)]
# Vertex와 Edge를 튜플로 묶어 그래프 선언
graphs = (vertexList, edgeList)

# -----------------------------------------------------------------------------------------------

# DFS 함수 정의 (허민석님의 소스코드)
def dfs(graph, start):
    vertexList, edgeList = graph
    visitedVertex = []                                  # 방문한 Vertex를 체크하기 위한 리스트
    stack = [start]                                     # DFS는 스택을 사용하며, 시작점을 스택에 넣고 시작
    adjacencyList = [[] for vertex in vertexList]       # 한 정점과 인접한 정점을 담기 위한 이중리스트

    # 간선리스트를 참고하여 인접리스트를 채우기
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    # 실질적인 DFS 알고리즘 동작 과정
    while stack:                                        # 0. 스택이 비어있지 않을 동안 반복을 실행하며
        current = stack.pop()                           # 1. 변수 current에 스택에서 pop한 값을 담기
        for neighbor in adjacencyList[current]:         
            if not neighbor in visitedVertex:           # 2. current로 할당된 vertex와 인접한 vertex들을 스택에 push
                stack.append(neighbor)                  #    단, 이때 이미 방문했던 vertex라면 push하지 않는다
        visitedVertex.append(current)                   # 3. 모든 인접 vertex를 push했다면, current에 할당된 vertex를 방문리스트에 append
    return visitedVertex

print(dfs(graphs, 0))

# 소스코드 : https://github.com/minsuk-heo/problemsolving/blob/master/graph/dfs.py
# 정말 혹시라도 보게 되실 허민석님에게 - 간단명료한 설명과 좋은 코드 항상 감사합니다, 허민석님.