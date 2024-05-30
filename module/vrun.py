import sys
from slurm import srun_cmd


if __name__ == "__main__":
    srun_cmd(*sys.argv)
