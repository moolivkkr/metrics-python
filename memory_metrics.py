import psutil
from opentelemetry.sdk.metrics import Counter, MeterProvider
from settings import *


class MemoryMetrics:
    def __init__(self, meter_provider: MeterProvider, **kwargs):
        self.meter = meter_provider.get_meter("system")
        self.labels = kwargs
        self.metrics = {}

    def create_mem_metrics(self):
        self.metrics[METRIC_MEMORY_TOTAL] = self.meter.create_metric(
            name=METRIC_MEMORY_TOTAL,
            description="Total memory available on the system",
            unit="bytes",
            value_type=int,
            metric_type=Counter,
        )
        self.metrics[METRIC_MEMORY_AVAILABLE] = self.meter.create_metric(
            name=METRIC_MEMORY_AVAILABLE,
            description="Total memory available for use on the system",
            unit="bytes",
            value_type=int,
            metric_type=Counter,
        )
        self.metrics[METRIC_MEMORY_USED] = self.meter.create_metric(
            name=METRIC_MEMORY_USED,
            description="Total memory currently being used on the system",
            unit="bytes",
            value_type=int,
            metric_type=Counter,
        )
        self.metrics[METRIC_MEMORY_FREE] = self.meter.create_metric(
            name=METRIC_MEMORY_FREE,
            description="Total memory currently free on the system",
            unit="bytes",
            value_type=int,
            metric_type=Counter,
        )
        self.metrics[METRIC_MEMORY_ACTIVE] = self.meter.create_metric(
            name=METRIC_MEMORY_ACTIVE,
            description="Total memory currently being used actively by processes on the system",
            unit="bytes",
            value_type=int,
            metric_type=Counter,
        )
        self.metrics[METRIC_MEMORY_INACTIVE] = self.meter.create_metric(
            name=METRIC_MEMORY_INACTIVE,
            description="Total memory currently being used passively by processes on the system",
            unit="bytes",
            value_type=int,
            metric_type=Counter,
        )
        self.metrics[METRIC_MEMORY_PERCENT] = self.meter.create_metric(
            name=METRIC_MEMORY_PERCENT,
            description="Percent of available memory being used on the system",
            unit="percent",
            value_type=float,
            metric_type=Counter,
        )

    def update_mem_metrics(self):
        mem_stats = psutil.virtual_memory()
        self.metrics[METRIC_MEMORY_TOTAL].add(mem_stats.total, self.labels)
        self.metrics[METRIC_MEMORY_AVAILABLE].add(mem_stats.available, self.labels)
        self.metrics[METRIC_MEMORY_USED].add(mem_stats.used, self.labels)
        self.metrics[METRIC_MEMORY_FREE].add(mem_stats.free, self.labels)
        self.metrics[METRIC_MEMORY_ACTIVE].add(mem_stats.active, self.labels)
        self.metrics[METRIC_MEMORY_INACTIVE].add(mem_stats.inactive, self.labels)
        self.metrics[METRIC_MEMORY_PERCENT].add(mem_stats.percent, self.labels)
