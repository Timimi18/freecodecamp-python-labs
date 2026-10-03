# Description: Traverses multi-directional graph spaces systematically using tracking matrices and custom execution call-stacks.
def dfs(matrix: list[list[int]], start_node: int) -> list[int]:
    visited = []
    stack = [start_node]
    
    while stack:
        current_node = stack.pop()
        
        if current_node not in visited:
            visited.append(current_node)
            
            for neighbor in range(len(matrix) - 1, -1, -1):
                if matrix[current_node][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)
                    
    return visited
