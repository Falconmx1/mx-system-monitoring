import psutil

def get_disk_info():
    """Obtiene información del disco (partición raíz)"""
    disk = psutil.disk_usage('/')
    return {
        'total': disk.total,
        'used': disk.used,
        'free': disk.free,
        'percent': disk.percent
    }
