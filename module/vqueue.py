import sys
from slurm import squeue_cmd


if __name__ == "__main__":
    squeue_cmd(*sys.argv)
