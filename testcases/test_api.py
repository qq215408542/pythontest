import pytest

from commons.yaml_util import write_yaml, read_yaml, clear_yaml


class TestApi:

    @pytest.mark.smoke
    def test_login(self):
        nummm = {"aaa": "cctv"}
        write_yaml(nummm)



    @pytest.fixture(scope="function",autouse=True)
    def setup(self):
        print("开始了")
        yield
        print("好啊")

    @pytest.fixture(scope="session",autouse=True)
    def setup(self):
        clear_yaml()
        yield
        print(read_yaml("aaa"))
