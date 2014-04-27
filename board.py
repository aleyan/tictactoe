positions = set([n for n in xrange(1,10)])
wins = [ set([1,5,9]), set([3,5,7]),
         set([1,2,3]),set([4,5,6]),set([7,8,9]),
         set([1,4,7]),set([2,5,8]),set([3,6,9]) ]

class Board(object):
    xs = set()
    os = set()
    
    def __init__(self, pos):
        self.xs = set([int(n) for n in pos[::2]])
        self.os = set([int(n) for n in pos[1::2]])
    
    def make_move(self, move):
        if move not in self.moves_possible():
            raise Exception("Illegal Move: %s for %s" % (move, self.__repr__()))
        
        return Board("".join([str(n) for n in self.moves_made()]) + str(move))
    
    def whose_turn(self):
        """Returns whose turn it is to go.
        1   : X Turn
        -1  : O Turn
        """
        moves = len(self.xs)+len(self.os)
        return (moves%2)*-2+1
    
    def who_won(self):
        statuses = { self.has_win(win) for win in wins }
        if 1 in statuses:
            return 1
        elif -1 in statuses:
            return -1
        elif statuses==set([0]):
            return 0
        else:
            return None
        
                
    def has_win(self, win):
        """Checks if there is a win for a particular triplet:
            1   : X won
            -1  : O won
            0   : Draw
            None: Contested
            """
        if set(win).issubset(self.xs):
            return 1
        elif set(win).issubset(self.os):
            return -1
        elif set(win).issubset(self.os.union(self.xs)):
            return 0
        else:
            return None
    
    def moves_possible(self):
        return positions - set(self.moves_made())
                
    def moves_made(self):
        out = [None]*(len(self.xs)+len(self.os))
        out[::2] = sorted(self.xs)
        out[1::2] = sorted(self.os)
        return out 
    
    def __eq__(self, other):
        return self.xs==other.xs and self.os==other.os

    def __hash__(self):
        return ("".join([str(n) for n in self.moves_made()])).__hash__()
    
    def __repr__(self):
        #return( "Xs" + "".join([str(n) for n in self.xs]) + "\t\tOs" + "".join([str(n) for n in self.os]) )
        return( """Board("%s")""" % "".join([str(n) for n in self.moves_made()]) )
    
    def __str__(self):
        out = ""
        for row in xrange(3):
            for col in xrange(1,4):
                if (row*3+col) in self.xs:
                    out = out + 'X'
                elif (row*3+col) in self.os:
                    out = out + 'O'
                else:
                    out = out + ' '
            out = out + '\n'
        return out