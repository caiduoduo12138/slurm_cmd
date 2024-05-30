import sys
from slurm import sinfo_cmd


if __name__ == "__main__":
    sinfo_cmd(*sys.argv)
