class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D, R = deque(), deque()
        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)
        while D and R:
            dturn = D.popleft()
            rturn = R.popleft()
            if rturn<dturn:
                R.append(rturn+len(senate))
            elif rturn>dturn:
                D.append(dturn+len(senate))
        return "Radiant" if R else "Dire"
        