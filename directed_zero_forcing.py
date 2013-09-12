#    Created by Nathan Warnberg on June 14th as part of the 2013 Iowa State 
#    University Research Experience for Undergraduates Combinatorial 
#    Matrix Theory Research Group.
#    Copyright (c) 2013 Iowa State University. All right reserved.
#
#    This code is distributed under the GNU Public License (GPL), version 2 or (at your option)
#    any later version. See http://www.gnu.org/licenses/gpl-2.0.html for details


def out_and_in_neighborhoods(G):
    """
    Given a directed graph we need functions that return
    the out neighbors and in neighbors of a particular 
    vertex.  This function will return two lists of lists, 
    where the outer list is a list of out/in neighborhoods
    and the inner list is the neighborood.  Note that to 
    access this list the vertices need to be labelled 
    0,1,2,...,n with no gaps, otherwise we cannot access 
    and manipulate the nieghborhood properly

    
    INPUT:
            graph G
        
    OUTPUT: 
            Returns two lists, out_list and in_list, that 
            are accessible via vertex labels.
    
    EXAMPLES:
        sage: out1,in1 = out_and_in_neighborhoods(DiGraph({0:{1,2,3}, 2:{4,5}, 4:{2}}))
        sage: print out1
        sage: print in1
        [[0, [1, 2, 3]], [1, []], [2, [4, 5]], [3, []], [4, [2]], [5, []]]
        [[0, []], [1, [0]], [2, [0, 4]], [3, [0]], [4, [2]], [5, [2]]]
    """


    out_list = []
    in_list = []
    for v in G.vertices():
        temp_out = []
        temp_in = []
        for o in G.outgoing_edge_iterator([v]):
            temp_out.append(o[1])
        for i in G.incoming_edge_iterator([v]):
            temp_in.append(i[0])
        out_list.append([v,temp_out])
        in_list.append([v,temp_in])
        
    return out_list,in_list

def is_di_zero_forcing(G,s):
    """
    Given a directed graph G and a vertex subset
    s this function determines whether or not s
    is a directed zero forcing set.

    
    INPUT:
            graph G and set s
        
    OUTPUT: 
            True if s is a directed zero forcing set
            False else
    
    EXAMPLES:
        sage: G = DiGraph({0:[1,2,3], 2:[4]})
        sage: s = [0,1,3]
        sage: is_di_zero_forcing(G,s)
        True
    """
    #note re-labelling might change whether or not s is a zero forcing set
    H = G.copy()
    blue=[]
    k = 0
    #we don't want blue and s to point at the same object so we cannot say blue = s
    while k < len(s):
        blue.append(s[k])
        k+=1
        
    out_neighborhoods,in_neighborhoods = out_and_in_neighborhoods(H)
    
    #making sure all vertices with in degree of 0 are in s
    for v in H.vertices():
        if in_neighborhoods[v][1]==[] and v not in blue:
            return False
            
    #Removing blue vertices from the out neighborhoods
    for v in H.vertices():
        for b in blue:
            if b in out_neighborhoods[v][1]:
                out_neighborhoods[v][1].remove(b)
    
    
    #initialize temp so the while loop can start
    temp = [30]
    while temp!=[]:
        temp = []
        for b in blue:
            if len(out_neighborhoods[b][1]) ==1:
                v_temp = out_neighborhoods[b][1][0]
                temp.append(v_temp)
                #removing the vertex from all out neighborhoods
                #print out_neighborhoods
                for x in in_neighborhoods[v_temp][1]:
                    out_neighborhoods[x][1].remove(v_temp)
                #print out_neighborhoods
                
                
        #updating our blue vertex set
        i = 0
        while i < len(temp):
            blue.append(temp[i])
            i+=1
            
    if len(blue) == len(H.vertices()):
        return True
    else:
        return False
        
def di_Z(G):
    """
    Given a directed graph G this function determines
    the directed zero forcing number and a particular
    minimum directed zero forcing set.

    
    INPUT:
            graph G 
        
    OUTPUT: 
            (zero forcing number, [zero forcing set])
    
    EXAMPLES:
        sage: G = DiGraph({0:[1,3,4],1:[2], 4:[0]})
        sage: di_Z(G)
        (2,[1,4])
    """
    i = 1
    while i <=len(G.vertices()):
        for w in combinations(G.vertices(),i):
            indicator = is_di_zero_forcing(G,w)
            if indicator == True:
                return i,w
        i+=1