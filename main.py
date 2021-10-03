import argparse
import configparser
import sys
import yaml
from datetime import datetime

def add_numbers(number, other_number, output):
    result = number * other_number
    print(f'[{datetime.utcnow().isoformat()}] The result is {result}', file=output)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(formatter_class=argparse.rgumentDefaultsHelpFormatter)

    parser.add_argument('--config', '-c', type=argparse.FileType('r'), help='config file', default='/etc/automate.ini')
    # Added Argument Parsing Functionality
    parser.add_argument('-o', dest='output', type=argparse.FileType('w'), help='output file', default=sys.stdout)

    args = parser.parse_args()

    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)
        # Transforming values into integers
        args.n1 = int(config['ARGUMENTS']['n1'])
        args.n2 = int(config['ARGUMENTS']['n2'])

    add_numbers(args.n1, args.n2, args.output)
