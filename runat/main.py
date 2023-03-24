import sys
import time
import os
import croniter
import click

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

# Main function using click
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
    cron_iter = croniter.croniter(cron, start_time=time.time())

    try:
        while True:
            # Calculate next run time and wait
            nextrun = cron_iter.get_next()
            wait_time = nextrun - time.time()
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
