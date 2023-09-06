#!/usr/bin/env python

import os
import os.path
import sys


def release(source_path, build_path, install_path, targets):
    pass


if __name__ == '__main__':
    release(
        source_path=os.environ['REZ_BUILD_SOURCE_PATH'],
        build_path=os.environ['REZ_BUILD_PATH'],
        install_path=os.environ['REZ_BUILD_INSTALL_PATH'],
        targets=sys.argv[1:]
    )
