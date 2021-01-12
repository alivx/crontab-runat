from setuptools import setup, find_packages


f = open("README.md", "r")
LONG_DESCRIPTION = f.read()
f.close()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("VERSION") as f:
    VERSION = f.read().splitlines()[0]


setup(
    name="runat",
    version=VERSION,
    description="Cli like cron, to run task a specific time",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    setup_requires=requirements,
    author="Ali Saleh Baker",
    author_email="alivxlive@gmail.com",
    url="https://github.com/alivx/runat",
    license="GNU",
    packages=find_packages(exclude=["ez_setup", "tests*"]),
    package_data={"runat":["templates/*"]},
    include_package_data=True,
    keywords=["cron", "at", "timer", "time", "cli"],
    entry_points="""
        [console_scripts]
        runat = runat.main:main
    """,
)
