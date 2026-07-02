from datetime import datetime

def format_bytes(bytes):
    """Formatea bytes a unidad legible"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            return f"{bytes:.1f} {unit}"
        bytes /= 1024.0
    return f"{bytes:.1f} PB"

def get_timestamp():
    """Retorna timestamp formateado"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
