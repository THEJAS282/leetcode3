def equalPairs(self, grid: List[List[int]]) -> int:
        dabba={"col":[]}
        for j in range(len(grid)):
            potti=[]
            for k in range(len(grid)):
                potti.append(grid[k][j])
            dabba["col"].append(potti)
        ennikkai=0
        for j in grid:
            for k in dabba["col"]:
                if j==k:
                    ennikkai+=1
        return ennikkai
                

