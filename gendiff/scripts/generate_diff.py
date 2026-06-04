import os

from gendiff.scripts.difference import build_diff_tree
from gendiff.formatters import apply_formatter
from gendiff.scripts.parser import parse


def generate_diff(file_path1, file_path2, format_name='stylish'):
    content1, content2 = map(_get_content, (file_path1, file_path2))
    diff_tree = build_diff_tree(content1, content2)
    return apply_formatter(diff_tree, format_name)


def _get_content(file_path):
    _, extension = os.path.splitext(file_path)
    with open(file_path) as input_file:
        return parse(input_file, extension)
