# oden

Learning for AI agents

## 專案說明

一個簡單的 Flask 網站應用程式，顯示「Hello」畫面。該應用已打包成 Docker 映像以便於部署。

## 技術棧

- **框架**: Python Flask
- **容器化**: Docker

## 快速開始

### 本地運行

1. 克隆倉庫:
```bash
git clone https://github.com/Neomi25/oden.git
cd oden
```

2. 安裝依賴:
```bash
pip install -r requirements.txt
```

3. 運行應用:
```bash
python app.py
```

應用將在 `http://localhost:5000` 啟動

### 使用 Docker 運行

1. 構建映像:
```bash
docker build -t oden:latest .
```

2. 運行容器:
```bash
docker run -p 5000:5000 oden:latest
```

訪問 `http://localhost:5000` 查看應用

## 功能

- 簡單的 Flask web 伺服器
- 主頁面顯示「Hello」

## Source Code

### 目錄結構

```
oden/
├── app.py              # Flask 主應用程式
├── requirements.txt    # Python 依賴清單
├── Dockerfile          # Docker 容器配置
└── templates/          # HTML 模板目錄
    └── index.html      # 主頁面模板
```

### 核心文件

#### app.py
Flask 應用的主要入口點，定義路由和應用配置。

#### requirements.txt
列出項目所有的 Python 依賴包。

#### Dockerfile
定義 Docker 映像的構建步驟，用於容器化應用。

#### templates/index.html
渲染「Hello」頁面的 HTML 模板。

## 貢獻

歡迎提交 Issues 和 Pull Requests！