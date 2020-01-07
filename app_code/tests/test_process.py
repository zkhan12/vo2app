""" tests for process.py """
import os
import pytest
from app_code.process import process_csv


@pytest.mark.parametrize(
    "fname,source",
    [
        ("output_kumc.csv", "kumc"),
        ("output_su.csv", "su"),
        ("output_su-ex.csv", "su-ex"),
    ]
)
def test_process_csv(tmp_path, simple_csv, fname, source):
    output = tmp_path / fname
    path = process_csv(simple_csv, output, source)

    assert os.path.isfile(output) and (str(path) == str(output))
