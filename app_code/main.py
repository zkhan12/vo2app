from process import process_csv
from argparse import ArgumentParser
from argparse import RawTextHelpFormatter


def _get_parser():
    """
    Build the parser for command line utilities

    :returns parser:contains options for command line
    """

    parser = ArgumentParser(description='vo2 percentile arguments',
                            formatter_class=RawTextHelpFormatter)

    parser.add_argument('input', help='The path of the input csv with '
                        'sex, age, and vo2 columns')

    parser.add_argument('-o', '-output', default='none',
                        help='Optional path of output csv')

    parser.add_argument('-s', '-source', default='KUMC',
                        choices=['KUMC', 'shiny-data'],
                        help='Data source to get percentiles from, default is KUMC')

    return parser


def main():
    """
    Filter command line options
    """

    opts = _get_parser().parse_args()  # get options from command line

    if opts.input[-4:] != '.csv':
        raise IOError('Input file is not a csv')

    if opts.o != 'none':
        if opts.o[-4:] != '.csv':
            raise IOError('Output file is not a csv')

    process_csv(opts.input, opts.o, opts.s)


if __name__ == '__main__':
    main()
