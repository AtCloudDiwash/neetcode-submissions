class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        store = []
        stack = []
        for i in range(len(position)):
            store.append([position[i], speed[i]])
        
        store.sort(key = lambda x:x[0], reverse = True)

        for i in range(len(store)):
            if not stack:
                stack.append((target - store[i][0])/store[i][1])
            else:
                curr = (target - store[i][0])/store[i][1]
                if stack[-1] < curr:
                    stack.append(curr)
                
        return len(stack)


        
        







