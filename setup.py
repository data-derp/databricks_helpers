from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="databricks_helpers",
    version="0.1.0",
    description="Data Derp databricks_helpers",
    author="Kelsey Mok",
    author_email="kelseymok@gmail.com",
    url="https://github.com/data-derp/databricks_helpers",
    packages=find_packages("src", exclude=("tests",)),
    package_dir={"": "src"},
    install_requires=required,
    python_requires=">=3.9",
)
