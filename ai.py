import board

def memoize(f):
    class memodict(dict):
        def __missing__(self, key):
            self[key] = ret = f(key)
            return ret
    return memodict().__getitem__


def is_better(old, new, turn):    
    if old==None:
        return True
    if (cmp(new[0], old[0]) * turn)==1:
        return True
    elif new[0]==old[0] and ( (new[0]==turn  and new[1]<old[1])
                             or (new[0]!=turn  and new[1]>=old[1])):
        return True
    else:
        return False
        
@memoize
def evaluate(board):
    """Returns the triplet of values:
    first val : best minimax outcome
    second val: how many moves to achieve it
    third val : what is the best move to make
    """
    who_won = board.who_won()
    if who_won != None:
        return who_won, 0, None
    moves = board.moves_possible()
    if len(moves)==0:
        return 0, 0, None
    best_move = None
    best_outcome = None
    turn = board.whose_turn()
    
    for move in moves:
        outcome = evaluate(board.make_move(move))
        outcomes.append((move,outcome))
        if is_better( best_outcome, outcome, turn):
            best_outcome = outcome
            best_move = move
    return best_outcome[0], best_outcome[1]+1, best_move