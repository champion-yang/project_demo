# -*- coding:utf-8 -*-
import os
from flask import jsonify
from flasgger import swag_from
from . import app1
from utils.response import Response

base_dir = os.path.dirname(__file__)
demo_yml_path = os.path.join(base_dir, "docs/demo.yml")


@app1.route('/demo', endpoint="demo", methods=['POST'])
@swag_from(demo_yml_path, endpoint="app1.demo", methods=['POST'])
def demo1():
    """
    :return:
    """
    res = Response()
    try:
        pass
    except Exception as e:
        pass

    return jsonify(res.object_to_dict())
