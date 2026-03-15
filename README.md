# python-app-with-uv

Dev Container と `uv` を使った Python サンプルワークスペースです。

## 構成

- `.devcontainer/`
  Dev Container の設定です。
- `python-projects/sample_project/`
  `uv` で管理するサンプル Python プロジェクトです。
- `python-app-with-uv.code-workspace`
  指定したプロジェクトを開くための VS Code ワークスペースです。
- `.github/workflows/ci.yml`
  GitHub Actions で `pytest`、`ruff`、`mypy` を実行する CI 設定です。

## 前提

- VS Code
- Dev Containers 拡張
- Docker Desktop または Docker が動く環境

## 使い方

1. VS Code で `python-app-with-uv` を開きます。
2. `Dev Containers: Reopen in Container` を実行します。
3. 必要に応じて `python-app-with-uv.code-workspace` を開きます。

## セットアップ

Dev Container の初回作成時に、`python-projects` 配下の各プロジェクトで `uv sync --group dev` を自動実行する設定です。

```bash
cd python-projects/sample_project
uv sync --group dev
```

## よく使うコマンド

```bash
uv run sample_project
uv run python src/sample_project/main.py
uv run pytest
uv run ruff check .
uv run mypy src tests
```

`test_project` でも同様に実行できます。

```bash
cd python-projects/test_project
uv run test_project
```

## 別プロジェクトを追加する

新しいプロジェクトを追加するときは `sample_project` を雛形として使います。

1. `python-projects/sample_project` を `python-projects/<new_project_name>` にコピーします。
2. `src/sample_project` を `src/<new_project_name>` に変更します。
3. `tests/sample_project` を `tests/<new_project_name>` に変更します。
4. `pyproject.toml` を更新します。
   - `[project].name`
   - `[project.scripts]`
   - `[tool.hatch.build.targets.wheel].packages`
5. `src/<new_project_name>/main.py` と `tests/<new_project_name>/test_main.py` の import と表示文字列を更新します。
6. [python-app-with-uv.code-workspace](./python-app-with-uv.code-workspace) に新しいフォルダを追加します。
7. [.devcontainer/docker-compose.yml](./.devcontainer/docker-compose.yml) に新しい `.venv` 用 volume を追加します。
8. [.github/workflows/ci.yml](./.github/workflows/ci.yml) の matrix に新しいプロジェクトパスを追加します。
9. Dev Container を作り直すと、`python-projects` 配下の `pyproject.toml` を持つ各プロジェクトで `uv sync --group dev` が自動実行されます。

```bash
cd python-projects/<new_project_name>
uv sync --group dev
```

`my_app` を追加する例:

```bash
cp -r python-projects/sample_project python-projects/my_app
mv python-projects/my_app/src/sample_project python-projects/my_app/src/my_app
mv python-projects/my_app/tests/sample_project python-projects/my_app/tests/my_app
cd python-projects/my_app
uv sync --group dev
```

## 補足

- `mypy` のキャッシュは `/tmp/mypy-cache` を使います。
- `pytest` のキャッシュは `/tmp/pytest-cache` を使います。
- `ruff` のキャッシュは `/tmp/ruff-cache` を使います。
- `.venv`、`__pycache__` などの生成物は Git 管理対象外です。
