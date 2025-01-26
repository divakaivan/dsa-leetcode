class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # [[1,2],[3],[3],[]]
        # target = 4 - 1 = 3
        # 
        
        def backtrack(curr_node, path):
            
            if curr_node == target:
                results.append(list(path))
                return
            
            for next_node in graph[curr_node]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()
        
        target = len(graph) - 1
        results = []
        backtrack(0, [0])
        return results
        