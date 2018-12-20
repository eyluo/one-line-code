# There are N rooms and you start in room 0.  Each room has a distinct number 
# in 0, 1, 2, ..., N-1, and each room may have some keys to access the next 
# room.
# Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is
# an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v 
# opens the room with number v.
# Initially, all the rooms start locked(except for room 0).
# You can walk back and forth between rooms freely.
# Return true if and only if you can enter every room.

class Solution(object):
    def canVisitAllRooms(self, rooms): return ((lambda vstd: vstd if (lambda frontier: [(lambda v: [vstd.add(v)] + [frontier.append(neighbor) if neighbor not in vstd else None for neighbor in rooms[v]])(frontier.pop(0)) if len(frontier) != 0 else None for _ in range(len(rooms)**2)])([0]) else vstd)(set())) == set(range(len(rooms)))
