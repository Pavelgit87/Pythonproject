import random
import string
from datetime import datetime
import pytest
import yaml
from checkers import ssh_checkout, ssh_get
from files import upload_files

with open('config.yaml') as f:
    # читаем документ YAML
    data = yaml.safe_load(f)


@pytest.fixture()  # создает директории
def make_folders():
    return ssh_checkout("0.0.0.0", "user2", "2222",
                        "mkdir -p {} {} {} {}".format(data["folder_in"], data["folder_out"], data["folder_ext"],
                                                      data["folder_ext2"]), "")


@pytest.fixture(autouse=True, scope="module")  # затем очищает эти директории
def clear_folders():
    return ssh_checkout("0.0.0.0", "user2", "2222",
                        "rm -rf {}/* {}/* {}/* {}/*".format(data["folder_in"], data["folder_in"], data["folder_ext"],
                                                            data["folder_ext2"]), "")


@pytest.fixture(autouse=True, scope="module")  # после создает файлы
def make_files():
    list_of_files = []
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if ssh_checkout("0.0.0.0", "user2", "2222",
                        "cd {}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock".format(data["folder_in"],
                                                                                               filename, data["bs"]),
                        ""):
            list_of_files.append(filename)
    return list_of_files


@pytest.fixture()
def make_bad_arx():
    ssh_checkout("0.0.0.0", "user2", "2222",
                 "cd {}; 7z a {}/bad_arx".format(data["folder_in"], data["folder_out"]), "Everything is Ok")
    ssh_checkout("0.0.0.0", "user2", "2222",
                 "truncate -s 1 {}/bad_arx.7z".format(data["folder_out"]), "")


@pytest.fixture(autouse=True, scope="module")
def deploy():
    res = []
    upload_files("0.0.0.0", "user2", "2222",
                 "/home/user/p7zip-full.deb",
                 "/home/user2/p7zip-full.deb")
    res.append(ssh_checkout("0.0.0.0", "user2",
                            "2222", "echo '2222' | sudo -S dpkg -i /home/user2/p7zip-full.deb",
                            "Настраивается пакет"))
    res.append(ssh_checkout("0.0.0.0", "user2", "2222", "echo '2222' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))
    return all(res)



def start_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def safe_log(name, starttime):
    with open(name, 'a') as f:
        f.write(ssh_get("0.0.0.0", "user2", "2222",
                        "journalctl --since {}".format(starttime)))







# @pytest.fixture()
# def make_subfolder():
#     testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
#     subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
#     if not checkout("cd {}; mkdir {}".format(data["folder_in"], subfoldername), ""):
#         return None, None
#     if not checkout("cd {}/{}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["folder_in"],
#                                                                                               subfoldername,
#                                                                                               testfilename), ""):
#         return subfoldername, None
#     else:
#         return subfoldername, testfilename
#
#
# @pytest.fixture(autouse=True)
# def print_time():
#     print("Start: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
#     yield
#     print("Finish: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
