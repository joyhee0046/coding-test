# import sys
# sys.stdin = open("input.txt", "r")


# #리스트로 풀기
#
# def in_order(node) :
#     if node :
#         in_order(data[node][2]) #left
#         print(data[node][1], end="")
#         in_order(data[node][3]) #right
#
#
# for tc in range(1,11):
#     N = int(input())
#     data = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]
#     # 람다 안쓰고 입력받기
#     # data = [list(input().split()) for _ in range(N)]
#     # for i in range(N):
#     #     for j in range(len(data[i])):
#     #         if data[i][j].isdecimal():
#     #             data[i][j] = int(data[i][j])
#     for arr in data :
#         while len(arr) != 4:   #입력 길이 맞추려고
#             arr.append(0)
#
#     data.insert(0, [0,0,0,0])
#     print(f"#{tc}", end=' ')
#     in_order(1)
#     print()


# #남의 특강
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# def inorder(node):
#     global ans
#     if node.left:
#         inorder(tree[node.left])
#     ans += node.data
#     if node.right:
#         inorder(tree[node.right])
#
# result = []
# for case in range(1, 10 + 1):
#     ans = ""
#     N = int(input())
#     tree = {0: Node}
#
#     for _ in range(N):
#         arr = list(input().split())
#         tree[int(arr[0])] = Node(arr[1])
#
#         if len(arr) > 2:
#             tree[int(arr[0])].left = int(arr[2])
#             if len(arr) > 3:
#                 tree[int(arr[0])].right = int(arr[3])
#
#     inorder(tree[1])
#     result.append(f"#{case} {ans}")
#
# for r in result:
#     print(r)


#
# def tree_search(node_num, value, left=None, right=None):
#     result = ''
#     # if len(tree_dict[node_num]) == 3:
#     if left:
#         # 왼쪽 노드
#         result += tree_search(node_num * 2, *tree_dict[node_num * 2])
#         # 현재 노드
#         result += value[0]
#         if right:
#             # 오른쪽 노드
#             result += tree_search(node_num * 2 + 1, *tree_dict[node_num * 2 + 1])
#     # 자식 노드가 없다면
#     else:
#         result += value[0]
#     return result
#
# for tc in range(1, 11):
#     n = int(input())
#
#     tree_dict = {i: input().split()[1:] for i in range(1, n + 1)}
#     #딕셔너리 입력받기
#     data = {}
#     for _ in range(N):
#         temp = list(map(lambda x: int(x) if x.isdecimal() else x, input().split()))
#         data.temp[0] = temp[1:]
#
#     result = tree_search(1, *tree_dict[1])
#     print(f"#{tc} {result}")
#


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def tree_search(node_num, value, left=None, right=None):
    result = ''
    # if len(tree_dict[node_num]) == 3:
    if left:
        # 왼쪽 노드
        result += tree_search(node_num * 2, *tree_dict[node_num * 2])
        # 현재 노드
        result += value[0]
        if right:
            # 오른쪽 노드
            result += tree_search(node_num * 2 + 1, *tree_dict[node_num * 2 + 1])
    # 자식 노드가 없다면
    else:
        result += value[0]
    return result

for tc in range(1, 11):
    n = int(input())

    tree_dict = {i: input().split()[1:] for i in range(1, n + 1)}

    result = tree_search(1, *tree_dict[1])
    print(f"#{tc} {result}")



# #트리로 풀기
# # 노드 만들기. 값은 무조건 있어야 하고, l.r은 있으면 추가
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
# #중위순회로 탐색해서 왼자식 탐색 완료한 부모노드부터 하나씩 출력
# def inorder_root(root):
#     if root.left:
#         inorder_root(data[root.left])
#     print(data[root.value], end="")
#     if root.right:
#         inorder_root(data[root.right])
# #테케 10가지
# for tc in range(1, 11):
#     N = int(input())
#     # 입력을 딕셔너리형태로 정리하기
#     data = []
#     for _ in range(N):
#         temp = list(map(lambda x: int(x) if x.isdecimal() else x, input().split()))
#         while len(temp) != 4:   #입력길이 모두 4자리로 맞추기
#             temp.append(0)
#         data.append(temp[0] = Node(temp[1])
#         data[temp[0]].left = temp[2]
#         data[temp[0]].right = temp[3]
#     #print(data)
#
#     inorder_root(data)
#
#     print(f"#{tc} {ans}")