import sys
from slurm import salloc_cmd


if __name__ == "__main__":
    salloc_cmd(*sys.argv)
