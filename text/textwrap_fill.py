#!/usr/bin/python

import textwrap

from textwrap_example import sample_text

print sample_text

print textwrap.fill(sample_text, width=50)
