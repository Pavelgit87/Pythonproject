from checkout import checkout_negative
import yaml
from conftest import data


def test_step8(write_stat_file):
    # test8
    assert checkout_negative("cd {}; 7z e badarx.7z -o{} -y".format(data['folder_out'], data['folder_ext']),
                             "ERROR"), "Test8 Fail"


def test_step9(write_stat_file):
    # test9
    assert checkout_negative("cd {}; 7z t badarx.7z".format(data['folder_out']), "ERROR"), "Test9 Fail"