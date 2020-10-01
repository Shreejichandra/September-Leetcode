'''You are given equations in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating-point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.'''


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        d = defaultdict(dict)
    
        for i in range(len(values)):
            d[equations[i][0]][equations[i][1]] = values[i]
            d[equations[i][1]][equations[i][0]] = 1.0 / values[i]
        # print(d)
        
        
        def dfs(x, y, visited):
            if x not in d or y not in d:
                return -1.0
            if x == y:
                return 1.0
            if y in d[x]:
                return d[x][y]
            
            for i in d[x]:
                if i not in visited:
                    visited.append(i)
                    value = dfs(i, y, visited)
                    if value == -1.0:
                        continue
                    else:
                        return value * d[x][i]
            return -1.0
        
        output = []
        
        for i in queries:
            visited = []
            output.append(dfs(i[0], i[1], visited))
        return output
            
        
