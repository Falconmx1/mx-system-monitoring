import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from monitor.cpu import get_cpu_info

def test_cpu():
    info = get_cpu_info()
    assert 'percent' in info
    assert 'cores' in info
    assert isinstance(info['percent'], (int, float))
    assert 0 <= info['percent'] <= 100

if __name__ == "__main__":
    test_cpu()
    print("✅ Test CPU pasado")
