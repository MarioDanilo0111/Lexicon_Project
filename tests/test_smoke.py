import importlib
import os

def test_imports():
    # Allow overriding the entry module with APP_MODULE, default to "main"
    module = os.getenv("APP_MODULE", "main").removesuffix(".py").replace("/", ".")
    importlib.import_module(module)

def test_sanity():
    assert True