from gendiff.scripts.utils import resolve_none_and_boolean


def plain(diff):
    return '\n'.join(_walk(diff))


def _walk(diff, parent_path=''):
    lines = []
    for node in diff:
        key = node['key']
        path = f'{parent_path}.{key}' if parent_path else key

        if node['status'] == 'nested':
            lines.extend(_walk(node['children'], path))
            continue

        line = _make_line(node, path)
        if line:
            lines.append(line)
    return lines


def _make_line(node, path):
    status = node['status']

    if status == 'added':
        value = _format_value(node.get('new_value'))
        return f"Property '{path}' was added with value: {value}"

    if status == 'removed':
        return f"Property '{path}' was removed"

    if status == 'updated':
        old_value = _format_value(node.get('old_value'))
        new_value = _format_value(node.get('new_value'))
        return (
            f"Property '{path}' was updated. "
            f"From {old_value} to {new_value}"
        )

    return None


def _format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    return resolve_none_and_boolean(value)
