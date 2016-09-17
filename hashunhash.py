letters = "acdegilmnoprstuw"
 
def hashstring(s):
    h = 7
    letters = "acdegilmnoprstuw"
    len_of_letters = len(s)
    for i in range(len_of_letters):
        h = (h*37 + letters.find(s[i]))
    return h

def unhash(hashstr):
    lis_val = []
    output_string = ""
    count = 0
    while hashstr > 37:
        #print count
        #print hashstr % 37
        lis_val.append(hashstr % 37)
        hashstr /= 37
        #print hashstr
        count += 1
        
    for i in lis_val:
        output_string += letters[i]
    
    return output_string[::-1]


input_str = "leepadg"
print "Hash Function..."
print "Input: "+input_str
hashstr = hashstring("leepadg")
print "Output: "+str(hashstr)
print ""
print "Unhash Function..."
print "Input: "+str(hashstr)
outputstr = unhash(hashstr)
print "Output: "+str(outputstr)

