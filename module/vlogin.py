import os


def login():
    user_name = input("enter the username to login: ")
    # login & get passwd
    if_user = True

    if if_user:
        try:
            if not os.path.exists("/root/.vlogin/"):
                os.makedirs("/root/.vlogin/")

            if len(os.listdir("/root/.vlogin/")) > 0:
                for each in os.listdir("/root/.vlogin/"):
                    os.remove("/root/.vlogin/"+each)

            with open("/root/.vlogin/"+user_name+".txt", "w") as f:
                print("******successfully login!******")
                return True
        except:
            return False

    else:
        print("ERROR: password error, failed to login!")
        return False


if __name__ == "__main__":
    login()
