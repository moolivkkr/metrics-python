import psutil
from opentelemetry.sdk.metrics import Counter, MeterProvider

from settings import *


class CPUMetrics:
    def __init__(self, meter_provider=None, **kwargs):
        self.meter_provider = meter_provider or MeterProvider()
        self.labels = kwargs
        self.cpu_counters = {}
        self.core_counters = {}

    def create_cpu_metrics(self):
        self.cpu_counters = {
            f"cpu_{metric}_{i}": self.meter_provider.get_meter(__name__).create_metric(
                f"system.cpu.{metric}", f"CPU {metric.capitalize()}", "1", int, Counter, (CPU_LABEL_CPU, CPU_STATES),
                labels={**self.labels, **{CPU_LABEL_CPU: str(i)}}
            ) for i, cpu in enumerate(psutil.cpu_times(percpu=True)) for metric in CPU_METRICS
        }

    def create_core_metrics(self):
        self.core_counters = {
            f"core_{metric}_{i}.{j}": self.meter_provider.get_meter(__name__).create_metric(
                f"system.cpu.{metric}", f"CPU {metric.capitalize()} per core", "1", int, Counter,
                (CPU_LABEL_CPU, CPU_LABEL_CORE, CPU_STATES),
                labels={**self.labels, **{CPU_LABEL_CPU: str(i), CPU_LABEL_CORE: str(j)}}
            ) for i, cpu in enumerate(psutil.cpu_times(percpu=True)) for j, core in enumerate(cpu) for metric in
            CORE_METRICS
        }
