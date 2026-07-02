# Guía de uso de MX System Monitoring

## Comandos básicos

| Comando | Descripción |
|---------|-------------|
| `python src/main.py` | Monitoreo en tiempo real |
| `python src/main.py --once` | Muestra datos una sola vez |
| `python src/main.py --cpu --ram` | Muestra solo CPU y RAM |
| `python src/main.py --alert-cpu 80` | Alerta si CPU > 80% |
| `python src/main.py --export report.csv` | Exporta datos a CSV |

## Ejemplos

### Monitoreo completo en vivo
```bash
python src/main.py
