import sys
import argparse
import logging

# create logger
logger = logging.getLogger("harlemnext-assessment")
logger.setLevel(logging.INFO)

def parse_args(args):
    try:
        parser = argparse.ArgumentParser(description="Harlem Next Assessment", formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument("--password", "-p", type=str, 
        help="""a. At least 1 letter between [a-z]
b. At least 1 numbr between [0-9]
c. At least 1 letter between [A-Z]
d. At least 1 special character within [$%%#]
e. At least 6 characters long but not more than 12 characters
Eg.: python main.py -p s0m3#%%P4$$wD""")
        return parser.parse_args(args)
    except SystemExit as err:
        logger.error(f"Can't find all arguments: Error code [{err}]")
        raise SystemExit()

if __name__ == "__main__":

    # Get args
    args = parse_args(sys.argv[1:])
