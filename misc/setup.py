#!/usr/bin/env python

from distutils.core import setup
import py2exe

setup(
    windows = [
        {
            "script": "kmlWriter.py",
            "icon_resources": [(1, "comma.ico")]
        }
    ],
)