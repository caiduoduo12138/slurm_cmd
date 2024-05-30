import os
import subprocess
from utils import check_login, parase_cmd_args, get_index


@check_login
def sinfo_cmd(*args):
    command = "sinfo"
    for arg in args[1:]:
        command = command + " " + arg
    tmp = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")

    if len(tmp.stdout) > 0:
        out_string = tmp.stdout
    else:
        out_string = tmp.stderr

    out_string = out_string.replace('sinfo', 'vinfo')
    print(out_string)

    return out_string


@check_login
def squeue_cmd(*args):
    command = "squeue"
    for arg in args[1:]:
        command = command + " " + arg
    tmp = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")

    if len(tmp.stdout) > 0:
        out_string = tmp.stdout
    else:
        out_string = tmp.stderr

    out_string = out_string.replace('squeue', 'vqueue')
    print(out_string)

    return out_string


@check_login
def scancel_cmd(*args):
    command = "scancel"
    for arg in args[1:]:
        command = command + " " + arg
    tmp = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")

    if len(tmp.stdout) > 0:
        out_string = tmp.stdout
        print(out_string)
    else:
        out_string = tmp.stderr

    out_string = out_string.replace('scancel', 'vcancel')
    print(out_string)

    return out_string


@check_login
def sbatch_cmd(*args):
    command = "sbatch"
    args = list(args)
    index = get_index(args, ['-U', '--user'])
    if index != -1:
        username = args[index+1]
        del args[index:index+2]

    else:
        username = os.listdir('/root/.vlogin/')[0].split('.')[0]

    for arg in args[1:]:
        command = command + " " + arg

    tmp = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    json_data = parase_cmd_args(command)
    json_data['user'] = username

    # request the interface

    if len(tmp.stdout) > 0:
        out_string = tmp.stdout
        json_data['state'] = True
    else:
        out_string = tmp.stderr
        json_data['state'] = False
    out_string = out_string.replace('sbatch', 'vbatch') \
                 + "  -U,  --user                specify the user to submit a job\n"
    print(out_string)

    return out_string


@check_login
def srun_cmd(*args):
    command = "srun"
    args = list(args)
    index = get_index(args, ['-U', '--user'])
    if index != -1:
        username = args[index+1]
        del args[index:index+2]

    else:
        username = os.listdir('/root/.vlogin/')[0].split('.')[0]

    for arg in args[1:]:
        command = command + " " + arg
    tmp = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    json_data = parase_cmd_args(command)
    json_data['user'] = username

    if len(tmp.stdout) > 0:
        out_string = tmp.stdout
        json_data['state'] = True
    else:
        out_string = tmp.stderr
        json_data['state'] = False
    out_string = out_string.replace('srun', 'vrun') + "  -U,  --user                specify the user to submit a job\n"
    print(out_string)
    return out_string


@check_login
def salloc_cmd(*args):
    command = "salloc"
    args = list(args)
    index = get_index(args, ['-U', '--user'])
    if index != -1:
        username = args[index+1]
        del args[index:index+2]

    else:
        username = os.listdir('/root/.vlogin/')[0].split('.')[0]

    for arg in args[1:]:
        command = command + " " + arg
    tmp = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    json_data = parase_cmd_args(command)
    json_data['user'] = username

    if len(tmp.stdout) > 0:
        out_string = tmp.stdout
        json_data['state'] = True
    else:
        out_string = tmp.stderr
        json_data['state'] = False

    out_string = out_string.replace('salloc', 'valloc')
    print(out_string)
    return out_string


@check_login
def scontrol_cmd(*args):
    command = "scontrol"
    for arg in args[1:]:
        command = command + " " + arg
    tmp = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")

    if len(tmp.stdout) > 0:
        out_string = tmp.stdout
    else:
        out_string = tmp.stderr

    out_string = out_string.replace('scontrol', 'vcontrol')
    print(out_string)

    return out_string


@check_login
def sacct_cmd(*args):
    command = "sacct"
    for arg in args[1:]:
        command = command + " " + arg
    tmp = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")

    if len(tmp.stdout) > 0:
        out_string = tmp.stdout
    else:
        out_string = tmp.stderr

    out_string = out_string.replace('sacct', 'vacct')
    print(out_string)

    return out_string


def check_version(self):
    tmp = subprocess.run("slurm --version", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    if len(tmp.stderr) > 0:
        return -1

    return 0


if __name__ == "__main__":
    check_version()
