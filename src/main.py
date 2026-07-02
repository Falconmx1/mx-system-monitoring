#!/usr/bin/env python3
"""
MX System Monitoring - Punto de entrada principal
"""
import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from monitor.cpu import get_cpu_info
from monitor.memory import get_memory_info
from monitor.disk import get_disk_info
from monitor.network import get_network_info
from monitor.processes import get_top_processes
from utils.helpers import format_bytes, get_timestamp
import time
import sys

console = Console()

@click.command()
@click.option('--cpu', is_flag=True, help="Mostrar solo CPU")
@click.option('--ram', is_flag=True, help="Mostrar solo RAM")
@click.option('--disk', is_flag=True, help="Mostrar solo disco")
@click.option('--network', is_flag=True, help="Mostrar solo red")
@click.option('--processes', is_flag=True, help="Mostrar solo procesos")
@click.option('--export', type=click.Path(), help="Exportar a archivo CSV")
@click.option('--alert-cpu', type=int, help="Alerta si CPU supera este %")
@click.option('--alert-ram', type=int, help="Alerta si RAM supera este %")
@click.option('--once', is_flag=True, help="Ejecutar una sola vez y salir")
def main(cpu, ram, disk, network, processes, export, alert_cpu, alert_ram, once):
    """MX System Monitoring - Monitoreo en tiempo real"""
    
    # Si se especifican flags, filtrar módulos
    modules = []
    if cpu: modules.append('cpu')
    if ram: modules.append('ram')
    if disk: modules.append('disk')
    if network: modules.append('network')
    if processes: modules.append('processes')
    if not modules:
        modules = ['cpu', 'ram', 'disk', 'network', 'processes']
    
    # Exportar modo (una sola vez)
    if export:
        data = collect_data(modules)
        export_to_csv(data, export)
        console.print(f"[green]✓ Datos exportados a {export}[/green]")
        return
    
    # Modo una sola vez
    if once:
        display_data(collect_data(modules), alert_cpu, alert_ram)
        return
    
    # Modo en vivo
    with Live(refresh_per_second=1, screen=True) as live:
        try:
            while True:
                data = collect_data(modules)
                layout = create_layout(data, alert_cpu, alert_ram)
                live.update(layout)
                time.sleep(1)
        except KeyboardInterrupt:
            console.print("\n[bold yellow]Monitoreo detenido[/bold yellow]")

def collect_data(modules):
    """Recolecta datos según módulos activos"""
    data = {}
    if 'cpu' in modules:
        data['cpu'] = get_cpu_info()
    if 'ram' in modules:
        data['memory'] = get_memory_info()
    if 'disk' in modules:
        data['disk'] = get_disk_info()
    if 'network' in modules:
        data['network'] = get_network_info()
    if 'processes' in modules:
        data['processes'] = get_top_processes()
    data['timestamp'] = get_timestamp()
    return data

def create_layout(data, alert_cpu=None, alert_ram=None):
    """Crea el layout con Rich"""
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=3)
    )
    
    # Header
    header_text = Text(f"🖥️  MX System Monitoring ", style="bold cyan")
    header_text.append(f"| {data['timestamp']}", style="white")
    layout["header"].update(Panel(header_text, border_style="bright_blue"))
    
    # Main content
    main_layout = Layout()
    main_layout.split_row(
        Layout(name="left", ratio=1),
        Layout(name="right", ratio=1)
    )
    
    left_content = []
    right_content = []
    
    # CPU
    if 'cpu' in data:
        cpu = data['cpu']
        cpu_text = f"CPU: {cpu['percent']}%"
        if alert_cpu and cpu['percent'] > alert_cpu:
            cpu_text = f"[bold red]⚠ CPU: {cpu['percent']}% (ALERTA > {alert_cpu}%)[/bold red]"
        left_content.append(Panel(cpu_text, title="🧠 CPU", border_style="green"))
        for i, core in enumerate(cpu['cores']):
            left_content.append(f"  Núcleo {i}: {core}%")
    
    # RAM
    if 'memory' in data:
        mem = data['memory']
        mem_text = f"RAM: {format_bytes(mem['used'])} / {format_bytes(mem['total'])} ({mem['percent']}%)"
        if alert_ram and mem['percent'] > alert_ram:
            mem_text = f"[bold red]⚠ RAM: {mem['percent']}% (ALERTA > {alert_ram}%)[/bold red]"
        right_content.append(Panel(mem_text, title="💾 Memoria", border_style="yellow"))
        right_content.append(f"  Swap: {format_bytes(mem['swap_used'])} / {format_bytes(mem['swap_total'])} ({mem['swap_percent']}%)")
    
    # Disco
    if 'disk' in data:
        disk = data['disk']
        disk_text = f"Disco: {format_bytes(disk['used'])} / {format_bytes(disk['total'])} ({disk['percent']}%)"
        right_content.append(Panel(disk_text, title="💿 Disco", border_style="magenta"))
    
    # Red
    if 'network' in data:
        net = data['network']
        net_text = f"↓ {format_bytes(net['bytes_recv'])}/s | ↑ {format_bytes(net['bytes_sent'])}/s"
        left_content.append(Panel(net_text, title="🌐 Red", border_style="cyan"))
    
    # Procesos
    if 'processes' in data:
        procs = data['processes']
        proc_table = Table(title="Procesos", show_header=True, header_style="bold magenta")
        proc_table.add_column("PID", style="dim")
        proc_table.add_column("Nombre")
        proc_table.add_column("CPU%")
        proc_table.add_column("RAM%")
        for p in procs[:10]:
            proc_table.add_row(str(p['pid']), p['name'][:20], f"{p['cpu']:.1f}", f"{p['memory']:.1f}")
        right_content.append(Panel(proc_table, title="📊 Procesos", border_style="blue"))
    
    # Actualizar layout
    main_layout["left"].update(Panel("\n".join(str(c) for c in left_content), border_style="bright_blue"))
    main_layout["right"].update(Panel("\n".join(str(c) for c in right_content), border_style="bright_blue"))
    
    layout["main"].update(main_layout)
    
    # Footer
    footer_text = "Presiona [bold]Ctrl+C[/bold] para salir | [bold]MX System Monitoring[/bold]"
    layout["footer"].update(Panel(footer_text, style="dim", border_style="gray"))
    
    return layout

def display_data(data, alert_cpu, alert_ram):
    """Muestra datos una sola vez"""
    console.print(Panel.fit("📊 MX System Monitoring", style="bold cyan"))
    if 'cpu' in data:
        cpu = data['cpu']
        console.print(f"🧠 CPU: {cpu['percent']}%", style="green")
    if 'memory' in data:
        mem = data['memory']
        console.print(f"💾 RAM: {format_bytes(mem['used'])} / {format_bytes(mem['total'])} ({mem['percent']}%)", style="yellow")
    if 'disk' in data:
        disk = data['disk']
        console.print(f"💿 Disco: {format_bytes(disk['used'])} / {format_bytes(disk['total'])} ({disk['percent']}%)", style="magenta")

def export_to_csv(data, filename):
    """Exporta datos a CSV"""
    import csv
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'metric', 'value'])
        for key, value in data.items():
            if key != 'timestamp' and isinstance(value, dict):
                for k, v in value.items():
                    if isinstance(v, (int, float)):
                        writer.writerow([data['timestamp'], f"{key}_{k}", v])

if __name__ == "__main__":
    main()
