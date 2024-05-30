import os


def logout():
    for each in os.listdir("/root/.vlogin/"):
        os.remove("/root/.vlogin/"+each)
