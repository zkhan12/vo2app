import pandas as pd
from app_code.kumc import get_percentile as get_percentile_kumc
from app_code.su import get_percentiles as get_percentiles_su
from datetime import datetime
import os

_default_cols = ['sex', 'age', 'vomax']

_sex_col_names = ('sex', 'SEX', 'Sex')
_age_col_names = ('age', 'AGE', 'Age')
_vo2_col_names = ('vo2', 'VO2', 'Vo2', 'relative vo2', 'RELATIVE VO2', 'Relative Vo2',
                  'Relative VO2', 'vomax')

_male_row_values = ['m', 'male', 'MALE', 'Male', 'M']
_female_row_values = ['f', 'female', 'FEMALE', 'Female', 'F']


def process_csv(path, output, source):
    """
    Reads in .csv file and processes it before adding percentiles

    :param path:location of file
    :returns path:file path of output csv with percentiles
    """

    df = pd.read_csv(path, header=None)

    top_row = df.iloc[0, :]
    header_exists = not any(cell.isdigit() for cell in top_row)  # ensure top row cells aren't nums

    if header_exists:
        df = pd.read_csv(path, header=(0))
        df = _standardize_cols(df)

    else:
        df.columns = _default_cols  # assume default columns for header

    df = _standardize_sex(df)

    df = _get_percentiles(df, source)

    if output == 'none':
        output_path = _get_file_name()
    else:
        output_path = output

    df.to_csv(output_path, index=False)

    return(output_path)


def _get_percentiles(df, source):
    """
    Get percentile values based on user defined source

    :param df:standardized dataframe
    :param source:data source to get percentiles from -- options: fit_data, shiny_data
    :returns df:dataframe with percentile values added
    """

    if source.lower() == 'kumc':
        for index, row in df.iterrows():
            percentile = get_percentile_kumc(row['sex'], row['age'], row['vomax'])
            df.loc[index, 'percentile'] = percentile

    elif (source.lower() == 'su') or (source.lower() == 'su-ex'):
        df = get_percentiles_su(df, source.lower() == 'su-ex')

    return df


def _standardize_sex(df):
    """
    Fix sex column in data frame so all values are standardized

    :param df:dataframe of csv with standardized columns
    :returns df:df with standardized values for sex column
    """

    df = df.replace(_male_row_values, 'm')
    df = df.replace(_female_row_values, 'f')

    return df


def _standardize_cols(df):
    """
    Fix data frame columns so they are standardized

    :param df:dataframe of csv with custom columns
    :returns formatted_df:df with proper col names and order for further processing
    """

    header = df.columns
    rename = {}

    for col in header:
        if col in _sex_col_names:
            rename[col] = 'sex'
        elif col in _age_col_names:
            rename[col] = 'age'
        elif col in _vo2_col_names:
            rename[col] = 'vomax'
        else:
            raise ValueError('Column name not recognized {}'.format(col))

    df.rename(columns=rename, inplace=True)
    formatted_df = df[_default_cols]

    return formatted_df


def _get_file_name():
    """
    Generate the output file name and place it in the current working directory.

    :returns file_path:the path of the output file
    """

    file_name = str(datetime.date(datetime.today())) + '.csv'
    file_path = os.getcwd() + '/' + file_name

    return file_path
