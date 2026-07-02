import psutil
import time

_prev_net = None
_prev_time = None

def get_network_info():
    """Obtiene velocidad de red (entrada/salida por segundo)"""
    global _prev_net, _prev_time
    current = psutil.net_io_counters()
    now = time.time()
    
    if _prev_net is None:
        _prev_net = current
        _prev_time = now
        return {'bytes_sent': 0, 'bytes_recv': 0}
    
    time_diff = now - _prev_time
    if time_diff == 0:
        return {'bytes_sent': 0, 'bytes_recv': 0}
    
    sent_diff = current.bytes_sent - _prev_net.bytes_sent
    recv_diff = current.bytes_recv - _prev_net.bytes_recv
    
    _prev_net = current
    _prev_time = now
    
    return {
        'bytes_sent': sent_diff / time_diff,
        'bytes_recv': recv_diff / time_diff
    }
