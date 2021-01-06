######################################################################
#
# File: b2/version.py
#
# Copyright 2019 Backblaze Inc. All Rights Reserved.
#
# License https://www.backblaze.com/using_b2_code.html
#
######################################################################

from importlib.metadata import version, PackageNotFoundError

try:
    VERSION = version('b2')
except PackageNotFoundError:
    VERSION = '0.0.0'
