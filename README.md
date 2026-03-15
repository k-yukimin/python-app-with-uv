# python-app-with-uv

Dev Container と `uv` を使って、複数の Python プロジェクトを 1 つのワークスペースで扱うためのサンプルです。

## 構成

- `.devcontainer/`
  Dev Container の設定です。`Dockerfile`、`docker-compose.yml`、`devcontainer.json` を置いています。
- `python-projects/project1/`
  1つ目の Python プロジェクトです。
- `python-projects/project2/`
  2つ目の Python プロジェクトです。
- `python-app-with-uv.code-workspace`
  `project1` と `project2` をまとめて開くための VS Code ワークスペースです。

## 前提

- VS Code がインストールされていること
- VS Code の Dev Containers 拡張が使えること
- Docker Desktop など Docker を実行できること

## 使い方

1. `python-app-with-uv` フォルダを VS Code で開きます。
2. `Dev Containers: Reopen in Container` を実行します。
3. コンテナ起動後、必要なら `python-app-with-uv.code-workspace` を開きます。
4. VS Code のエクスプローラーから `project1` / `project2` を個別に操作できます。

## `uv` について

各プロジェクトの依存は `uv` で管理します。仮想環境は各プロジェクト配下の `.venv` に作成されます。

- `python-projects/project1/.venv`
- `python-projects/project2/.venv`

`.venv` は Docker volume にマウントされるため、コンテナ再作成時にも依存を再利用できます。

## セットアップ

各プロジェクトで `uv sync` を実行します。

### project1

```bash
cd python-projects/project1
uv sync --group dev
```

### project2

```bash
cd python-projects/project2
uv sync --group dev
```

## よく使うコマンド

### 依存を同期する

```bash
uv sync --group dev
```

### 依存を追加する

```bash
uv add requests
```

開発用依存を追加する場合:

```bash
uv add --group dev pytest
```

### 依存を削除する

```bash
uv remove requests
```

### スクリプトを実行する

```bash
uv run python src/project1/main.py
```

または `project.scripts` に定義したエントリーポイントを実行できます。

```bash
uv run project1
```

`project2` も同様です。

```bash
uv run project2
```

## チェック

各プロジェクトで以下を実行できます。

- `pytest`: テスト
- `ruff`: lint
- `mypy`: 型チェック

```bash
uv run pytest
uv run ruff check .
uv run mypy src tests
```

GitHub では [`.github/workflows/ci.yml`](./.github/workflows/ci.yml) で同じチェックを実行します。

## 例

`project2` へ移動して実行する例です。

```bash
cd /app/python-projects/project2
uv sync --group dev
uv run project2
```

## 補足

- `mypy` のキャッシュは `/tmp/mypy-cache` を使う設定です。
- `pytest` のキャッシュは `/tmp/pytest-cache` を使う設定です。
- `.venv` や `__pycache__` などの生成物は Git 管理対象外です。
- Dev Container の設定を変更した場合は `Rebuild Container` を実行してください。
