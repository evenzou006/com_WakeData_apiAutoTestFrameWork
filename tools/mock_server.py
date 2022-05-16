# -*- coding: utf-8 -*-
# @Author : EvenZou
# @CreateTime : 2022/5/7 10:47
# @FileName : mock_server.py
from flask import Flask, request, jsonify
# 基于flask实现MockServer识别不同的请求参数而返回对应的响应数据

# 创建一个flask实例
app = Flask(__name__)


# 指定路由和请求方法
@app.route('/api/login', methods=['POST'])
def login():
    pass

