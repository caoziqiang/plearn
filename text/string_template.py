#!/usr/bin/python

import string

values = { 'var':'mars' }

t = string.Template("""
Variable	: $var
Escape		: $$
Variable in text : ${var}iable
""")
print 'TEMPLATE', t.substitute(values)

s = """Variable	: %(var)s
Escape		: %%
Variable in text : %(var)siable"""

print 'INTERPOLATION:', s % values

