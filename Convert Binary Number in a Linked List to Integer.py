#understand how binary numbers work. Imagine, that we have number 101100. 
#Then, it is equal to 1*2^5 + 0*2^4 + 1*2^3 + 1*2^2 + 0*2^1 + 0^2^0.

def getDecimalValue(head):
    s = 0
    while head:
        s = 2 * s + head.val
        head = head.next
    return s