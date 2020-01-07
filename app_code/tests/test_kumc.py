from app_code.kumc import get_percentile
import numpy as np
import pandas as pd


def test_get_percentile_kumc(simple_csv):
    df = pd.read_csv(simple_csv, header=(0))
    targets = np.array([10.65, 23.94, 12.83, 34.66])
    actual = np.array([])

    for index, row in df.iterrows():
        actual = np.append(actual, get_percentile(row['sex'], float(row['age']), float(row['vomax'])))

    assert np.array_equal(targets, actual)
