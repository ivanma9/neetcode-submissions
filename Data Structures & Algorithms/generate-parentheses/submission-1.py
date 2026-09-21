class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # if there are still open i can choose close or open
        # restriciton: cannot make more close if there are no open
        # opencount >= closecount
        # if number of close == # of open only can choose open if # open < n
        
        # once # of close == n: append to res
        combinations = []

        def subFunc(open_count, close_count, parens):
            print(open_count, close_count, parens)
            if open_count == close_count == n:
                combinations.append(parens)
                return
            # if open_count == n:
            #     # must choose close
            #     parens +=")"
            #     subFunc(open_count, close_count + 1, parens)
            #     parens = parens[:-1]           
             # only can choose open
            if close_count <= open_count and open_count < n:
                # add open
                parens += "("
                subFunc(open_count +1, close_count, parens)
                parens = parens[:-1]
            if close_count < open_count:
                parens +=")"
                subFunc(open_count, close_count+1, parens)
                parens = parens[:-1]

            # parens.pop()
# ["((()))","(()())","(())()","()(())","()()()"]
# ()
        subFunc(0,0, "")
        return combinations

        

