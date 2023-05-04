#https://leetcode.com/problems/dota2-senate/
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        queue = deque(list(senate))
        n_r = senate.count("R")
        n_d = len(senate) - n_r
        r_banned = 0
        d_banned = 0
        while n_r != 0 and n_d != 0:
            senator = queue.popleft()
            if senator == "R":
                if r_banned == 0:
                    d_banned += 1
                    queue.append("R")
                else:
                    r_banned -= 1
                    n_r -= 1
            else:
                if d_banned == 0:
                    r_banned += 1
                    queue.append("D")
                else:
                    d_banned -= 1
                    n_d -= 1
        return "Radiant" if n_r > 0 else "Dire"