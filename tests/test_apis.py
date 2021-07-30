from unittest.mock import patch, Mock

from cpu.api import usage


def test_get_cpu_usage():
    """test for get_data_to_be_updated"""
    with patch("cpu.api.psutil") as psutil:
        cpu_percent = Mock()
        cpu_percent().return_value = 10
        psutil.return_value = cpu_percent
        actual_data = usage()
        expected_data = 10
        assert actual_data == expected_data
