from app_code.su import get_percentiles
import pandas as pd
import numpy as np


def test_get_percentile_su(simple_csv):
    df = pd.read_csv(simple_csv, header=(0))
    out_df = get_percentiles(df, False)
    target_percentiles = np.array([19.3, 49.7, 27.0, 60.0])
    assert np.array_equal(out_df.loc[:, 'percentile'].values,
                          pd.Series.from_array(target_percentiles).values)

def test_get_percentile_su_ex(simple_csv):
    df = pd.read_csv(simple_csv, header=(0))
    out_ex_df = get_percentiles(df, True)
    target_ex_percentiles = np.array([18.6, 41.6, 25.3, 53.0])
    assert np.array_equal(out_ex_df.loc[:, 'percentile'].values,
                          pd.Series.from_array(target_ex_percentiles).values)
