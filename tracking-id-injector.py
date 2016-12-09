#!/usr/bin/python

import sys
from bs4 import BeautifulSoup

TRACKING_SCRIPT_TEMPLATE = """
(function(i,s,o,g,r,a,m){{i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){{
(i[r].q=i[r].q||[]).push(arguments)}},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
}})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
ga('create', '{0}', 'auto');
ga('send', 'pageview');
"""

if len(sys.argv) < 4:
    print('usage: python {0} tracking_id input_filename output_filename'.format(sys.argv[0]))
    exit(1)

with open(sys.argv[2], 'r') as infile:
    soup = BeautifulSoup(infile, "html.parser")
    tracking_script = soup.new_tag("script")
    tracking_script.string = TRACKING_SCRIPT_TEMPLATE.format(sys.argv[1])
    soup.head.append(tracking_script)

    with open(sys.argv[3], 'w') as outfile:
        outfile.write(soup.prettify())
