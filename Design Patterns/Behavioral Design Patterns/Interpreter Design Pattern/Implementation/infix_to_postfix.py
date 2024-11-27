# Interface
class Pattern:
    def conversion(self, expression):
        pass

class InfixToPostfix(Pattern):
    def preced(self, ch):
        if ch == '^':
            return 3
        
        if ch in ['*', '/']:
            return 2
        
        if ch in ['-', '+']:
            return 1
        
        return -1
    

    def conversion(self, expression):
        arr = []
        ans = ''
        
        for ch in expression:
            if ch >= 'a' and ch <= 'z':
                ans += ch

            elif ch == '(':
                 arr.append('(')

            elif ch == ')':

                while len(arr) !=0 and arr[-1] != '(':
                    ans += arr[-1]
                    arr.pop()
                # popping out left parenthesis.    
                if len(arr) != 0:
                    arr.pop()
            
            else:

                while len(arr) !=0 and self.preced(arr[-1]) > self.preced(ch):
                    ans += arr[-1]
                    arr.pop()

                arr.append(ch)

        while len(arr) != 0:
            ans += arr[-1]
            arr.pop()

        return ans  



input_str = "(a-b/c)*(a/k-l)"

infix_to_postfix = InfixToPostfix()

print(infix_to_postfix.conversion(input_str))