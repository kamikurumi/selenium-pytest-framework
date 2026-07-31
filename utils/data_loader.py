import json
import os

def load_test_data(file_name="test_data.json"):
    """从 data 目录加载 JSON 测试数据"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)