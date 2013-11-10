def is_in_list(G,list):
    """
    This function tells whether a given graph
    is already in a given list of graphs.
    
    INPUT:
        Graph G and a list of graphs.
        
    OUTPUT:
        True if the graph is already in the list
        False else
        
    EXAMPLE:
        sage: L = [DiGraph({0:[1],1:[2],2:[3]}]
        sage: is_in_list(DiGraph({0:[1],1:[2]}), L)
        False
    
    
    """
    if not len(list) == 0:
        H = G.copy()
        i = 0
        while i < len(list):
            if H.is_isomorphic(list[i]):
                return True
            i+=1
    return False
    
    
    
def binary_strings(n):
    """
    This function will return all binary strings of length n.
    
    INPUT: 
        Integer n.
        
    OUTPUT:
        All binary strings of length n.
        
    EXAMPLE:
        sage: binary_strings(3)
        sage: for b in binary_stings:
        sage:     print b
               	
        [0, 0, 0]
        [0, 0, 1]
        [0, 1, 0]
        [0, 1, 1]
        [1, 0, 0]
        [1, 0, 1]
        [1, 1, 0]
        [1, 1, 1]

    """
    i = 0
    list = []
    while i < n:
        list.append(0)
        list.append(1)
        i+=1
    
    binary = Permutations(list,n)
    return binary
    
 
def di_edge_sets(G):
    """
    This function takes a simple graph and creates
    a list of possible edges for the orientations
    of G.
    
    INPUT:
        A simple graph G.
        
    OUTPUT:
        The set of possible edges that can exist in
        an orientation of G.
        
    EXAMPLE:
        sage: G = Graph({0:[1],1:[2]})
        sage: di_edge_sets(G)
        [[(0,1),(1,0)],[(1,2),(2,1)]]
    """
    edges = G.edges(labels = False)
    new_edges = []
    i=0
    while i < len(edges):
        new_edges.append([edges[i],(edges[i][1],edges[i][0])])
        i+=1
        
    return new_edges
    
    
    
    
def orientations(G):
    """
    This function will produce a list of all
    the orientations of a graph G.
    
    Input:
        A simple graph G.
        
    Output:
        A list of orientations of G.
        
    EXAMPLE:
        sage: G = Graph({0:[1],1:[2]})
        sage: for g in orientations(G):
        sage:    print g
        
                Digraph on 3 vertices
                Digraph on 3 vertices
                Digraph on 3 vertices  
    """
    orientations = []
    num_edges = len(G.edges(labels = False))
    possible_edges = di_edge_sets(G)
    binary = binary_strings(num_edges)
    for b in binary:
        D = DiGraph()
        i = 0
        while i < num_edges:
            D.add_edge(possible_edges[i][b[i]])
            i+=1
        if not is_in_list(D,orientations):
            orientations.append(D)
            
    return orientations