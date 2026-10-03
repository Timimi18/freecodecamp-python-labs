# Description: Parses internal dictionary-mapped connectivity schemas and converts them into explicit 2D adjacency matrix grids.
def adjacency_list_to_matrix(adj_list: dict) -> list[list[int]]:
    num_vertices = len(adj_list)
    matrix = [[0] * num_vertices for _ in range(num_vertices)]
    
    for source_node, target_nodes in adj_list.items():
        for target_node in target_nodes:
            matrix[source_node][target_node] = 1
            
    for row in matrix:
        print(row)
        
    return matrix
