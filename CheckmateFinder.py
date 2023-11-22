board_file = input()
opponent_file = input()

pieces = open(board_file)
opponent = open(opponent_file)
horizontal = "abcdefgh"
vertical = "12345678"
board = dict()
for h in horizontal:                        #built the board
    for v in vertical:
        board[h+v] = "00"
line = pieces.readline()
color = line[:-1]                           #got the color
if color == "white":
    opp_king = "BK"
    our_king = "WK"
else:
    opp_king = "WK"
    our_king = "BK"
while line != "":
    line = pieces.readline()
    if line != "":
        line_els = line.split()
        board[line_els[1]] = line_els[0]    #pieces are placed
def valid_moves_list(piece,board,position):
    lst = []
    h = position[0]
    v = position[1]
    if piece[1] == "K":
        if board.get(chr(ord(h)+1)+v , piece[0])[0] != piece[0]: #checking square on right
            lst.append(chr(ord(h)+1)+v)
        if board.get(chr(ord(h)+1) + str((int(v)+1)) , piece[0])[0] != piece[0]: #up-right
            lst.append(chr(ord(h)+1) + str((int(v)+1)))
        if board.get(chr(ord(h)+1) + str((int(v) - 1)), piece[0])[0] != piece[0]: #down-right
            lst.append(chr(ord(h)+1) + str((int(v) - 1)))
        if board.get(chr(ord(h)) + str((int(v) + 1)), piece[0])[0] != piece[0]: #up
            lst.append(chr(ord(h)) + str((int(v) + 1)))
        if board.get(chr(ord(h)) + str((int(v) - 1)), piece[0])[0] != piece[0]: #down
            lst.append(chr(ord(h)) + str((int(v) - 1)))
        if board.get(chr(ord(h)-1) + str((int(v))), piece[0])[0] != piece[0]: #left
            lst.append(chr(ord(h)-1) + str((int(v))))
        if board.get(chr(ord(h)-1) + str((int(v) + 1)), piece[0])[0] != piece[0]: #up-left
            lst.append(chr(ord(h)-1) + str((int(v) + 1)))
        if board.get(chr(ord(h)-1) + str((int(v) - 1)), piece[0])[0] != piece[0]: #down-left
            lst.append(chr(ord(h)-1) + str((int(v) - 1)))
    if piece[1] == "Q":
        x,y = (1,1)
        while True:   #right check
            check_pos = chr(ord(h)+x)+v
            if board.get(check_pos) == "00":
                lst.append(check_pos)
                x += 1
            else:
                if board.get(check_pos,piece[0])[0] != piece[0]:
                    lst.append(check_pos)
                break
        x, y = (1, 1)
        while True:  # down
            check_pos = chr(ord(h)) + str((int(v) - y))
            if board.get(check_pos) == "00":
                lst.append(check_pos)
                y += 1
            else:
                if board.get(check_pos, piece[0])[0] != piece[0]:
                    lst.append(check_pos)
                break
        x, y = (1, 1)
        while True: #up-right
            check_pos = chr(ord(h)+x) + str((int(v)+y))
            if board.get(check_pos) == "00":
                lst.append(check_pos)
                x+=1
                y+=1
            else:
                if board.get(check_pos,piece[0])[0] != piece[0]:
                    lst.append(check_pos)
                break
        x, y = (1, 1)
        while True: #down-right
            check_pos = chr(ord(h)+x) + str((int(v) - y))
            if board.get(check_pos) == "00":
                lst.append(check_pos)
                x+=1
                y+=1
            else:
                if board.get(check_pos,piece[0])[0] != piece[0]:
                    lst.append(check_pos)
                break
        x, y = (1, 1)
        while True: #up
            check_pos = chr(ord(h)) + str((int(v) + y))
            if board.get(check_pos) == "00":
                lst.append(check_pos)
                y += 1
            else:
                if board.get(check_pos,piece[0])[0] != piece[0]:
                    lst.append(check_pos)
                break
        x, y = (1, 1)
        while True: #left
            check_pos = chr(ord(h)-x) + str((int(v)))
            if board.get(check_pos) == "00":
                lst.append(check_pos)
                x += 1
            else:
                if board.get(check_pos,piece[0])[0] != piece[0]:
                    lst.append(check_pos)
                break
        x, y = (1, 1)
        while True: #up-left
            check_pos = chr(ord(h)-x) + str((int(v) + y))
            if board.get(check_pos) == "00":
                lst.append(check_pos)
                x+=1
                y+=1
            else:
                if board.get(check_pos,piece[0])[0] != piece[0]:
                    lst.append(check_pos)
                break
        x, y = (1, 1)
        while True: #down-left
            check_pos = chr(ord(h)-x) + str((int(v) - y))
            if board.get(check_pos) == "00":
                lst.append(check_pos)
                x+=1
                y+=1
            else:
                if board.get(check_pos,piece[0])[0] != piece[0]:
                    lst.append(check_pos)
                break
    if piece[1] == "B":
        x, y = (1, 1)
        while True:  # up-right
            check_pos = chr(ord(h) + x) + str((int(v) + y))
            if board.get(check_pos) == "00":
                lst.append(check_pos)
                x += 1
                y += 1
            else:
                if board.get(check_pos, piece[0])[0] != piece[0]:
                    lst.append(check_pos)
                break
        x, y = (1, 1)
        while True:  # up-left
            check_pos = chr(ord(h) - x) + str((int(v) + y))
            if board.get(check_pos) == "00":
                lst.append(check_pos)
                x += 1
                y += 1
            else:
                if board.get(check_pos, piece[0])[0] != piece[0]:
                    lst.append(check_pos)
                break
        x, y = (1, 1)
        while True:  # down-right
            check_pos = chr(ord(h) + x) + str((int(v) - y))
            if board.get(check_pos) == "00":
                lst.append(check_pos)
                x += 1
                y += 1
            else:
                if board.get(check_pos, piece[0])[0] != piece[0]:
                    lst.append(check_pos)
                break
        x, y = (1, 1)
        while True:  # down-left
            check_pos = chr(ord(h) - x) + str((int(v) - y))
            if board.get(check_pos) == "00":
                lst.append(check_pos)
                x += 1
                y += 1
            else:
                if board.get(check_pos, piece[0])[0] != piece[0]:
                    lst.append(check_pos)
                break
    if piece[1] == "N":
        if board.get(chr(ord(h)+1)+str(int(v)+2), piece[0])[0] != piece[0]:
            lst.append(chr(ord(h)+1)+str(int(v)+2))
        if board.get(chr(ord(h)+1)+str(int(v)-2), piece[0])[0] != piece[0]:
            lst.append(chr(ord(h)+1)+str(int(v)-2))
        if board.get(chr(ord(h)-1)+str(int(v)+2), piece[0])[0] != piece[0]:
            lst.append(chr(ord(h)-1)+str(int(v)+2))
        if board.get(chr(ord(h)-1)+str(int(v)-2), piece[0])[0] != piece[0]:
            lst.append(chr(ord(h)-1)+str(int(v)-2))
        if board.get(chr(ord(h)+2)+str(int(v)+1), piece[0])[0] != piece[0]:
            lst.append(chr(ord(h)+2)+str(int(v)+1))
        if board.get(chr(ord(h)+2)+str(int(v)-1), piece[0])[0] != piece[0]:
            lst.append(chr(ord(h)+2)+str(int(v)-1))
        if board.get(chr(ord(h)-2)+str(int(v)+1), piece[0])[0] != piece[0]:
            lst.append(chr(ord(h)-2)+str(int(v)+1))
        if board.get(chr(ord(h)-2)+str(int(v)-1), piece[0])[0] != piece[0]:
            lst.append(chr(ord(h)-2)+str(int(v)-1))
    if piece[1] == "R":
        x, y = (1, 1)
        while True:  # right check
            check_pos = chr(ord(h) + x) + v
            if board.get(check_pos) == "00":
                lst.append(check_pos)
                x += 1
            else:
                if board.get(check_pos, piece[0])[0] != piece[0]:
                    lst.append(check_pos)
                break
        x, y = (1, 1)
        while True:  # left
            check_pos = chr(ord(h) - x) + str((int(v)))
            if board.get(check_pos) == "00":
                lst.append(check_pos)
                x += 1
            else:
                if board.get(check_pos, piece[0])[0] != piece[0]:
                    lst.append(check_pos)
                break
        x, y = (1, 1)
        while True:  # up
            check_pos = chr(ord(h)) + str((int(v) + y))
            if board.get(check_pos) == "00":
                lst.append(check_pos)
                y += 1
            else:
                if board.get(check_pos, piece[0])[0] != piece[0]:
                    lst.append(check_pos)
                break
        x, y = (1, 1)
        while True:  # down
            check_pos = chr(ord(h)) + str((int(v) - y))
            if board.get(check_pos) == "00":
                lst.append(check_pos)
                y += 1
            else:
                if board.get(check_pos, piece[0])[0] != piece[0]:
                    lst.append(check_pos)
                break
    if piece[1] == "P":
        if piece[0] == "W": #FOR WHITE PAWNS
            if v == "2" and board.get(h+str(int(v)+2)) == "00" and board.get(h+str(int(v)+1)) == "00": #pawn's opening special
                lst.append(h+str(int(v)+2))
            if board.get(h+str(int(v)+1)) == "00": #up
                lst.append(h+str(int(v)+1))
            if board.get(chr(ord(h)+1)+str(int(v)+1) , "e")[0] == "B":   #up-right capturing
                lst.append(chr(ord(h)+1)+str(int(v)+1))
            if board.get(chr(ord(h) - 1) + str(int(v) + 1), "e")[0] == "B": #up-left capturing
                lst.append(chr(ord(h) - 1) + str(int(v) + 1))
        if piece[0] == "B": #FOR BLACK PAWNS
            if v == "7" and board.get(h+str(int(v)-2)) == "00" and board.get(h+str(int(v)-1)) == "00": #pawn's opening special
                lst.append(h+str(int(v)-2))
            if board.get(h+str(int(v)-1)) == "00": #down
                lst.append(h+str(int(v)-1))
            if board.get(chr(ord(h)+1)+str(int(v)-1) , "e")[0] == "W":   #down-right capturing
                lst.append(chr(ord(h)+1)+str(int(v)-1))
            if board.get(chr(ord(h) - 1) + str(int(v) - 1), "e")[0] == "W": #down-left capturing
                lst.append(chr(ord(h) - 1) + str(int(v) - 1))
    return lst
