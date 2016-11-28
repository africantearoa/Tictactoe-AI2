### Start with X or O. Input moves as numbers 0-8
import random

example_code=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

class Board:
    def __init__(self,code):
        self.code=code
    
    def print_board(self,code):
        print("Current board")
        print(code[0],' | ',code[1],' | ',code[2])
        print('---+-----+---')
        print(code[3],' | ',code[4],' | ',code[5])
        print('---+-----+---')
        print(code[6],' | ',code[7],' | ',code[8])
    
    def add_move(self,code,move,team):
        code[int(move)]=str(team)
    
    def check_end(self,code):
        for x in 'XO':
            if code[0]==x and code[1]==x and code[2]==x:
                return True,x      
            elif code[3]==x and code[4]==x and code[5]==x:
                return True,x
            elif code[6]==x and code[7]==x and code[8]==x:
                return True,x
            elif code[0]==x and code[3]==x and code[6]==x:
                return True,x
            elif code[1]==x and code[4]==x and code[7]==x:
                return True,x
            elif code[2]==x and code[5]==x and code[8]==x:
                return True,x        
            elif code[0]==x and code[4]==x and code[8]==x:
                return True,x  
            elif code[2]==x and code[4]==x and code[6]==x:
                return True,x          
            ###Draw
            elif code[0]!=' ' and code[1]!=' ' and code[2]!=' ' and code[3]!=' ' and code[4]!=' ' and code[5]!=' ' and code[6]!=' ' and code[7]!=' ' and code[8]!=' ':
                return True,None
        return False,x
    

def next_move_moderate(code,ai_team):
    board=Board(code)
    def dfs(code,team,node):
        over,winner=board.check_end(code)
        if over:
            if winner==ai_team:
                return node,1
            elif winner==None:
                return node,0
            else:
                return node,-1
        ##########
        ##New team
        if team=='O':
            next_team='X'
        else:
            next_team='O'            
        ####
        max_score=None
        best_move=None
        for node in range(9):
            if code[node]==' ':
                new_code=code.copy()
                new_code[node]=next_team
                move,score=dfs(new_code,next_team,node)
                if next_team==ai_team:
                    if max_score==None:
                        max_score=score
                        best_move=move
                    if score<max_score:
                        max_score=score
                        best_move=move
                else:
                    if max_score==None:
                        max_score=score
                        best_move=move
                    if score>max_score:
                        max_score=score
                        best_move=move                    
        ###Tally scores here and find which move you want?
        print ('returning',best_move,max_score)
        return best_move,max_score
            
                    
        ##########
    best_move,max_score=dfs(code,team,None)
    return best_move

def next_move(code,ai_team):
    board=Board(code)
    total=set()
    def dfs(code,team,node,top=True):
        over,winner=board.check_end(code)
        if over:
            s=''.join(str(x) for x in code)
            total.add((s,winner,node))
            if winner==ai_team:
                return 1
            elif winner==None:
                return 0
            else:
                return -1
        ##########
        ##New team
        if team=='O':
            next_team='X'
        else:
            next_team='O'            
        ####
        max_score=None
        best_move=None
        for node in range(9):
            if code[node]==' ':
                new_code=code.copy()
                new_code[node]=next_team
                score=dfs(new_code,next_team,node,False)
                if next_team==ai_team:
                    if max_score==None:
                        max_score=score
                        best_move=node
                    if score==max_score:
                        x=random.random()
                        if x>0.5:
                            best_move=node
                    if score>max_score:
                        max_score=score
                        best_move=node
                else:
                    if max_score==None:
                        max_score=score
                        best_move=node
                    if score==max_score:
                        x=random.random()
                        if x>0.5:
                            best_move=node                    
                    if score<max_score:
                        max_score=score
                        best_move=node                    
        ###Tally scores here and find which move you want?
        if top==True:
            return best_move,max_score
        return max_score
            
                    
        ##########
    best_move,max_score=dfs(code,team,None)
    return best_move

        
board=Board(example_code)
board.print_board(example_code)
over=False
team=input('X or O?')
if team=='O':
    ai_team='X'
    move= next_move(example_code,ai_team)
    board.add_move(example_code,move,ai_team)
    board.print_board(example_code)
    over,winner=board.check_end(example_code)    
else:
    ai_team='O'
    
while over==False:
    move=input('Enter a move: ')
    if example_code[int(move)]!=' ':
        print('invalid move')
        continue
    board.add_move(example_code,move,team)
    board.print_board(example_code)
    over,winner=board.check_end(example_code)
    if over:
        break
    
    move= next_move(example_code,ai_team)
    board.add_move(example_code,move,ai_team)
    board.print_board(example_code)
    over,winner=board.check_end(example_code)
    
if over==True and winner:
    print("Game Over!", winner,'wins!')
if over==True and winner==None:
    print("Game over! It's a draw!")