from checkers import checkout_negative
import yaml

with open('config.yaml') as f:
    # читаем документ YAML
    data = yaml.safe_load(f)


class TestNegative:

    def test_step1(self, make_bad_arx):
        # test1 ======== take docs from folder: out and copy this docs to folder1
        assert checkout_negative("cd {}; 7z e bad_arx.7z -o{} -y".format(data["folder_out"],
                                                                         data["folder_ext"]), "ERRORS"), "Test1 FAIL"

    def test_step2(self):
        # test2 =========show info about arx2.7z
        assert checkout_negative("cd {}; 7z t bad_arx.7z".format(data["folder_out"]), "ERRORS"), "Test2 FAIL"