def is_in_check(piece,board):
    for pos,pie in board.items():
        if pie == piece:
            king_position = pos
            break
    for pos,pie in board.items():
        if pie[0] != piece[0]:
            for square in valid_moves_list(pie,board,pos):
                if square == king_position:
                    return True
    return False
def board_after_move(board,prepos,newpos):
    global color
    boa = board.copy()
    piece = boa[prepos]
    boa[prepos] = "00"
    boa[newpos] = piece
    return boa
sol=[]
checkmate = False
def solution(board,our_moves=["x"]):
    global color
    global checkmate
    before_move = opponent.tell()
    if our_moves == ["x"]:
        our_moves = [(pos_i,pos_f) for pos_i,pie in board.items() if pie[0].lower() == color[0] for pos_f in valid_moves_list(pie,board,pos_i)]
    if our_moves == []:
        return
    opp_moves = []
    pre,new = our_moves[0]
    new_board = board_after_move(board,pre,new)         #board after our possible move
    try:
        if is_in_check(our_king,new_board):
            solution(board,our_moves[1:])
            return
    except:
        pass
    for pos,pie in new_board.items():
        if (pie[0] == "B" and color == "white") or (pie[0] == "W" and color == "black"):
            for move in valid_moves_list(pie,new_board,pos):
                if not is_in_check(opp_king,board_after_move(new_board,pos,move)):
                    opp_moves.append(f"{pos} {move}")
    if opp_moves == [] and is_in_check(opp_king,new_board):   #checkmate
        checkmate = True
        sol.append(f"{pre} {new}")
        return
    target = opponent.readline().strip().split(",")
    try:
        opponent_initial,opponent_final = target[0].split()
    except:
        pass
    if sorted(opp_moves) == sorted(target) and opp_moves != []:  #covers last move stalemate
        sol.append(f"{pre} {new}")
        new_new_board = board_after_move(new_board,opponent_initial,opponent_final)
        solution(new_new_board)
    else:
        opponent.seek(before_move)
        solution(board, our_moves[1:])
        return
    if not checkmate:
        sol.pop()
        opponent.seek(before_move)
        solution(board, our_moves[1:])
solution(board)
for i in sol:
    print(i)

