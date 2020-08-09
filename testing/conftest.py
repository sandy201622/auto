#只有在当前目录下或者子目录生效，pytest会自动加载该文件

import pytest


def pytest_collection_modifyitems(session, config, items:list):
    for item in items:
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)

        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)

