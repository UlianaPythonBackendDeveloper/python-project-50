import json
import os

import pytest

from gendiff import generate_diff

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'test_data')


def get_test_data_path(file_name):
    return os.path.join(TEST_DATA_DIR, file_name)


def read_expected(file_name):
    path = get_test_data_path(file_name)
    with open(path) as expected_file:
        return expected_file.read().rstrip('\n')


def read_expected_json(file_name):
    path = get_test_data_path(file_name)
    with open(path) as expected_file:
        return json.loads(expected_file.read())


@pytest.mark.parametrize(
    'file1, file2',
    [
        ('file1.json', 'file2.json'),
        ('file1.yml', 'file2.yml'),
        ('file1.yaml', 'file2.yml'),
    ],
)
def test_flat_files_stylish(file1, file2):
    path1 = get_test_data_path(file1)
    path2 = get_test_data_path(file2)
    result = generate_diff(path1, path2)

    assert result == read_expected('expected_stylish.txt')


@pytest.mark.parametrize(
    'file1, file2',
    [
        ('file1_nested.json', 'file2_nested.json'),
        ('file1_nested.yml', 'file2_nested.yml'),
    ],
)
def test_nested_files_stylish(file1, file2):
    path1 = get_test_data_path(file1)
    path2 = get_test_data_path(file2)
    result = generate_diff(path1, path2)

    assert result == read_expected('expected_nested_stylish.txt')


@pytest.mark.parametrize(
    'file1, file2',
    [
        ('file1.json', 'file2.json'),
        ('file1.yml', 'file2.yml'),
    ],
)
def test_flat_files_plain(file1, file2):
    path1 = get_test_data_path(file1)
    path2 = get_test_data_path(file2)
    result = generate_diff(path1, path2, 'plain')

    assert result == read_expected('expected_plain.txt')


@pytest.mark.parametrize(
    'file1, file2',
    [
        ('file1_nested.json', 'file2_nested.json'),
        ('file1_nested.yml', 'file2_nested.yml'),
    ],
)
def test_nested_files_plain(file1, file2):
    path1 = get_test_data_path(file1)
    path2 = get_test_data_path(file2)
    result = generate_diff(path1, path2, 'plain')

    assert result == read_expected('expected_nested_plain.txt')


@pytest.mark.parametrize(
    'file1, file2, expected_file',
    [
        ('file1.json', 'file2.json', 'expected_flat.json'),
        ('file1.yml', 'file2.yml', 'expected_flat.json'),
        ('file1_nested.json', 'file2_nested.json', 'expected_nested.json'),
        ('file1_nested.yml', 'file2_nested.yml', 'expected_nested.json'),
    ],
)
def test_files_json(file1, file2, expected_file):
    path1 = get_test_data_path(file1)
    path2 = get_test_data_path(file2)
    result = generate_diff(path1, path2, 'json')

    assert json.loads(result) == read_expected_json(expected_file)
