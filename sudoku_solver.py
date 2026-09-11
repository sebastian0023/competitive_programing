class Solution(object):
    def solveSudoku(self, board):
        # creamos sets para guardar valores unicos y aseguramos que no se repitan
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # recorremos el tablero para ver que existe y que no
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    b_idx = (r // 3) * 3 + (c // 3) # calculamos en que subtabla estamos
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[b_idx].add(val)
                else:
                    empty_cells.append((r, c))

        # hacemos el backtrackng con la celdas acias que ya habiamos guardado
        def backtrack(index):
            if index == len(empty_cells):
                return True

            r, c = empty_cells[index]
            b_idx = (r // 3) * 3 + (c // 3)

            for num in range(1, 10):
                val = str(num)
                if val not in rows[r] and val not in cols[c] and val not in boxes[b_idx]:
                    # aqui colocamos el valor y actualizamos nuestros sets
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[b_idx].add(val)

                    if backtrack(index + 1):
                        return True

                    # si no funciona hacemos backtrack y quitamos el valor que habiamos colocado
                    board[r][c] = '.'
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[b_idx].remove(val)

            return False

        backtrack(0)