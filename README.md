# Cronlike cli :) 
<img src="https://raw.githubusercontent.com/alivx/runat/master/other/logo.PNG" alt="logo" style="zoom:50%;" />


# runat
Tiny replacement for crontab

## Use Case/Note
* Run it inside container 🥚.
* Your crontab is broken 🐛.
* For security compliance 🔒.
* Anything you mayneed 🚑.


## Notes
* Crontab running on your timezone, if you want to use UTC pass arg --utc

## Option

```
> runat --help
usage: main.py [-h] --cron CRON --do DO [--utc]

tiny replacement cron for different usages

optional arguments:
  -h, --help            show this help message and exit
  --cron CRON, -c CRON  cron like syntax "22 23 * * *"
  --do DO, -d DO        list of command or shell script
  --utc, -u             Use UTC time
```

## Useages
```Bash
runat --cron "01 23 * * *"  --do "cd /srv/;bash cleanTemp.sh | tee  -a /var/log/cleanTemp.log"

#To use UTC time
runat --cron "01 23 * * *"  --do "cd /srv/;bash cleanTemp.sh | tee  -a /var/log/cleanTemp.log" --utc
> The next run  in 1.0 hour, 54.0 minutes, 44.0 seconds
```

## Exmaple output:
```
runat --cron "01 23 * * *"  --do "cd /srv/;bash cleanTemp.sh | tee  -a /var/log/cleanTemp.log"
> The next run  in 23.0 hours, 59.0 minutes, 56.0 seconds
```

## Installation using pypi
```
pip install runat
```

## Installation

```
$ pip install -r requirements.txt

$ pip install setup.py
```

## Development

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

### Environment Setup

The following demonstrates setting up and working with a development environment:

```
### create a virtualenv for development

$ make virtualenv

$ source env/bin/activate


### run runat cli application

$ runat --help


### run pytest / coverage

$ make test
```


### Releasing to PyPi

Before releasing to PyPi, you must configure your login credentials:

**~/.pypirc**:

```
[pypi]
username = YOUR_USERNAME
password = YOUR_PASSWORD
```

Then use the included helper function via the `Makefile`:

```
$ make dist

$ make dist-upload
```

## Deployments

### Docker

#### Note
If you want to work on local file you should mount it to the container using `-v`

Included is a basic `Dockerfile` for building and distributing `Redis Mirror `,
and can be built with the included `make` helper:

```
$ make docker

$ docker run -it runat --help
```