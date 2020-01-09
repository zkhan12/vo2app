from app_code.main import _get_parser
import pytest


def test_parser(simple_csv):
    arg = [str(simple_csv), '-s', 'sf']
    with pytest.raises(SystemExit) as error:
        _get_parser(args=arg)
    assert 2 == error.value.code
