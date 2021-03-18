#!/usr/bin/env python3

import unittest
import sys
from markdownanchormaker import get_pretty_title
from markdownanchormaker import anchor_maker
from markdownanchormaker import replace_spaces_with_dashes
from markdownanchormaker import drop_unwanted_chars
from markdownanchormaker import prepend_octothorpe
from markdownanchormaker import parenthesis_surround
from markdownanchormaker import remove_leading_dashes
from markdownanchormaker import make_lowercase


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
    
    def test_replace_spaces_with_dashes(self):
        """
        Test that spaces are replaced with dashes
        """
        data = "foo bar baz"
        result = replace_spaces_with_dashes(data)
        # Test that there are no spaces
        self.assertNotRegex(result, r"(?= )")

    def test_drop_unwanted_chars(self):
        data = "-  ^Foo* ?baR <baz "
        result = drop_unwanted_chars(data)
        # Test that there are no "special" characters
        self.assertNotRegex(result, r"(?=[!@$%^&*<>\[\]\{\};:\"'])")

    def test_prepend_octothorpe(self):
        data = "Foo ?baR <baz "
        result = prepend_octothorpe(data)
        # Test that the string starts with #
        self.assertRegex(result, r"^#")

    def tet_parenthesis_surround(self):
        data = "# Test Title"
        result = parenthesis_surround(data)
        # Test that result starts with ( and ends with )
        self.assertRegex(result, r"^\(.*?\)$")

    def test_remove_leading_dashes(self):
        data = "(#-Foo ?baR <baz "
        result = remove_leading_dashes(data)
        # Test that the string doesn't contain dashes between (# and first letter
        self.assertNotRegex(result, r"^\(#[-]+")

    def test_make_lowercase(self):
        data = "UPPERCASE"
        result = make_lowercase(data)
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
