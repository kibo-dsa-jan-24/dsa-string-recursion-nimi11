class String:
    def print_dashed(s):
        if s is None or s == " ":
            return s
        if len(s) == 1:
            print(s) 
            return
        print(s[0], end='-')
        return String.print_dashed(s[1:])

    def remove_char(s, c):
        if s is None or s == " ":
            return s
        removed_from_rest = String.remove_char(s[1:], c)
        if s[0] ==c:
            return removed_from_rest
        else:
            return s[0] + removed_from_rest


    def to_upper_case(s):
        if s is None or s == "":
            return s 
        
        upper = String.to_upper_case(s[1:])  
        return s[0].upper() + upper 
        

    def get_index(s, c):
        if s[c] == -1:
            return -1
        index_of_rest= get_index(s[1:],c)
        if s[0] == c:
            return 1+ index_of_rest
        else:
            return index_of_rest
        


    def prune(s):
        if s is None or s == '':
            return s
        if s[0] ==" ":
            return String.prune(s[1:])
        elif s[-1] == " ":
            return String.prune(s[:-1])
        return s


if __name__ == "__main__":
    String.print_dashed("hello")
    ans =String.to_upper_case('hi')
    print(ans)
    index = get_index('hello', 'z')
    print(index)
