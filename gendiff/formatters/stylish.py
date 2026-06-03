from itertools import chain

from gendiff.utils import resolve_none_and_boolean

SPACES_PER_LEVEL = 4
OFFSET = 2
ROOT_DEPTH = 1


def stylish(diff):
    lines = [_make_line(node, ROOT_DEPTH) for node in diff]
    return '\n'.join(chain('{', lines, ['}']))


def _format_inner(diff, content_depth, close_depth):
    if isinstance(diff, dict):
        lines = [
            _make_line(
                {'key': key, 'status': 'equal', 'old_value': diff[key]},
                content_depth,
            )
            for key in sorted(diff)
        ]
    else:
        lines = [_make_line(node, content_depth) for node in diff]
    closing = ' ' * (close_depth * SPACES_PER_LEVEL) + '}'
    return '\n'.join(chain('{', lines, [closing]))


def _make_line(node, depth):
    key = node['key']
    status = node['status']

    if status == 'equal':
        indent = _indent(depth, marker=False)
        value = _resolve_value(node.get('old_value'), depth)
        return f'{indent}{key}: {value}'

    if status == 'added':
        indent = _indent(depth, marker=True)
        value = _resolve_value(node.get('new_value'), depth)
        return f'{indent}+ {key}: {value}'

    if status == 'removed':
        indent = _indent(depth, marker=True)
        value = _resolve_value(node.get('old_value'), depth)
        return f'{indent}- {key}: {value}'

    if status == 'updated':
        indent = _indent(depth, marker=True)
        value1 = _resolve_value(node.get('old_value'), depth)
        value2 = _resolve_value(node.get('new_value'), depth)
        return (
            f'{indent}- {key}: {value1}\n'
            f'{indent}+ {key}: {value2}'
        )

    if status == 'nested':
        indent = _indent(depth, marker=False)
        value = _resolve_value(node.get('children'), depth)
        return f'{indent}{key}: {value}'

    raise ValueError(f'Unknown status: {status}')


def _indent(depth, marker):
    if marker:
        return ' ' * (depth * SPACES_PER_LEVEL - OFFSET)
    return ' ' * (depth * SPACES_PER_LEVEL)


def _resolve_value(value, depth):
    if isinstance(value, (list, dict)):
        return _format_inner(value, depth + 1, depth)
    return resolve_none_and_boolean(value)
