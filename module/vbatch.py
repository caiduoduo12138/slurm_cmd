import sys
from slurm import sbatch_cmd


if __name__ == "__main__":
    sbatch_cmd(*sys.argv)
