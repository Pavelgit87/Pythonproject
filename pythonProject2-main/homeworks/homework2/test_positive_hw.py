import subprocess
# from zlib import crc32

tst = "/home/user/tst"
out = "/home/user/out"
folder1 = "/home/user/folder1"
folder2 = "/home/user/folder2"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def hash_func(cmd):
    return subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8').stdout

# create txt, folder 1, out, folder2
# create "one", "two" in txt


def test_step1():
    # test1 =================== create archive arx2.7z (docs from tst) in out
    result1 = checkout("cd {}; 7z a {}/arx2".format(tst, out), "Everything is Ok")
    # check if arx2.7z in out
    result2 = checkout("cd {}; ls".format(out), "arx2.7z")
    assert result1 and result2, "Test1 FAIL"


def test_step2():
    # test2 ======== take docs from archive in out and past docs to folder1
    result1 = checkout("cd {}; 7z e arx2.7z -o{} -y".format(out, folder1), "Everything is Ok")
    result2 = checkout("cd {}; ls".format(folder1), "one")
    result3 = checkout("cd {}; ls".format(folder1), "two")
    assert result1 and result2 and result3, "Test2 FAIL"


def test_step3():
    # test find smth in out
    result1 = checkout("cd {}; 7z l arx2.7z".format(out), "")
    result2 = checkout("cd {}; 7z l arx2.7z".format(out), "one")
    result3 = checkout("cd {}; 7z l arx2.7z".format(out), "two")
    assert result1 and result2 and result3, "Test3 FAIL"


def test_step4():
    # test2 ======== take docs from archive in out and past docs to folder2 (no rewrite if docs are already in folder2)
    result1 = checkout("cd {}; 7z x arx2.7z -o{}".format(out, folder2), "Everything is Ok")
    result2 = checkout("cd {}; ls".format(folder2), "one")
    result3 = checkout("cd {}; ls".format(folder2), "two")
    assert result1 and result2 and result3, "Test4 FAIL"


def test_step6():
    # test6 =========show info about arx2.7z
    assert checkout("cd {}; 7z t arx2.7z".format(out), "Everything is Ok"), "Test6 FAIL"


def test_step7():
    # test7 ========= add archive update
    assert checkout("cd {}; 7z u {}/arx2.7z".format(tst, out), "Everything is Ok"), "Test7 FAIL"


def test_hash_step8():
    result1 = hash_func('cd {}; crc32 arx2.7z'.format(out).upper())
    result2 = hash_func('cd {}; 7z h arx2.7z'.format(out))
    assert result1 in result2, 'Test8 Fail'

# def test_hash_step8():
#     result1 = crc32("{}/arx2.7z".format(out)).lower()
#     assert checkout("crc32 {}/arx2.7z".format(out), result1), "Test8 FAIL"


def test_step9():
    # test8 ========= delete docs one and two from archive in folder out
    assert checkout("cd {}; 7z d arx2.7z".format(out), "Everything is Ok"), "Test9 FAIL"



