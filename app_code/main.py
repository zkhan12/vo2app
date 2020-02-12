from app_code.process import process_csv
from argparse import ArgumentParser
from argparse import RawTextHelpFormatter


def _get_parser(args=None):
    """
    Build the parser for command line utilities

    :returns parser:contains options for command line
    """

    parser = ArgumentParser(description='vo2 percentile arguments',
                            formatter_class=RawTextHelpFormatter)

    parser.add_argument('-i', '-input', help='path of the input csv with '
                        'sex, age, and vo2 columns', required=True)

    parser.add_argument('-o', '-output', default='none',
                        help='optional path of output csv')

    parser.add_argument('-s', '-source', default='kumc',
                        choices=['kumc', 'su', 'su-ex'],
                        help='data source to get percentiles from, default is kumc')

    return parser.parse_args(args)


def main():
    """
    Filter command line options
    """

    opts = _get_parser()  # get options from command line

    if opts.i[-4:] != '.csv':
        raise IOError('Input file is not a csv')

    if opts.o != 'none':
        if opts.o[-4:] != '.csv':
            raise IOError('Output file is not a csv')

    process_csv(opts.i, opts.o, opts.s)


if __name__ == '__main__':
    main()
