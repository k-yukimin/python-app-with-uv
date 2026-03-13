# python-app

Dev Container と `uv` を使って、複数の Python プロジェクトを 1 つのワークスペースで扱うためのサンプル構成です。

## 構成

- `.devcontainer/`
  Dev Container の設定です。`Dockerfile`、`docker-compose.yml`、`devcontainer.json` を含みます。
- `python-projects/project1/`
  1 つ目の Python プロジェクトです。
- `python-projects/project2/`
  2 つ目の Python プロジェクトです。
- `python-app.code-workspace`
  `project1` と `project2` をまとめて開くための VS Code ワークスペースです。

## 前提

- VS Code がインストールされていること
- VS Code の Dev Containers 拡張機能が利用できること
- Docker Desktop など、Docker が使えること

## 使い方

1. `python-app` フォルダを VS Code で開きます。
2. `Dev Containers: Reopen in Container` を実行します。
3. コンテナ起動後、必要に応じて `python-app.code-workspace` を開きます。
4. VS Code のエクスプローラーから `project1` / `project2` を個別に操作できます。

## `uv` について

各プロジェクトは `uv` で依存関係を管理します。仮想環境は各プロジェクト配下の `.venv` に作成されます。

- `python-projects/project1/.venv`
- `python-projects/project2/.venv`

`.venv` は Docker volume にマウントされるため、コンテナ再作成時も依存関係を保持しやすい構成です。

## セットアップ

各プロジェクトで初回のみ `uv sync` を実行します。

### project1

```bash
cd python-projects/project1
uv sync
```

### project2

```bash
cd python-projects/project2
uv sync
```

`uv sync` により、`pyproject.toml` と `uv.lock` に基づいて依存関係がインストールされます。

## よく使うコマンド

### 依存関係を同期する

```bash
uv sync
```

### パッケージを追加する

```bash
uv add requests
```

開発用依存関係を追加する場合:

```bash
uv add --dev pytest
```

### パッケージを削除する

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

## 品質チェック

各プロジェクトには、サンプルとして以下を追加しています。

- `pytest`: テスト実行
- `ruff`: Lint
- `mypy`: 型チェック

初回セットアップ後に、各プロジェクトで次を実行できます。

```bash
uv run pytest
uv run ruff check .
uv run mypy src tests
```

GitHub に push したときや Pull Request を作成したときは、`.github/workflows/ci.yml` で同じチェックが自動実行されます。

## 別プロジェクトへ移るとき

別のプロジェクトで作業する場合は、そのプロジェクトのディレクトリへ移動してから `uv` コマンドを実行します。

```bash
cd /app/python-projects/project2
uv sync
uv run project2
```

`uv` はカレントディレクトリの `pyproject.toml` を見て動作するため、対象プロジェクトの場所で実行してください。

## 補足

- `mypy` のキャッシュは `/tmp/mypy-cache` を使う設定です。
- `.venv` や `__pycache__` などの生成物は Git 管理対象外です。
- Dev Container の設定を変更した場合は `Rebuild Container` を実行してください。
