from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}          
        players = set()       
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            losses[loser] = losses.get(loser, 0) + 1

        answer0 = []
        answer1 = []

        for player in players:
            if losses.get(player, 0) == 0:
                answer0.append(player)
            elif losses[player] == 1:
                answer1.append(player)

        return [sorted(answer0), sorted(answer1)]
