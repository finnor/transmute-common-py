import setuptools

setuptools.setup(
  name="transmute-common",
  version="0.0.2",
  author="Adrian Flannery",
  author_email="aflannery@uabmc.edu",
  description="A package to support ETL creation within Transmute",
  url="https://github.com/finnor/transmute-common-py",
  packages=setuptools.find_packages(),
  classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)