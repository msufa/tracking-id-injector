import os
import sys
from mock import patch
from bs4 import BeautifulSoup
from tridinjector import injector


def test_injection(tmpdir):
    tracking_tag = "my_tracking_tag"
    outfile_path = str(tmpdir.join("out.html"))
    test_args = ["script.py",
                 tracking_tag,
                 os.path.join(os.path.dirname(__file__), "data/test.html"),
                 outfile_path]
    with patch.object(sys, 'argv', test_args):
        injector.main()

        with open(outfile_path, "r") as outfile:
            soup = BeautifulSoup(outfile, "html.parser")
            found = soup.find_all("script")
            assert found
            assert tracking_tag in found[0].text


def test_removing_stray_tags():
    with open(os.path.join(os.path.dirname(__file__), "data/test.html"), "r") as infile:
        soup = BeautifulSoup(infile, "html.parser")
        embed_tag = soup.new_tag("embed")
        soup.body.append(embed_tag)

        output = soup.prettify()
        assert "</embed>" in output
        assert "</embed>" not in injector._remove_stray_tags(output)
