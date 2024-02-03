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
        if s is None or s == '':
            return s
        removed_from_rest = String.remove_char(s[1:],c)
        if s[0] == c:
            return removed_from_rest
        else:
            return s[0] + removed_from_rest

    def to_upper_case(s):
        if s is None or s == '':
            return s 
        
        upper = String.to_upper_case(s[1:])  
        return s[0].upper() + upper 
        

    def get_index(s, c):
        if c not in s:
            return -1
        if s[0] == c:
            return 0
        index_of_rest= String.get_index(s[1:],c)
        if index_of_rest == -1:
            return -1
        else:
            return index_of_rest +1
        


    def prune(s):
        if s is None or s =='':
            return -1
        if s[0] == ' ':
            return  String.prune(s[1:])
        if s[-1] == " ":
            return String.prune(s[:-1])
        return s
        

if __name__ == "__main__":
    String.print_dashed("hello")
    ans =String.to_upper_case('hi')
    print(ans)
    index = String.get_index('elephant','t')
    print(f'index: {index}')

    removed = String.remove_char('apple','a')
    print(f"removed : {removed}")

    removed1 = String.remove_char('banana','a')
    print(f"removed : {removed1}")

    pruned = String.prune('   hello world   ')
    print(f"pruned: {pruned}")