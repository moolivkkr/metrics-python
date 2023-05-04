import psutil
from opentelemetry.sdk.metrics import Counter, MeterProvider

from settings import *


class DiskMetrics:
    def __init__(self, meter_provider: MeterProvider, **kwargs):
        self.meter = meter_provider.get_meter("system")
        self.labels = kwargs
        self.metrics = {}

    def create_disk_metrics(self):
        for partition in psutil.disk_partitions():
            device = partition.device.replace("/", "_")
            try:
                self.metrics[f"{METRICS_DISK_READ_BYTES}/{device}"] = self.meter.create_metric(
                    name=f"{METRICS_DISK_READ_BYTES}/{device}",
                    description=f"Bytes read from {partition.mountpoint} partition", unit="bytes", value_type=int,
                    metric_type=Counter)
                self.metrics[f"{METRICS_DISK_WRITE_BYTES}/{device}"] = self.meter.create_metric(
                    name=f"{METRICS_DISK_WRITE_BYTES}/{device}",
                    description=f"Bytes written to {partition.mountpoint} partition", unit="bytes", value_type=int,
                    metric_type=Counter)
                self.metrics[f"{METRICS_DISK_READ_TIME}/{device}"] = self.meter.create_metric(
                    name=f"{METRICS_DISK_READ_TIME}/{device}",
                    description=f"Time spent reading from {partition.mountpoint} partition", unit="seconds",
                    value_type=float, metric_type=Counter)
                self.metrics[f"{METRICS_DISK_WRITE_TIME}/{device}"] = self.meter.create_metric(
                    name=f"{METRICS_DISK_WRITE_TIME}/{device}",
                    description=f"Time spent writing to {partition.mountpoint} partition", unit="seconds",
                    value_type=float, metric_type=Counter)
                self.metrics[f"{METRICS_DISK_IO_TIME}/{device}"] = self.meter.create_metric(
                    name=f"{METRICS_DISK_IO_TIME}/{device}",
                    description=f"Time spent doing I/O on {partition.mountpoint} partition", unit="seconds",
                    value_type=float, metric_type=Counter)
                self.metrics[f"{METRICS_DISK_BUSY_TIME}/{device}"] = self.meter.create_metric(
                    name=f"{METRICS_DISK_BUSY_TIME}/{device}",
                    description=f"Time spent with I/O in progress on {partition.mountpoint} partition", unit="seconds",
                    value_type=float, metric_type=Counter)
            except Exception as e:
                print(f"Error creating disk metrics for {device}: {e}")
                continue

    def update_disk_metrics(self):
        for disk, stats in psutil.disk_io_counters(perdisk=True).items():
            disk = disk.replace("/", "_")
            self.labels[METRICS_DISK_LABEL_DEVICE] = disk
            try:
                self.metrics[f"{METRICS_DISK_READ_BYTES}/{disk}"].add(stats.read_bytes, self.labels)
                self.metrics[f"{METRICS_DISK_WRITE_BYTES}/{disk}"].add(stats.write_bytes, self.labels)
                self.metrics[f"{METRICS_DISK_READ_TIME}/{disk}"].add(stats.read_time, self.labels)
                self.metrics[f"{METRICS_DISK_WRITE_TIME}/{disk}"].add(stats.write_time, self.labels)
                self.metrics[f"{METRICS_DISK_IO_TIME}/{disk}"].add(stats.read_time + stats.write_time, self.labels)
                self.metrics[f"{METRICS_DISK_BUSY_TIME}/{disk}"].add(stats.busy_time, self.labels)
            except Exception as e:
                print(f"Error updating disk metrics for {disk}: {e}")
                continue
