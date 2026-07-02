import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from monitor.memory import get_memory_info

def test_memory():
    info = get_memory_info()
    assert 'total' in info
    assert 'used' in info
    assert 'percent' in info
    assert info['total'] > 0
    assert 0 <= info['percent'] <= 100

if __name__ == "__main__":
    test_memory()
    print("✅ Test Memory pasado")
