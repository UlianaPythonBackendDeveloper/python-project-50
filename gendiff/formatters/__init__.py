from gendiff.formatters.stylish import stylish


def apply_formatter(diff_tree, formatter_name):
    if formatter_name == 'stylish':
        return stylish(diff_tree)
    raise ValueError('Invalid format, choose from stylish, plain, json')
