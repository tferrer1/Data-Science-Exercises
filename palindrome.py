def palindrome_finder(s):

    if len(s) == 0:
        return ''
    else:
        longest_palindrome = s[0]
    
    while len(s) > len(longest_palindrome):        
        
        ptr = len(s)-1
        
        while ptr >= len(longest_palindrome):
            
            if s[0] == s[ptr]:
                # go down the rabbit hole
                p1 = 0
                p2 = ptr
                
                start_half = ''
                end_half = ''
                
                is_palindrome = True
                while (p2 - p1) > 0: # check if palindrome / go down rabbithole
                    if s[p1] == s[p2]:
                        start_half += s[p1]
                        end_half = s[p2] + end_half
                        p1 += 1
                        p2 -= 1
                    else:
                        is_palindrome = False
                        break
                
                if is_palindrome:
                    if p2 == p1:
                        longest_palindrome = start_half + s[p1] + end_half
                    else:
                        longest_palindrome = start_half + end_half
                    
                    break
                
            ptr -= 1
        s = s[1:]
        
    return longest_palindrome

#s = "zabbabbammabbabbafghtypdpxxpdpythgf"
#s = 'abacab'
#s = ''
#s = 'a'
#s = 'cbbd'
    
import timeit
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

start = timeit.default_timer()
print(palindrome_finder(s))
print("seconds it took", timeit.default_timer() - start)