import sys
import time
import os
import click
from datetime import datetime, timedelta

class CronParser:
    def __init__(self, cron_expression):
        self.fields = cron_expression.split()

    def get_next(self, start_time):
        dt = start_time
        while True:
            dt += timedelta(minutes=1)
            if all(self._match_field(dt, field, index) for index, field in enumerate(self.fields)):
                return dt

    @staticmethod
    def _match_field(dt, field, index):
        if field == '*':
            return True
        else:
            if index == 0:
                return dt.minute in map(int, field.split(','))
            elif index == 1:
                return dt.hour in map(int, field.split(','))
            elif index == 2:
                return dt.day in map(int, field.split(','))
            elif index == 3:
                return dt.month in map(int, field.split(','))
            elif index == 4:
                return dt.weekday() in map(int, field.split(','))
        return False
    
    

# Convert seconds to a human-readable time string
def display_time(seconds, granularity=3):
    """
    Convert seconds to a human-readable time string.

    Args:
        seconds (int): Number of seconds.
        granularity (int): Number of time units to display.

    Returns:
        str: Human-readable time string.
    """
    intervals = (
        ("weeks", 604800),
        ("days", 86400),
        ("hours", 3600),
        ("minutes", 60),
        ("seconds", 1),
    )
    result = []

    # Calculate time units and append to the result list
    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip("s")
            result.append("{} {}".format(value, name))

    return ", ".join(result[:granularity])

# Execute a shell command and print its output
def run_command(command):
    """
    Execute a shell command and print its output.

    Args:
        command (str): Shell command to execute.
    """
    try:
        stream = os.popen(command)
        output = stream.read()
        print(output)
    except Exception as e:
        print(f"There is an error with command {command}: {e}")
        sys.exit(1)
        
        
@click.command()
@click.option("-c", "--cron", required=True, type=str, help='Cron like syntax "22 23 * * *"')
@click.option("-d", "--do", "do_", required=True, type=str, help="List of command or shell script")
def main(cron, do_):
    """
    A tiny replacement for cron for different usages.

    Args:
        cron (str): Cron-like syntax string.
        do_ (str): List of command or shell script.
    """
    cron_parser = CronParser(cron)

    try:
        while True:
            # Calculate next run time and wait
            nextrun = cron_parser.get_next(datetime.now())
            wait_time = (nextrun - datetime.now()).total_seconds()
            print(f"> The next run in {display_time(wait_time)}")
            time.sleep(wait_time)

            # Execute the command
            run_command(do_)
    except Exception as e:
        print(e)
    finally:
        print("\nInterpreted")
        time.sleep(0.5)
        sys.exit(1)

if __name__ == "__main__":
    main()