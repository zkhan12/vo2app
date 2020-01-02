import pandas as pd
import os


def get_percentile(df, exclusion):
    '''
    Gives percentiles based on sex, age, and vo2 max score. Percentiles can be based on
    data with obese and smoking participants exluded from the reference data set.
    Based on the analysis/data from:
    Rapp et al., 2018 Reference values for peak oxygen uptake: cross-sectional analysis of
    cycle ergometry-based cardiopulmonary exercise tests of 10 090 adult German volunteers
    from the Prevention First Registry.
    Paper can be found at: https://bmjopen.bmj.com/content/8/3/e018697.long

    :param df: pandas dataframe containing user data
    :param exclusion: whether user specified output percentiles should be based on exclusion data
    :returns df: pandas dataframe containing user data and percentiles
    '''

    if exclusion:
        m_df = pd.read_csv(os.path.dirname(__file__) + '/su_data/q_m_ex_rel.csv', index_col=0)
        f_df = pd.read_csv(os.path.dirname(__file__) + '/su_data/q_f_ex_rel.csv', index_col=0)
    else:
        m_df = pd.read_csv(os.path.dirname(__file__) + '/su_data/q_m_rel.csv', index_col=0)
        f_df = pd.read_csv(os.path.dirname(__file__) + '/su_data/q_f_rel.csv', index_col=0)

    for index, row in df.iterrows():
        if row['sex'] == 'm':
            percentile = m_df.loc[float(round(row['vomax'], 1)), str(row['age'])]
        elif row['sex'] == 'f':
            percentile = f_df.loc[float(round(row['vomax'], 1)), str(row['age'])]
        else:
            raise ValueError('Selected sex is not an option:', row['sex'])

        df.loc[index, 'percentile'] = round(percentile*100, 1)

    return df
