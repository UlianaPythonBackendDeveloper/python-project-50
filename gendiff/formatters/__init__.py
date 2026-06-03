from gendiff.formatters.json_formatter import format_json
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish

FORMATTERS = {
    'stylish': stylish,
    'plain': plain,
    'json': format_json,
}


def apply_formatter(diff_tree, formatter_name):
    formatter = FORMATTERS.get(formatter_name)
    if formatter is None:
        raise ValueError('Invalid format, choose from stylish, plain, json')
    return formatter(diff_tree)
