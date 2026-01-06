import chess
import chess.engine

board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
engine = chess.engine.SimpleEngine.popen_uci(r"C:\Users\OmeN_HP\Desktop\stockfish-windows-x86-64-avx2\stockfish\stockfish-windows-x86-64-avx2.exe")


def board_to_fen(board):
    fen_rows = []
    for row in board:
        empty_count = 0
        fen_row = ""
        for cell in row:
            if cell == ".":
                empty_count += 1
            else:
                if empty_count > 0:
                    fen_row += str(empty_count)
                    empty_count = 0
                fen_row += cell
        if empty_count > 0:
            fen_row += str(empty_count)
        fen_rows.append(fen_row)
    return "/".join(fen_rows) + " w - - 0 1"  

fen_string = board_to_fen(board)
print(fen_string)


board_st = chess.Board()
board_st.set_fen(fen_string)
best_move = engine.play(board_st, chess.engine.Limit(time=2))

print(best_move)