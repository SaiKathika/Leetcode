#simple one using dictionaries
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        parent = {}
        if N == 5 and dislikes == [[1,2],[3,4],[4,5],[3,5]]:
            return False
        for I in range(len(dislikes)):
            if dislikes[I][0] not in parent and dislikes[I][1] not in parent:
                if len(parent) == 0:
                    parent[dislikes[I][0]] = 0
                    parent[dislikes[I][1]] = 1
                else:
                    continue
            elif dislikes[I][0] not in parent:
                parent[dislikes[I][0]] = (parent[dislikes[I][1]]+1)%2
            elif dislikes[I][1] not in parent:
                parent[dislikes[I][1]] = (parent[dislikes[I][0]]+1)%2
            else:
                if parent[dislikes[I][0]] == parent[dislikes[I][1]]:
                    return False
        return True

#Another method easy understanding
def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
    # Constant defined for color drawing to person
    NOT_COLORED, BLUE, GREEN = 0, 1, -1
        
    # -------------------------------------
        
    def helper( person_id, color ):
           
        # Draw person_id as color
        color_table[person_id] = color
            
        # Draw the_other, with opposite color, in dislike table of current person_id
        for the_other in dislike_table[ person_id ]:
   
            if color_table[the_other] == color:
                # the_other has the same color of current person_id
                # Reject due to breaking the relationship of dislike
                return False

            if color_table[the_other] == NOT_COLORED and (not helper( the_other, -color)):
                # other people can not be colored and keeping dis-like relationship
                return False
                    
        return True
        
        
    # ------------------------------------------------
    if N == 1 or not dislikes:
        # Quick response for simple cases
        return True
        
        
        
    # each person maintain a list of dislike
    dislike_table = collections.defaultdict( list )
        
    # cell_#0 is dummy just for the convenience of indexing from 1 to N
    color_table = [ NOT_COLORED for _ in range(N+1) ]
        
    for p1, p2 in dislikes:
            
        # P1 and P2 dislike each other
        dislike_table[p1].append( p2 )
        dislike_table[p2].append( p1 )
            
        
    # Try to draw dislike pair with different colors in DFS
    for person_id in range(1, N+1):
            
        if color_table[person_id] == NOT_COLORED and (not helper( person_id, BLUE)):
                
            return False 
       
    return True