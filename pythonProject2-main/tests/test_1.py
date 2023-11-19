import subprocess

import pytest


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
    # test1
    assert checkout("cat /etc/os-release", "22.04.1 LTS (Jammy Jellyfish)"), "FAIL"

# @pytest.mark.run_this
def test_step2():
    # test1
    assert checkout("cat /etc/os-release", "22.04.1 LTS (Jammy Jellyfish)"), "FAIL"
    print("Hello")


