#    Written Nathan Warnberg as part of the 2013 Iowa State University Research Experience
#    for Undergraduates Combinatorial Matrix Theory research group.
#
#    Updated by Nathan Warnberg on October 26, 2013.
#    Copyright (c) 2013 Iowa State University. All rights reserved.
#
#    This code is distributed under the GNU Public License (GPL), version 2 or (at your option)
#    any later version. See http://www.gnu.org/licenses/gpl-2.0.html for details

def directed_delta(G):
    """
        This function gives the maximum of the minimum 
        of the in and out degrees of a directed graph.
        
        
        INPUT:
            A directed graph G.
        
        OUTPUT:
            The maximum of the minimum of the in and out
            degrees of the directed graph G.
        
        EXAMPLES:
        sage: G = DiGraph({0:{1,2,3}, 2:{0,4,5,6,7}, 4:{2,6}})
        sage: directed_delta(G)
        1
        
    """

    return max(min(G.in_degree_sequence()),min(G.out_degree_sequence()))

def directed_delta_upper(G):
    """
        This function calculates and upper bound on the 
        minimum rank of the corresponding matrix based 
        on the minimum in/out degree.
        
        
        INPUT:
            A directed graph G.
        
        OUTPUT:
            An upper bound on the minimum rank of G
        
        EXAMPLES:
        sage: G = DiGraph({0:{1,2,3}, 2:{0,4,5,6,7}, 4:{2,6}})
        sage: directed_delta_upper(G)
        7
        
    """
    
    return G.order()-directed_delta(G)   
     
def directed_Z_lower(G):
    """
        This function calculates a lower bound on the
        minimum rank of the corresponding matrix based
        on the directed zero forcing number.  Note that
        this function requires the di_Z(G) function.
        
        
        INPUT:
            A directed graph G.
        
        OUTPUT:
            A lower bound on the minimum rank of G
        
        EXAMPLES:
        sage: G = DiGraph({0:{1,2,3}, 2:{0,4,5,6,7}, 4:{2,6}})
        sage: directed_Z_lower(G)
        3    
    """
    
    return G.order()-di_Z(G)[0]      
    

def di_min_rank_bounds(G):
    """
        This function computes lower and upper bounds on
        minimum rank of a given directed graph.
        
        
        INPUT:
            A directed graph G.
        
        OUTPUT:
            A lower and upper bounds on the minimum rank of G.
        
        EXAMPLES:
        sage: G = DiGraph({0:{1,2,3}, 2:{0,4,5,6,7}, 4:{2,6}})
        sage: di_min_rank_bounds(G)
        (3,7)
        
    """ 
    
    lower = []
    upper = []
    lower.append(directed_Z_lower(G))
    upper.append(directed_delta_upper(G))
    return max(lower),min(upper)