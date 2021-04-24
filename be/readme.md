If you get an error tring to run the application with somthing like this "from bson.py3compat import abc, string_type, PY3, text_type ImportError: cannot import name 'abc' from 'bson.py3compat'"

For some reason the order matters? https://www.gitmemory.com/issue/py-bson/bson/82/486309073
run these commands:
pip uninstall bson
pip uninstall pymongo

pip install bson
pip install pymongo