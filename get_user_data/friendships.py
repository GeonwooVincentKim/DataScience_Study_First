import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

from main import *

friendships = {
    user["id"]
}
