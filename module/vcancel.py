import sys
from slurm import scancel_cmd


if __name__ == "__main__":
    scancel_cmd(*sys.argv)
