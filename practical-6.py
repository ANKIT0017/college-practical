def is_complete_graph(adj_matrix):
    """
    Check if the given graph represented by the adjacency matrix is a complete graph.

    Parameters:
        adj_matrix (list of lists): Adjacency matrix representation of the graph.

    Returns:
        bool: True if the graph is a complete graph, False otherwise.
    """
    num_vertices = len(adj_matrix)
    
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and adj_matrix[i][j] != 1:
                return False
    
    return True

def main():
    # Example adjacency matrix for a graph with 4 vertices
    adj_matrix = [
        [0, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 0]
    ]

    if is_complete_graph(adj_matrix):
        print("The given graph is a complete graph.")
    else:
        print("The given graph is not a complete graph.")

if __name__ == "__main__":
    main()
