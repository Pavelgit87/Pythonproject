import pytest
from checkers import checkout
import random, string
import yaml
from datetime import datetime

with open('config.yaml') as f:
    # читаем документ YAML
    data = yaml.safe_load(f)


@pytest.fixture() # создает директории
def make_folders():
    return checkout("mkdir -p {} {} {} {}".format(data["folder_in"], data["folder_out"], data["folder_ext"],
                                                  data["folder_ext2"]), "")


@pytest.fixture(autouse=True, scope="module") # затем очищает эти директории
def clear_folders():
    return checkout("rm -rf {}/* {}/* {}/* {}/*".format(data["folder_in"], data["folder_in"], data["folder_ext"],
                                                        data["folder_ext2"]), "")


@pytest.fixture(autouse=True, scope="module") # после создает файлы
def make_files():
    list_of_files = []
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout("cd {}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock".format(data["folder_in"],
                                                                                           filename, data["bs"]), ""):
            list_of_files.append(filename)
    return list_of_files


@pytest.fixture()
def make_bad_arx():
    checkout("cd {}; 7z a {}/bad_arx".format(data["folder_in"], data["folder_out"]), "Everything is Ok")
    checkout("truncate -s 1 {}/bad_arx.7z".format(data["folder_out"]), "")











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
