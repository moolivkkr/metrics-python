import unittest
import psutil
from unittest.mock import Mock
from opentelemetry.sdk.metrics import Counter, MeterProvider
from disk_metrics import DiskMetrics
from settings import *


class TestDiskMetrics(unittest.TestCase):
    def setUp(self):
        self.meter_provider = MeterProvider()
        self.disk_metrics = DiskMetrics(self.meter_provider, service_name="test-service")

    def test_create_disk_metrics(self):
        psutil.disk_partitions = Mock(return_value=[psutil._common.sdiskpart(device="/dev/disk1s1", mountpoint="/")])
        self.disk_metrics.create_disk_metrics()
        metrics = self.disk_metrics.metrics
        self.assertIn("metrics/disk_read_bytes/dev_disk1s1", metrics.keys())
        self.assertIn("metrics/disk_write_bytes/dev_disk1s1", metrics.keys())
        self.assertIn("metrics/disk_read_time/dev_disk1s1", metrics.keys())
        self.assertIn("metrics/disk_write_time/dev_disk1s1", metrics.keys())
        self.assertIn("metrics/disk_io_time/dev_disk1s1", metrics.keys())
        self.assertIn("metrics/disk_busy_time/dev_disk1s1", metrics.keys())
        self.assertIsInstance(metrics["metrics/disk_read_bytes/dev_disk1s1"], Counter)
        self.assertIsInstance(metrics["metrics/disk_write_bytes/dev_disk1s1"], Counter)
        self.assertIsInstance(metrics["metrics/disk_read_time/dev_disk1s1"], Counter)
        self.assertIsInstance(metrics["metrics/disk_write_time/dev_disk1s1"], Counter)
        self.assertIsInstance(metrics["metrics/disk_io_time/dev_disk1s1"], Counter)
        self.assertIsInstance(metrics["metrics/disk_busy_time/dev_disk1s1"], Counter)


def test_update_disk_metrics(self):
    psutil.disk_io_counters = Mock(return_value={
        "disk1s1": psutil._common.sdiskio(read_bytes=1024, write_bytes=512, read_time=0.5, write_time=0.2,
                                          busy_time=1.0)})
    self.disk_metrics.metrics = {
        "metrics/disk_read_bytes/disk1s1": self.meter_provider.get_meter("system").create_metric(
            name="metrics/disk_read_bytes/disk1s1", description="Bytes read from disk1s1 partition", unit="bytes",
            value_type=int, metric_type=Counter),
        "metrics/disk_write_bytes/disk1s1": self.meter_provider.get_meter("system").create_metric(
            name="metrics/disk_write_bytes/disk1s1", description="Bytes written to disk1s1 partition", unit="bytes",
            value_type=int, metric_type=Counter),
        "metrics/disk_read_time/disk1s1": self.meter_provider.get_meter("system").create_metric(
            name="metrics/disk_read_time/disk1s1", description="Time spent reading from disk1s1 partition",
            unit="seconds", value_type=float, metric_type=Counter),
        "metrics/disk_write_time/disk1s1": self.meter_provider.get_meter("system").create_metric(
            name="metrics/disk_write_time/disk1s1", description="Time spent writing to disk1s1 partition",
            unit="seconds", value_type=float, metric_type=Counter),
        "metrics/disk_io_time/disk1s1": self.meter_provider.get_meter("system").create_metric(
            name="metrics/disk_io_time/disk1s1", description="Time spent doing I/O on disk1s1 partition",
            unit="seconds", value_type=float, metric_type=Counter),
        "metrics/disk_busy_time/disk1s1": self.meter_provider.get_meter("system").create_metric(
            name="metrics/disk_busy_time/disk1s1", description="Time spent with I/O in progress on disk1s1 partition",
            unit="seconds", value_type=float, metric_type=Counter),
    }

    self.disk_metrics.update_disk_metrics()

    for key, metric in self.disk_metrics.metrics.items():
        device = key.split("/")[-1]
        labels = self.disk_metrics.labels.copy()
        labels[METRICS_DISK_LABEL_DEVICE] = device

        if "read_bytes" in key:
            self.assertEqual(metric.get_value(labels), 1024)
        elif "write_bytes" in key:
            self.assertEqual(metric.get_value(labels), 512)
        elif "read_time" in key:
            self.assertEqual(metric.get_value(labels), 0.5)
        elif "write_time" in key:
            self.assertEqual(metric.get_value(labels), 0.2)
        elif "io_time" in key:
            self.assertEqual(metric.get_value(labels), 0.7)
        elif "busy_time" in key:
            self.assertEqual(metric.get_value(labels), 1.0)
