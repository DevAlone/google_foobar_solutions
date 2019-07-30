import sys
from collections import deque


def answer(nodes):
    start_node = (0, 0, 1)
    goal_node = (len(nodes) - 1, len(nodes[0]) - 1, 1)
    queue = deque([start_node])
    distance_map = {start_node: 1}

    def get_neighbors(node):
        result = []
        rows = len(nodes)
        columns = len(nodes[0])
        y = node[0]
        x = node[1]
        saldo = node[2]
        
        if x > 0:
            if nodes[y][x - 1] == 1:
                if saldo > 0:
                    result.append((y, x - 1, saldo - 1))
            else:
                result.append((y, x - 1, saldo))

        if x < columns - 1:
            if nodes[y][x + 1] == 1:
                if saldo > 0:
                    result.append((y, x + 1, saldo - 1))
            else:
                result.append((y, x + 1, saldo))

        if y > 0:
            if nodes[y - 1][x] == 1:
                if saldo > 0:
                    result.append((y - 1, x, saldo - 1))
            else:
                result.append((y - 1, x, saldo))

        if y < rows - 1:
            if nodes[y + 1][x] == 1:
                if saldo > 0:
                    result.append((y + 1, x, saldo - 1))
            else:
                result.append((y + 1, x, saldo))

        return result

    while queue:
        current_node = queue.popleft()

        if current_node[0] == goal_node[0] and current_node[1] == goal_node[1]:
            return distance_map[current_node]

        for neighbor_node in get_neighbors(current_node):
            if neighbor_node not in distance_map:
                distance_map[neighbor_node] = distance_map[current_node] + 1
                queue.append(neighbor_node)

    raise Exception("there isn't any path")


if __name__ == '__main__':
    nodes = [
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0],
    ]
    nodes1 = [
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0],
    ]
    nodes = [
        [0, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
    ]
    print answer(nodes)
    # start_node = (0, 0)
    # end_node = (len(nodes) - 1, len(nodes[0]) - 1)
    # result = find_path_a_star(nodes, start_node, end_node)
    # print result
