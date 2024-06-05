import os
import subprocess
import requests
from utils import check_login, parase_cmd_args, get_index


url = "http://192.168.100.109:9999/api/slurmJob/syncSlurmJob"


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

    if len(tmp.stdout) > 0:
        out_string = tmp.stdout
        if "Submitted batch job" in out_string:
            json_data['state'] = True
            json_data['job_id'] = out_string.split(' ')[-1]

    else:
        out_string = tmp.stderr

    out_string = out_string.replace('sbatch', 'vbatch')

    if ('-h' in args) or ('--help' in args):
        out_string = out_string + "  -U,  --user                 specify the user to submit a job\n"
    print(out_string)

    try:
        _ = requests.post(url, json=json_data)
    except:
        print("request the {} failed!".format(url))

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
    tmp = subprocess.run("sacct -n -S 0101 |tail -n 1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         encoding="utf-8")
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if len(tmp.stdout) > 0:
        job_id = str(int(tmp.stdout.split(' ')[0]) + 1)

        # print(tmp.stdout)
    else:
        # print(tmp.stderr)
        job_id = "-1"

    json_data = parase_cmd_args(command)
    json_data['user'] = username
    json_data['job_id'] = job_id
    only_once = True
    while True:
        output = p.stdout.readline().decode('utf-8')
        if output == '' and p.poll() is not None:
            if ('-h' in args) or ('--help' in args):
                print("-U,  --user                 specify the user to submit a job")
            break

        if output:
            print(output.strip().replace('srun', 'vrun'))
            if only_once:
                json_data['state'] = True
                try:
                    _ = requests.post(url, json=json_data)
                except:
                    print("request the {} failed!".format(url))
                only_once = False

    err = p.stderr.read().decode('utf-8')
    if err:
        json_data['state'] = False
        print(f"Error: {err.strip().replace('srun', 'vrun')}")

    try:
        _ = requests.post(url, json=json_data)
    except:
        print("request the {} failed!".format(url))

    return None


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
        if "Submitted batch job" in out_string:
            json_data['state'] = True
            json_data['job_id'] = out_string.split(' ')[-1]

    else:
        out_string = tmp.stderr

    out_string = out_string.replace('salloc', 'valloc')
    if ('-h' in args) or ('--help' in args):
        out_string = out_string + "  -U,  --user                specify the user to submit a job\n"
    print(out_string)

    try:
        _ = requests.post(url, json=json_data)
    except:
        print("request the {} failed!".format(url))

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


def check_version():
    tmp = subprocess.run("slurm --version", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    if len(tmp.stderr) > 0:
        return -1

    return 0


if __name__ == "__main__":
    check_version()
    json_data = {"state": False,
                 "partition": None,
                 "nodes": None,
                 "user": None,
                 "job_name": None,
                 "cmd": "cmd"
                 }
    _ = requests.post('http://192.168.100.109:9999/api/slurmJob/syncSlurmJob', json=json_data)
    p = subprocess.Popen("nvidia-smi", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stderr = p.stderr.read().decode('utf-8')
    if stderr:
        print(f"Error: {stderr.strip()}")
    else:
        while True:
            output = p.stdout.readline().decode('utf-8')
            if output == '' and p.poll() is not None:
                break
            if output:
                print(output.strip())

