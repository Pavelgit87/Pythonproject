from checkers import checkout, getout
import yaml

with open('config.yaml') as f:
    # читаем документ YAML
    data = yaml.safe_load(f)

class TestPositive: #pytest -v ./test_positive.py::TestPositive::test_step1

    def test_step1(self):
        # test1
        res1 = checkout("cd {}; 7z a {}/arx2".format(data["folder_in"], data["folder_out"]), "Everything is Ok")
        res2 = checkout("cd {}; ls".format(data["folder_out"]), "arx2.7z")
        assert res1 and res2, "test1 FAIL"

    def test_step2(self, make_files):
        # test2
        res1 = checkout("cd {}; 7z e arx2.7z -o{} -y".format(data["folder_out"], data["folder_ext"]), "Everything is Ok")
        res2 = checkout("cd {}; ls".format(data["folder_ext"]), make_files[0])
        assert res1 and res2, "test2 FAIL"

    def test_step3(self):
        # test3
        assert checkout("cd {}; 7z t arx2.7z".format(data["folder_out"]), "Everything is Ok"), "test3 FAIL"

    def test_step4(self):
        # test4
        assert checkout("cd {}; 7z u {}/arx2.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"), "test4 FAIL"

    def test_step5(self, clear_folders, make_files):
        # test5
        assert checkout("cd {}; 7z d arx2.7z".format(data["folder_out"]), "Everything is Ok"), "test5 FAIL"


