import os


def parase_cmd_args(command: str):
    json_data = {"state": False,
                 "partition": None,
                 "nodes": None,
                 "user": None,
                 "job_name": None,
                 "cmd": command
                 }

    command_list = command.replace('=', ' ').split(' ')
    try:
        for ind, part in enumerate(command_list):
            if part in ['-P', '--partition']:
                json_data['partition'] = command_list[ind+1]
                continue

            if part in ['-N', '--nodes']:
                json_data['nodes'] = command_list[ind + 1]
                continue

            if part in ['-J', '--job-name']:
                json_data['job_name'] = command_list[ind + 1]

    except:
        pass

    return json_data


def check_params(params_list=None):
    if params_list is not None:
        for param in params_list:
            assert param in ['', '', '']

    def _check_params(func):
        def wrapper(*args, **kwargs):
            pass
            func(*args, **kwargs)
            pass
        return wrapper
    return _check_params


def check_login(func):
    def wrapper(*args, **kwargs):
        try:
            key_file = os.listdir("/root/.vlogin/")
            if (len(key_file) > 0) and (key_file[0].split('.')[-1] == 'txt'):
                is_login = True
            else:
                is_login = False
        except:
            is_login = False

        if is_login:
            func(*args, **kwargs)
        else:
            print("please login first!")

    return wrapper


def get_index(str_list, key):
    for ind, each in enumerate(str_list):
        if each in key:
            return ind
    return -1


if __name__ == "__main__":
    TMP = "sbatch -N 1 -par=3 -V 1 -S=2 -Z 3"
    print(TMP.replace('=', ' ').split(' '))
