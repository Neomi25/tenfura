import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    """主頁面路由，返回 Hello 頁面"""
    return render_template('index.html')

@app.route('/api/hello')
def api_hello() -> dict[str, str]:
    """API 路由，返回 JSON 格式的 Hello 訊息"""
    return {'message': 'Hello from oden!', 'status': 'success'}


@app.errorhandler(404)
def not_found(e: Exception) -> tuple[dict[str, str], int]:
    return {'error': 'Not found'}, 404


@app.errorhandler(500)
def server_error(e: Exception) -> tuple[dict[str, str], int]:
    return {'error': 'Internal server error'}, 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)