#!/usr/bin/env python

from setuptools import setup

setup(name='git_lambda',
      version='1.1.1',
      description='A compiled binary of git for use in AWS Lambda',
      author='Benjamin Congdon',
      author_email='me@bcon.gdn',
      url='https://github.com/bcongdon/git_lambda',
      packages=['git_lambda'],
      include_package_data=True
      )
