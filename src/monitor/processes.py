import psutil

def get_top_processes(limit=10):
    """Obtiene los procesos con mayor uso de CPU"""
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            info = proc.info
            processes.append({
                'pid': info['pid'],
                'name': info['name'] or 'unknown',
                'cpu': info['cpu_percent'] or 0,
                'memory': info['memory_percent'] or 0
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    # Ordenar por CPU descendente
    processes.sort(key=lambda x: x['cpu'], reverse=True)
    return processes[:limit]
