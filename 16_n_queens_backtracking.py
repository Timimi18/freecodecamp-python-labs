# Description: Employs a last-in-first-out optimization matrix stack to evaluate non-conflicting column coordinates for the N-Queens challenge.
def dfs_n_queens(n: int) -> list[list[int]]:
    if n < 1:
        return []
        
    solutions = []
    stack = [(0, [])]
    
    while stack:
        row, state = stack.pop()
        
        if row == n:
            solutions.append(state)
            continue
            
        for col in range(n - 1, -1, -1):
            if col in state:
                continue
                
            conflict = False
            for r, c in enumerate(state):
                if abs(r - row) == abs(c - col):
                    conflict = True
                    break
                    
            if not conflict:
                stack.append((row + 1, state + [col]))
                
    return solutions
