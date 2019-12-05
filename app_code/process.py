import pandas as pd
from app_code.fit_equation import get_percentile
from datetime import datetime
from os import path

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
    :returns dataframe:internal representation of csv with standardized column names and row values
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
        df.to_csv(_get_file_name(), index=False)
    else:
        df.to_csv(output, index=False)


def _get_percentiles(df, source):
    """
    Get percentile values based on user defined source

    :param df:standardized dataframe
    :param source:data source to get percentiles from -- options: fit_data, shiny_data
    :returns df:dataframe with percentile values added
    """

    if (source == 'fit-data') or (source == 'KUMC'):  # TODO fix this once names are established
        for index, row in df.iterrows():
            percentile = get_percentile(row['sex'], row['age'], row['vomax'])
            df.loc[index, 'percentile'] = percentile

    elif source == 'shiny-data':
        # TODO
        print('This source integration is still in progress')
        quit()

    return df


def _standardize_sex(df):
    """
    Fix sex column in data frame so all values are standardized

    :param df:dataframe of csv with standardized columns
    :returns df:df with standardized values for sex column
    """

    df.replace(_male_row_values, 'm')
    df.replace(_female_row_values, 'f')

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
        elif 'age' in col:
            pass
        else:
            raise ValueError('Column name not recognized {}'.format(col))

    df = df.rename(columns=rename)
    formatted_df = df[_default_cols]

    return formatted_df


def _get_file_name():
    """
    Generate the output file name and place it in output directory.
    Note: there is probably a better way to do this using relative file paths
          but I couldn't get it working with out setting cwd

    :returns file_path:the path of the output file
    """

    file_name = str(datetime.date(datetime.today())) + '.csv'
    file_path = path.abspath(path.join(path.dirname(__file__), '..', 'output', file_name))

    return file_path
