#!/usr/bin/env python3

import unittest
import sys
from markdownanchormaker import get_pretty_title
from markdownanchormaker import anchor_maker
from markdownanchormaker import output_title_and_link

class TestGetPrettyTitle(unittest.TestCase):

    def test_result_not_startswith_octothorpe(self):
        """
        Test that result doesn't start with a #; ie the # is removed
        """
        data = "# Test Title"
        result = get_pretty_title(data)
        self.assertRegex(result, r"^[^#]")

    def test_handles_multiple_spaces_after_octothorpe(self):
        """
        Test that get_pretty_title() can handle multiple spaces after # in
        a title, and that those extra spaces are stripped off
        """
        data = "#   Title With Extra Whitespace"
        result = get_pretty_title(data)
        self.assertRegex(result, r"^(?:[^\s]+)")

class TestAnchorMaker(unittest.TestCase):

    def test_anchor_maker(self):
        """
        Test that there are no spaces
        Test that "special" characters are dropped
        Test that the string starts with (# and ends with )
        Test that the string doesn't contain dashes between # and first letter
        Test that the string is all lowercase
        """
        data = "-  Foo ?baR <baz "
        result = anchor_maker(data)
        # Test that there are no spaces
        self.assertNotRegex(result, r"(?= )")
        # Test that there are no "special" characters
        self.assertNotRegex(result, r"(?=[!@$%^&*<>\[\]\{\};:\"'])")
        # Test that the string starts with (# and ends with )
        self.assertRegex(result, r"^\(#.*?\)$")
        # Test that the string doesn't contain dashes between # and first letter
        self.assertNotRegex(result, r"^\(#[-]+")
        # Test that the string is all lowercase
        self.assertNotRegex(result, r"(?=[A-Z])")

class TestOutputTitleAndLink(unittest.TestCase):

    def test_startswith_bracket(self):
        data_pretty_part = "[Three Octothorpe Title]"
        data_anchor_link = "(#three-octothorpe-title)"
        result = output_title_and_link(data_pretty_part, data_anchor_link)
        self.assertRegex(result, r"^\[")

    def test_endswith_parenthesis_and_two_spaces(self):
        # output_title_and_link() adds two spaces at end for Markdown newlines
        data_pretty_part = "[Three Octothorpe Title]"
        data_anchor_link = "(#three-octothorpe-title)"
        result = output_title_and_link(data_pretty_part, data_anchor_link)
        self.assertRegex(result, r"\)  $")

if __name__ == "__main__":
    options = [sys.argv[0]]
    unittest.main(argv=options)
