import sys
import argparse
import time
import os
from crontab import CronTab

# Create the parser
aParser = argparse.ArgumentParser(
    description="tiny replacement cron for different usages"
)
# Add the arguments
aParser.add_argument(
    "--cron", "-c", required=True, type=CronTab, help='cron like syntax "22 23 * * *"'
)
aParser.add_argument(
    "--do", "-d", required=True, type=str, help="list of command or shell script"
)
aParser.add_argument(
    "--utc",
    "-u",
    default=False,
    help="Use UTC time",
    action="store_true",
)
args = aParser.parse_args()


# Check if no arg, show help and exit
if len(sys.argv) < 2:
    aParser.print_usage()
    sys.exit(1)

# Arg var
cron = args.cron
do = args.do
utc = args.utc

intervals = (
    ("weeks", 604800),
    ("days", 86400),
    ("hours", 3600),
    ("minutes", 60),
    ("seconds", 1),
)


def display_time(seconds, granularity=3):
    """Convert seconds to readable time

    Args:
        seconds int: seconds
        granularity int: item count

    Returns:
        str: time in readable format
    """
    result = []
    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip("s")
            result.append("{} {}".format(value, name))
    return ", ".join(result[:granularity])


def runCommand(command):
    """Run shell command

    Args:
        command str: shell script
    """
    try:
        stream = os.popen(do)
        output = stream.read()
        print(output)
    except Exception as e:
        print("There is an error with command {0}".format(command))
        sys.exit(1)

def main():
    try:
        while True:
            nextrun = args.cron.next(default_utc=utc)
            print("> The next run  in {}".format(display_time(nextrun)))
            time.sleep(args.cron.next(default_utc=utc))
            runCommand(do)
    finally:
        print("\nInterpreted")
        time.sleep(0.5)
        sys.exit(1)

if __name__ == "__main__":
    main()