# Copilot Instructions

## 專案概覽

這是一個純 Python CLI 工具專案，使用 Python 3.11。
主要用途為命令列操作，適合自動化或批次處理。

## 環境設定

```bash
# 建立虛擬環境
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS/Linux

# 安裝相依套件
pip install -r requirements.txt
pip install -r requirements-dev.txt  # 開發用（含測試、lint 工具）
```

## 建置 / 測試 / Lint 指令

```bash
# 執行所有測試
pytest

# 執行單一測試檔或測試函式
pytest tests/test_foo.py
pytest tests/test_foo.py::test_bar

# 顯示覆蓋率
pytest --cov=src --cov-report=term-missing

# Lint（ruff）
ruff check .

# 自動修正
ruff check . --fix

# 型別檢查
mypy src/
```

## 專案結構

```
src/          # 主要原始碼（套件或模組）
tests/        # pytest 測試，檔名以 test_ 開頭
```

## 程式碼慣例

- Python 3.11；型別提示（type hints）必填。
- 程式碼風格遵循 `ruff` 預設規則（PEP 8 為基礎）。
- 測試框架使用 `pytest`；測試函式以 `test_` 開頭。
- 不要在 `src/` 以外的地方放置業務邏輯；CLI 進入點獨立於核心邏輯。
- 使用 `pathlib.Path` 處理路徑，不使用 `os.path`。
- 例外處理：具體例外優先（避免裸 `except`），錯誤訊息需對使用者友善。
