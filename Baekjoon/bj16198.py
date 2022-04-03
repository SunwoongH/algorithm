'''
Created by sunwoong on 2022/04/03
'''
import sys

n = int(sys.stdin.readline())
beads = list(map(int, sys.stdin.readline().split()))

max_energy = -sys.maxsize
def dfs(energy: int) -> None:
    if len(beads) == 2:
        global max_energy
        max_energy = max(max_energy, energy)
        return
    for i in range(1, len(beads) - 1):
        bead = beads.pop(i)
        dfs(energy + beads[i - 1] * beads[i])
        beads.insert(i, bead)
dfs(0)
print(max_energy)