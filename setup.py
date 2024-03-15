from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="run-the-world",
    version="1",
    description="Cli Bot assistance for managing contacts and notes",
    long_description=long_description,
    url="https://github.com/TatianaSnisarenko/project-run-the-world",
    author="Tetiana Snisarenko, Olha Arzhanova, Daria Honcharuk, Lesia Katanova, Olena Deineha",
    license="MIT",
    packages=find_namespace_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "prompt-toolkit", "tabulate", "Pygments"
    ],
    entry_points={"console_scripts": ["run_bot = assistant:main"]}
)
