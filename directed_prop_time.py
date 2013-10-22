#    Written Nathan Warnberg as part of the 2013 Iowa State University Research Experience 
#    for Undergraduates Combinatorial Matrix Theory research group.
#
#    Updated by Nathan Warnberg on October 21, 2013.
#    Copyright (c) 2013 Iowa State University. All rights reserved.
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
    


#This function is given a directed graph G and a list s that is a subset of the vertices
#Note that we need our vertices to be labelled 0,1,2,...,n so that we can access the neighborhood lists nicely

#Example G = DiGraph({0:[1,2,3], 2:[4]}), s = [0,1,3]
#is_di_zero_forcing(G,[0,1,3])
#True

    
def is_di_zero_forcing(G,s):
    """
    This function takes a graph G and a subset of vertices s
    and returns whether or not s is a directed zero forcing
    set of G.  NOTE: THE VERTICES OF G NEED TO BE LABELLED
    0,1,2,...,n.

    
    INPUT:
            Graph G and vertex subset s.
        
    OUTPUT: 
            Returns True if s is a directed zero forcing set
            of G.
            
            Returns False else.
    
    EXAMPLES:
        sage: G = DiGraph({0:{1,2,3}, 2:{4,5}, 4:{2}})
        sage: is_di_zero_forcing(G,[0,1,4])
        True
        sage: is_di_zero_forcing(G,[2,3,1])
        False
 
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
    Given a directed graph this function will find the size
    of the smallest directed zero forcing set.
    
    INPUT:
            A graph G
        
    OUTPUT: 
            A list whose first element is the directed zero forcing
            number and whose second element is a minimum directed
            zero forcing set. 
    
    EXAMPLES:
        sage: G = DiGraph({0:{1,2,3}, 2:{4,5}, 4:{2}})
        sage: di_Z(G)
        (3,[0,1,4])
    """
    H = G.copy()
    H.relabel()
    i = 1
    while i <=len(H.vertices()):
        for w in combinations(H.vertices(),i):
            indicator = is_di_zero_forcing(H,w)
            if indicator == True:
                return i,w
        i+=1
        

def di_zero_forcing_sets_min(G):
    """
    This function generates all directed zero forcing sets of
    a graph G.
    
    INPUT:
            A graph G.    
            
    OUTPUT:
            A list of vertex subsets of G that are minimum
            directed zero forcing sets of G.
    EXAMPLES:
        sage: G = DiGraph({0:{1,2,3}, 2:{4,5}, 4:{2}})
        sage: di_zero_forcing_sets_min(G)
        [[0,1,4],[0,3,4]]
    
    """
    #This generates the directed zero forcing number of G
    H = G.copy()
    H.relabel()
    z = di_Z(H)[0]    
    sets = []
    #Uncomment the next line in if you would like to see what the
    #relabelled graph looks like
    #H.show()
    for w in combinations(H.vertices(),z):
        bool = is_di_zero_forcing(H,w)
        if bool == True:
            sets.append(w)
    return sets
    
    
def di_prop_time(G,s):
    """
    This function determines the directed propagation 
    time of a given graph G and given vertex subset s.

    
    INPUT:
            A graph G and vertex subset s.
        
    OUTPUT: 
            The propagation time. 
    
    EXAMPLES:
        sage: G = DiGraph({0:{1,2,3}, 2:{4,5}, 4:{2}})
        sage: di_prop_time(G,[0,1,4])
        2
        sage: di_prop_time(G,[2,3,1])
        -1
 
    """
    #note re-labelling might change whether or not s is a zero forcing set
    H = G.copy()
    counter = -1
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
            return -1
            
    #Removing blue vertices from the out neighborhoods
    for v in H.vertices():
        for b in blue:
            if b in out_neighborhoods[v][1]:
                out_neighborhoods[v][1].remove(b)
    
    
    #initialize temp so the while loop can start
    temp = [30]
    while temp!=[]:
        counter+=1
        temp = []
        for b in blue:
            if len(out_neighborhoods[b][1]) ==1:
                v_temp = out_neighborhoods[b][1][0]
                temp.append(v_temp)
                #removing the vertex from all out neighborhoods
                for x in in_neighborhoods[v_temp][1]:
                    out_neighborhoods[x][1].remove(v_temp)
                
                
        #updating our blue vertex set and adding one to the propagation time
        i = 0
        while i < len(temp):
            blue.append(temp[i])
            i+=1
            
    if len(blue) == len(H.vertices()):
        return counter
    else:
        return -1
    
    
def di_min_prop_time_int(G):
    """
    This function determines the minimum directed 
    propagation time of a given graph G.

    
    INPUT:
            A graph G.
        
    OUTPUT: 
            The minimum propagation time. 
    
    EXAMPLES:
        sage: G = DiGraph({0:{1,2,3}, 2:{0,4,5,6,7}, 4:{2,6}})
        sage: di_min_prop_time_int(G)
        [2,3]
 
    """
    H = G.copy()
    H.relabel()
    prop_times = []
    S = di_zero_forcing_sets_min(G)
    for s in S:
        time = di_prop_time(G,s)
        if time not in prop_times:
            prop_times.append(time)
    prop_times.sort()
    #To get the full propagation time interval remove the [0] from the next line
    return prop_times
        