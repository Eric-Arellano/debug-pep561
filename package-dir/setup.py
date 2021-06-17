from setuptools import setup

setup(
  name="dist",
  version="0.1",
  package_dir={"": "src"},
  package_data={"mypkg": ["py.typed"]},
  packages=["mypkg"],
)

