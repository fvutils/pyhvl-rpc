
import os
from setuptools import setup, find_namespace_packages

version="0.0.1"

setup(
  name="pyhvl-rpc",
  version=version,
  packages=find_namespace_packages(where='src'),
  package_dir={'' : 'src'},
  author="Matthew Ballance",
  author_email="matt.ballance@gmail.com",
  description=("pyhvl-rpc provides remote procedure call (RPC) infrastructure for functional verification"),
  license="Apache 2.0",
  keywords = ["Python", "Functional Verification"],
  url = "https://github.com/fvutils/pyhvl-rpc",
  entry_points={
    'console_scripts': [
      'hvlrpc = hvlrpc.__main__:main'
    ]
  },
  setup_requires=[
    'setuptools_scm',
    'wheel',
    'numpy'
  ],
  install_requires=[
    'colorama',
    'numpy'
  ],
)

