### Hexlet tests and linter status:

[![Actions Status](https://github.com/UlianaPythonBackendDeveloper/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/UlianaPythonBackendDeveloper/python-project-50/actions)
[![Github Actions Status](https://github.com/UlianaPythonBackendDeveloper/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/UlianaPythonBackendDeveloper/python-project-50/actions)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=UlianaPythonBackendDeveloper_python-project-50&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=UlianaPythonBackendDeveloper_python-project-50)

### Links

This project was built using these tools:

| Tool                                                                   | Description                                             |
|------------------------------------------------------------------------|---------------------------------------------------------|
| [uv](https://docs.astral.sh/uv/)                                       | "An extremely fast Python package and project manager, written in Rust" |
| [Pytest](https://pytest.org)                                           | "A mature full-featured Python testing tool"            |
| [ruff](https://docs.astral.sh/ruff/)                                   | "An extremely fast Python linter and code formatter, written in Rust" |

---

### Setup

```bash
make install
```

### Examples

Сравнение плоских JSON-файлов:

```bash
uv run gendiff tests/test_data/file1.json tests/test_data/file2.json
```

Сравнение плоских YAML-файлов:

```bash
uv run gendiff tests/test_data/file1.yml tests/test_data/file2.yml
```

[![asciicast](https://asciinema.org/a/Go0h5yOWlGjKs90kY807re9os.svg)](https://asciinema.org/a/Go0h5yOWlGjKs90kY807re9os)

Рекурсивное сравнение вложенных JSON-файлов:

```bash
uv run gendiff tests/test_data/file1_nested.json tests/test_data/file2_nested.json
```

[![asciicast](https://asciinema.org/a/9FK3jcz7nE4UD9B1oZbPf6KwR.svg)](https://asciinema.org/a/9FK3jcz7nE4UD9B1oZbPf6KwR)

Вывод разницы в плоском текстовом формате:

```bash
uv run gendiff --format plain tests/test_data/file1_nested.json tests/test_data/file2_nested.json
```

[![asciicast](https://asciinema.org/a/x3R9tEAJ8APBTKNyIF5udvCZg.svg)](https://asciinema.org/a/x3R9tEAJ8APBTKNyIF5udvCZg)

Вывод разницы в формате JSON:

```bash
uv run gendiff --format json tests/test_data/file1_nested.json tests/test_data/file2_nested.json
```

[![asciicast](https://asciinema.org/a/NImau3aVI761Vbrz8D5JKoK7D.svg)](https://asciinema.org/a/NImau3aVI761Vbrz8D5JKoK7D)

### Run tests

```bash
make test
```

[![Hexlet Ltd. logo](https://raw.githubusercontent.com/Hexlet/assets/master/images/hexlet_logo128.png)](https://hexlet.io/?utm_source=github&utm_medium=link&utm_campaign=python-package)

This repository is created and maintained by the team and the community of Hexlet, an educational project. [Read more about Hexlet](https://hexlet.io/?utm_source=github&utm_medium=link&utm_campaign=python-package).

See most active contributors on [hexlet-friends](https://friends.hexlet.io/).
