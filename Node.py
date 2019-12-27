class Node:
    goal_state = [1, 2, 3, 
                  8, 0, 4,
                  7, 6, 5]
    def __init__(self, puzzle_state, parent, level):
        self.puzzle_state = puzzle_state
        self.parent = parent
        self.level = level
    
    def is_goal_state(self):
        if self.puzzle_state == self.goal_state:
            return True
        return False

    def state(self):
        list=self.puzzle_state
        string=""
        for i in range(9):
            if (i + 1) % 3 != 0:
                if list[i]==0:
                    string += ("|   ")
                else:
                    string+=("| %d "% list[i])
            else:
                if list[i]==0:
                    string += ("|   \n")
                else:
                    string+=("| %d |\n" %list[i])
        string+="\n"
        return string

    def __str__(self):
        return self.state()

    def calc_f(self):
        manhattan_distance = 0
        for i in range(9):
                b, g = self.puzzle_state.index(i), self.goal_state.index(i)
                manhattan_distance += abs(b%3 - g%3) + abs(b//3 - g//3)
        f = manhattan_distance + self.level
        return f


    def possible_moves(self, i, j):
        moves = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        if i == 0:
            moves.remove('UP')
        if i == 2:
            moves.remove('DOWN')
        if j == 0:
            moves.remove('LEFT')
        if j == 2:
            moves.remove('RIGHT')
        return moves

    def expand(self):
        children = []
        x = self.puzzle_state.index(0)
        i = int(x / 3)
        j = int(x % 3)
        moves = self.possible_moves(i, j)
        for move in moves:
            new_state = self.puzzle_state.copy()
            if move is 'UP':
                new_state[x], new_state[x-3] = new_state[x-3], new_state[x]
            if move is 'DOWN':
                new_state[x], new_state[x+3] = new_state[x+3], new_state[x]
            if move is 'LEFT':
                new_state[x], new_state[x-1] = new_state[x-1], new_state[x]
            if move is 'RIGHT':
                new_state[x], new_state[x+1] = new_state[x+1], new_state[x]

            children.append(Node(new_state, self, self.level))
        return children

    def find_solution(self):
        solution = []
        solution.append(self.puzzle_state)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.puzzle_state)
        solution.reverse()
        return solution