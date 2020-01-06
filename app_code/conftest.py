""" Creation of objects to be used for multiple tests """
import pandas as pd
import pytest


@pytest.fixture(scope='session')
def simple_csv(tmp_path_factory):
    csv_dir = tmp_path_factory.mktemp("csv")
    csv_fname = "sample.csv"
    csv_path = csv_dir / csv_fname
    data_dict = {
        'sex': ['m', 'm', 'f', 'm'],
        'age': [22, 45, 22, 44],
        'vo2': [35.1, 35.72, 30.3, 38.05]
    }
    df = pd.DataFrame.from_dict(data_dict)
    df.to_csv(csv_path, index=False, sep=',')

    return csv_path
