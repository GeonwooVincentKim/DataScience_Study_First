import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "David"}
]

friendships = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]
