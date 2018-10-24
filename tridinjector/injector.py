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


def _parse_input(input_filename):
    with open(input_filename, 'r') as infile:
        return BeautifulSoup(infile, "html.parser")


def _inject_tracking_id(tracking_id, soup):
    tracking_script = soup.new_tag("script")
    tracking_script.string = TRACKING_SCRIPT_TEMPLATE.format(tracking_id)
    soup.head.append(tracking_script)


def _write_output(soup, output_filename):
    with open(output_filename, 'w') as outfile:
        outfile.write(soup.prettify().encode('utf-8'))


def main():
    if len(sys.argv) < 4:
        print('usage: tracking-id-injector tracking_id input_filename output_filename')
        exit(1)

    soup = _parse_input(sys.argv[2])
    _inject_tracking_id(sys.argv[1], soup)
    _write_output(soup, sys.argv[3])


if __name__ == '__main__':
    main()
