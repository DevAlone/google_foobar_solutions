# a queue built from scratch, just because of the bug which doesn't let me to import normal one
class Queue:
    def __init__(self, size):
        if size < 1:
            size = 1
        self.data = [None for i in range(size)]
        self.start_index = 0
        self.length = 0

    def empty(self):
        return self.length == 0

    def put(self, item):
        # self.data.append(item)
        if self.length >= len(self.data):
            self.resize()

        self.data[self.modulo(self.start_index + self.length, len(self.data))] = item
        self.length += 1

    def get(self):
        item = self.data[self.start_index]
        self.start_index = self.modulo(self.start_index + 1, len(self.data))
        self.length -= 1
        return item

    def resize(self):
        new_data = [None for i in range(len(self.data * 2))]
        for i in range(self.length):
            new_data[i] = self.data[(self.start_index + i) % len(self.data)]
        
        self.data = new_data
        self.start_index = 0

    def modulo(self, val, base):
        if base == 0:
            return val
        return val % base


def generate_all_knight_moves(src, board_size):
    def is_move_valid(move):
        return move[0] >= 0 and move[1] >= 0 \
                and move[0] < board_size[0] and move[1] < board_size[1]

    move = (src[0] + 2, src[1] + 1)
    if is_move_valid(move):
        yield move
    move = (src[0] + 2, src[1] - 1)
    if is_move_valid(move):
        yield move
    move = (src[0] - 2, src[1] + 1)
    if is_move_valid(move):
        yield move
    move = (src[0] - 2, src[1] - 1)
    if is_move_valid(move):
        yield move

    move = (src[0] + 1, src[1] + 2)
    if is_move_valid(move):
        yield move
    move = (src[0] - 1, src[1] + 2)
    if is_move_valid(move):
        yield move
    move = (src[0] + 1, src[1] - 2)
    if is_move_valid(move):
        yield move
    move = (src[0] - 1, src[1] - 2)
    if is_move_valid(move):
        yield move


def solution(src, dest):
    # (x, y, distance_from_the_beginning)
    src = (src % 8, src // 8, 0)
    dest = (dest % 8, dest // 8, 0)

    visited_nodes = set()
    q = Queue(8)
    q.put(src)

    # do bfs search
    while not q.empty():
        item = q.get()
        visited_nodes.add((item[0], item[1]))
        if item[0] == dest[0] and item[1] == dest[1]:
            return item[2]
        
        for move in generate_all_knight_moves(item, (8, 8)):
            if not move in visited_nodes:
                # increment the distance here
                q.put((move[0], move[1], item[2] + 1))

    # there is no path
    return -1


if __name__ == '__main__':
    print(solution(0, 1))
    print(solution(19, 36))

