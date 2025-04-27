from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    
    # 注册路由
    # from .routes import main
    # app.register_blueprint(main)
    
    # 初始化扩展
    socketio.init_app(app)
    
    return app