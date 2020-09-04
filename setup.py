from setuptools import setup

setup(name="lambda_swapi",
      version="2.0.0",
      description="A small program to determine in which movies two selected Star Wars characters appear",
      author="Daniel Palacio",
      packages=["packages", "tests"],
      install_requires=["python>=3.7.4",
                        "fuzzywuzzy"])
