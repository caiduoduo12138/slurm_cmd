import sys
from slurm import sacct_cmd


if __name__ == "__main__":
    sacct_cmd(*sys.argv)
