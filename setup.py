#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2022-2022 Caeden

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import pathlib

from setuptools import setup


ROOT = pathlib.Path(__file__).parent
with open(ROOT / "README.md", "r", encoding="utf-8") as f:
    README = f.read()
with open(ROOT / "requirements.txt", "r", encoding="utf-8") as f:
    REQUIREMENTS = f.read().splitlines()
VERSION = __import__("disdata.__init__").__version__

setup(
    name="disdata",
    author="Caeden",
    url="https://github.com/CaedenPH/disdata",
    license="MIT",
    description="A database for discord bots coded in disnake - easy to set up, maintain and interact with",
    long_description=README,
    long_description_content_type="text/markdown",
    project_urls={
        "Code": "https://github.com/CaedenPH/disdata",
    },
    version=VERSION,
    packages=["disdata", "disdata.models"],
    include_package_data=True,
    install_requires=REQUIREMENTS,
    python_requires=">=3.8.0",
    download_url=f"https://github.com/CaedenPH/disdata/archive/refs/tags/v_{VERSION.replace('', '')}.tar.gz",
    keywords="disnake discord python database structure easyusage",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Communications :: Chat",
        "Topic :: Internet",
        "Topic :: Utilities",
    ],
)
