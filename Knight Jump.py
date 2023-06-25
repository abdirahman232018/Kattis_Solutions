def bfs(kPosition, goal, board, N):
    validPositions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    queue = []
    queue.append((kPosition, 0))
    visited = {kPosition}
    while queue:
        cur_pos, moves = queue.pop(0)
        if cur_pos == goal:
            return moves
        x, y = cur_pos
        for x1, y1 in validPositions:
            nextX, nextY = (x + x1, y + y1)
            if 0 <= nextX < N and 0 <= nextY < N and board[nextX][nextY] != '#' and (nextX, nextY) not in visited:
                queue.append(((nextX, nextY), moves + 1))
                visited.add((nextX, nextY))
    return -1


def findK(board):
    return board[-1].find('K')


kFound = False
N = int(input())
board = []
k = (0, 0)
for x in range(N):
    board.append(input())
    if not kFound:
        y = findK(board)
        if y != -1:
            k = (x, y)
            kFound = True
print(bfs(k, (0, 0), board, N))
