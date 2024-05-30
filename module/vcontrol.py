import sys
from slurm import scontrol_cmd


if __name__ == "__main__":
    scontrol_cmd(*sys.argv)
