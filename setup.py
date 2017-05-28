import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()


required = [
    'vanilla==0.1.16'
]

setup(name='file_count',
      version=read('VERSION'),
      author="Francisco Huertas",
      author_email="francisco@fhuertas.com",
      license="Apache2",
      packages=["file_count"],
      description="Read properties of big files",
      long_description=read('README.md'),
      url='https://github.com/fhuertas/python_file_count',
      download_url="https://github.com/fhuertas/python_file_count/tarball/{}".format(read('VERSION')),
      install_requires=required,
      classifiers=[
          "Development Status :: 1 - Planning",
          "Topic :: Scientific/Engineering",
          "License :: OSI Approved :: Apache Software License",
          'Programming Language :: Python :: 3',
      ])
