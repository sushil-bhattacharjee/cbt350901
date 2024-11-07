import setuptools

with open("readme.md", "r") as fh:
  long_description = fh.read()
  
setuptools.setup(
  name="example-pkg-sushil.bhattacarjee",
  version="1.1.0",
  author="Sushil Bhattacharjee",
  author_email="sushil.bhattacharjee@outlook.com",
  description="A simple API and Router Class",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/DataKnox/CodeSamples/tree/master/Python/AppDev",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3.8",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  install_requires=['flask'],
  python_requires='>=3.8'
)