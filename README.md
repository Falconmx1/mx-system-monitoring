# MX System Monitoring

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey)]()

## 📊 Descripción

**MX System Monitoring** es una herramienta ligera y multiplataforma para monitorear el rendimiento de sistemas Windows y Linux en tiempo real. Ofrece una interfaz CLI/TUI (Texto/Consola) que muestra:

- ✅ Uso de CPU por núcleo
- ✅ Memoria RAM y Swap
- ✅ Almacenamiento en disco
- ✅ Actividad de red (entrada/salida)
- ✅ Lista de procesos activos con consumo de recursos
- ✅ Alertas configurables por umbrales

Ideal para administradores de sistemas, desarrolladores y entusiastas que quieren mantener el control de sus equipos sin recursos pesados.

---

## 🚀 Características

| Característica | Windows | Linux |
|----------------|---------|-------|
| Monitoreo CPU  | ✅      | ✅    |
| Monitoreo RAM  | ✅      | ✅    |
| Monitoreo Disco| ✅      | ✅    |
| Monitoreo Red  | ✅      | ✅    |
| Procesos       | ✅      | ✅    |
| Alertas        | ✅      | ✅    |
| Exportar logs  | ✅      | ✅    |

---

## 📦 Instalación

### Desde código fuente

```bash
git clone https://github.com/Falconmx1/mx-system-monitoring.git
cd mx-system-monitoring
pip install -r requirements.txt
python src/main.py
