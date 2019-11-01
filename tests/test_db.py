# coding:utf-8
import unittest
from flask import current_app
from apps import create_app
from apps import db


class TestDatabase(unittest.TestCase):
    """测试数据库的案例"""

    def setUp(self):
        # 开启测试模式
        self.app = create_app("default")
        self.app.debug = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        # db.drop_all()
        # db.create_all()

    def test_app_exits(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertFalse(current_app.config['test'])

    def tearDown(self):
        """在所有测试方法执行后，被调用"""
        # 清除记录的测试任务
        db.session.remove()
        # 清除数据库数据
        # db.drop_all()
        self.app_context.pop()
