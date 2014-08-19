#    Created by Steve Butler and Nathan Warnberg on August 28, 2013
#    Copyright (c) 2013 Iowa State University. All right reserved.
#
#    The source code for Zplus was authored by Steven Butler, Jason Grout and Tracy Hall.
#    It may be found on Github,https://github.com/jasongrout/minimum_rank/blob/master/Zq.py
#    This code is distributed under the GNU Public License (GPL), version 2 or (at your option)
#    any later version. See http://www.gnu.org/licenses/gpl-2.0.html for details

#This will load Steve Butler and Jason Grout minimum rank software
URL='http://github.com/jasongrout/minimum_rank/raw/minimum_rank_1_1_3/'
files=['Zq_c.pyx','Zq.py','zero_forcing_64.pyx','zero_forcing_wavefront.pyx','minrank.py', 'inertia.py']
for f in files:
   load(URL+f)
    
    


def pt_plus(G,S):
    """
    pt_plus(G,S) returns the propagation time for
    positive semidefinite zero forcing on the graph G
    given a set S

    
    INPUT:
            graph G, vertex subset S
        
    OUTPUT: 
            Returns the propagation time based on the
            positive semidefinite color change rule.
    
    EXAMPLES:
        sage: pt_plus(graphs.CompleteGraph(6),[0,1,2,3])
        -1
        sage: pt_plus(graphs.PetersenGraph(),[0,2,8,7]) 
        2
    """
    prop_time = 0
    H = copy(G)
    H.delete_vertices(S)
    T = list(copy(S))
    while len(H.connected_components())==1:
        prop_time += 1
        new_T=copy(T)
        for v in T:
            N = set(G.neighbors(v))
            N.difference_update(set(T))
            if len(N) == 1:
                new_T.append(N.pop())
        if T == new_T:
            return -1
        T = new_T
        H = copy(G)
        H.delete_vertices(T)
    if len(H.connected_components())==0:
        return prop_time
    else:
        sub_times=[]
        for V in H.connected_components():
            B=set(G.vertices())
            B.difference_update(set(V))
            B=list(B)
            sub_times.append(pt_plus(G,B))
            if sub_times[-1]==-1:
                return -1
        return prop_time+max(sub_times)
        
        

def pt_plus_set(G):
    """
    given a graph G computes all possible
    semidefinite propagation times and returns as
    list of lists
    
    INPUT:
            graph G
        
    OUTPUT: 
            A list of lists, where each sublist[i] is the set of propagation
            times for positive semidefinite zero forcing sets of size i.  If
            sublist[i] is empty then no positive semidefinite zero forcing set
            of size i exists.
    
    EXAMPLES:
        sage: pt_plus_set(graphs.CompleteGraph(4))
        [[],[],[1],[0]]
        sage: pt_plus_set(atlas_graphs[5]) #path on three vertices and an isolated vertex
        [[], [], [1, 2], [1], [0]]
    """
    H=copy(G)
    H.relabel()
    all_times=[[]]
    for i in range(1,H.order()):
        #the i^th entry of i_times corresponds to forcing sets of size i
        i_times=[]
        #checking the propagation time of every vertex subset of size i
        for S in combinations(range(H.order()),i):
            q=pt_plus(H,S)
            if q>-1 and q not in i_times:
                i_times.append(q)
        i_times.sort()
        all_times.append(i_times)
    all_times.append([0])
    return all_times
    

def Zplus_gen(G):
    """
    Given a graph G, connected or disconnected, calculates the
    positive semidefinite zero forcing number for each connected
    component and returns the sum.
    
    INPUT:
            graph G
        
    OUTPUT: 
            If the graph is connected returns the positive
    semidefinite zero forcing number.
            If the graph is disconneceted, returns the sum of the 
    positive semidefinite zero forcing number of each connected
    component.
    
    EXAMPLES:
        sage: Zplus_gen(graphs.CompleteGraph(6))
        5
        sage: Zplus_gen(atlas_graphs[5]) 
        2
    """
    
    z = 0
    #for each connected component find the positive semidefinite zero forcing number and sum
    for H in G.connected_components_subgraphs():
        #The positive semidefinite zero forcing number of a tree is 1 
        if H.is_tree():
            z = z+1
        else:
            z = z + Zplus(H)
        
    return z




def min_pt_plus_int(G):
    """
    Given a graph G this function computes the minimum and maximum propagation time
    of G, along with vertex subsets that realize them and the propagation time interval.
    
    INPUT:
            graph G
        
    OUTPUT: 
            Returns a list of three items: positive semidefinite propagation time interval, 
            a minimum positive semidefinite zero forcing set that realizes the minimum 
            propagation time, a minimum positive semidefinite zero forcing set that realizes
            the maximum propagation time. 
    
    EXAMPLES:
        sage: min_pt_plus_int(graphs.CompleteGraph(6))
        [[1],[0,1,2,3,4],[0,1,2,3,4]]
        sage: min_pt_plus_int(graphs.PetersenGraph()) 
        [[1, 2, 3], [0, 2, 8, 9], [0, 1, 2, 8]]
    """
    min_times = []
    max_set = []
    min_set = []
    H = copy(G)
    H.relabel()
    z=Zplus_gen(H)
    c = 0
    #checking the propagation time for all minimum positive semidefinite zero forcing sets.
    for S in Combinations(range(H.order()),z):
        q = pt_plus(H,S)
        if q > -1 and q not in min_times and c==0:
            c = c+1
            min_times.append(q)
            
        if q > -1 and c > 0:
            m = min(min_times)
            n = max(min_times)
            
            #adding sets that realize minimum prop time
            if q <= m:
                min_set.append(S)
                if q < m:
                    min_set = []
                    min_set.append(S) 
            #adding sets that realize maximum prop time
            if q >= n:
                max_set.append(S)
                if q > n:
                    max_set = []
                    max_set.append(S)
            if q not in min_times:
                min_times.append(q) 
        
    min_times.sort()
    return [min_times,min_set[0],max_set[0] ]
    
    

def full_pt_plus_int(G):
    """
        Given a graph G this function tells us whether or not
        the graph has a full positive semidefinite
        propagation time interval.
    
    INPUT:
            graph G
        
    OUTPUT: 
            Returns True if the propagation time interval is full, returns False else.
           
    
    EXAMPLES:
        sage: full_pt_plus_int(graphs.CompleteGraph(6))
        True
        sage: full_pt_plus_int(graphs.PetesonGraph) 
        True
    """
    z = Zplus_gen(G)
    #We know trees have a full propagation time interval
    if z == 1:
        return True
    else:
        p = min_pt_plus_int(G)[0] #the minimum prop time
        l = len(p) #how long the prop time interval is
        d = p[l-1] - p[0] # the difference between the minimum and maximum prop time
        D = (d + 1) - l 
    if D == 0:
        return True
    return False
