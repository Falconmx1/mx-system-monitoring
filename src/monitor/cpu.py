import psutil

def get_cpu_info():
    """Obtiene información de la CPU"""
    return {
        'percent': psutil.cpu_percent(interval=0.5),
        'cores': psutil.cpu_percent(interval=0.5, percpu=True),
        'count': psutil.cpu_count()
    }
