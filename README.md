# Runat: A Tiny Replacement for Crontab as cli command

<img src="https://raw.githubusercontent.com/alivx/crontab-runat/master/other/logo.PNG" alt="logo" style="zoom:50%;" />

Welcome to Runat, a CLI tool that offers a simple and efficient way to replace crontab. It provides a reliable solution for various use cases, including running it inside containers, when crontab is broken, for security compliance, and anything else you may need.

## **Installation**

Runat is easy to install via pip. You can install it using the following command:

```
pip install runat
```

## **Options**

To learn more about Runat's options, you can type **`runat --help`**. The following optional arguments are available:

```
Usage: runat [OPTIONS]

  A tiny replacement for cron for different usages.

  Args:     cron (str): Cron-like syntax string.     do_ (str): List of
  command or shell script.

Options:
  -c, --cron TEXT  Cron like syntax "22 23 * * *"  [required]
  -d, --do TEXT    List of command or shell script  [required]
  --help           Show this message and exit.
```

## **Usage**

Here's how you can use Runat:

```
runat --cron "01 23 * * *"  --do "cd /srv/;bash cleanTemp.sh | tee  -a /var/log/cleanTemp.log"

```

## **Example Output**

Here's an example of what Runat's output might look like:

```
runat --cron "01 23 * * *"  --do "cd /srv/;bash cleanTemp.sh | tee  -a /var/log/cleanTemp.log"
> The next run  in 23.0 hours, 59.0 minutes, 56.0 seconds
```

## **Installation via PyPI**

To install Runat via PyPI, simply run the following command:

```
pip install runat
```

## **Development**

Runat includes a number of helpers in the **`Makefile`** to streamline common development tasks. You can set up your development environment using the following steps:

```
### create a virtualenv for development
$ make virtualenv

$ source env/bin/activate

### run runat cli application
$ runat --help
```

## **Deployments**

### **Docker**

### Note

If you want to work on local file, you should mount it to the container using **`-v`**.

To build and distribute Runat using Docker, you can use the following commands:

```
$ make docker

$ docker run -it runat --help
```

## **License**

Runat is licensed under the GNU GENERAL PUBLIC LICENSE.

## **Author Information**

The tool was originally developed by **[Ali Saleh Baker](https://www.linkedin.com/in/alivx/)**.
