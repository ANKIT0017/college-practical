def compute_degrees(adj_matrix):
    """
    Compute the in-degree and out-degree of each vertex in a directed graph.

    Parameters:
        adj_matrix (list of lists): Adjacency matrix representation of the directed graph.

    Returns:
        tuple: A tuple containing two dictionaries:
               - The first dictionary maps each vertex to its in-degree.
               - The second dictionary maps each vertex to its out-degree.
    """
    num_vertices = len(adj_matrix)
    in_degrees = {}
    out_degrees = {}

    # Initialize in-degree and out-degree dictionaries with 0 for all vertices
    for i in range(num_vertices):
        in_degrees[i] = 0
        out_degrees[i] = 0

    # Compute in-degree and out-degree for each vertex
    for i in range(num_vertices):
        for j in range(num_vertices):
            out_degrees[i] += adj_matrix[i][j]  # Out-degree: Count of outgoing edges
            in_degrees[j] += adj_matrix[i][j]   # In-degree: Count of incoming edges

    return in_degrees, out_degrees

def main():
    # Example adjacency matrix for a directed graph with 4 vertices
    adj_matrix = [
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [1, 0, 1, 0]
    ]

    in_degrees, out_degrees = compute_degrees(adj_matrix)

    # Print the in-degree and out-degree of each vertex
    for vertex in range(len(adj_matrix)):
        print(f"Vertex {vertex}: In-degree = {in_degrees[vertex]}, Out-degree = {out_degrees[vertex]}")

if __name__ == "__main__":
    main()
