import unittest
from unittest.mock import MagicMock

import psutil
from opentelemetry.sdk.metrics import MeterProvider

from use_metrics import UseMetrics


class TestUseMetrics(unittest.TestCase):

    def setUp(self):
        self.meter_provider = MeterProvider()
        self.use_metrics = UseMetrics(self.meter_provider, "test_service", "test_asv", "test_component", "test_env",
                                      "test_cluster")

    def test_update_use_metrics_cpu_usage(self):
        psutil.cpu_percent = MagicMock(return_value=80.0)
        self.use_metrics.update_use_metrics()
        self.assertEqual(self.use_metrics.cpu_usage_metric.get_value(
            {"service_name": "test_service", "asv": "test_asv", "bap_component": "test_component",
             "environment": "test_env", "cluster_name": "test_cluster"}), 80.0)

    def test_update_use_metrics_memory_usage(self):
        psutil.virtual_memory = MagicMock(
            return_value=psutil._common.svmem(total=1000000000, available=500000000, percent=50, used=500000000,
                                              free=500000000))
        self.use_metrics.update_use_metrics()
        self.assertEqual(self.use_metrics.memory_usage_metric.get_value(
            {"service_name": "test_service", "asv": "test_asv", "bap_component": "test_component",
             "environment": "test_env", "cluster_name": "test_cluster"}), 50.0)

    def test_update_use_metrics_network_bandwidth_usage(self):
        psutil.net_io_counters = MagicMock(
            return_value=psutil._common.snicstats(bytes_sent=10000000, bytes_recv=5000000, packets_sent=10000,
                                                  packets_recv=5000))
        self.use_metrics.update_use_metrics()
        self.assertEqual(self.use_metrics.network_bandwidth_usage_metric.get_value(
            {"service_name": "test_service", "asv": "test_asv", "bap_component": "test_component",
             "environment": "test_env", "cluster_name": "test_cluster"}), 13.333333333333334)

    def test_update_use_metrics_network_connections_usage(self):
        psutil.net_connections = MagicMock(return_value=[
            psutil._common.sconn(fd=1, family=2, type=1, laddr=('127.0.0.1', 5432), raddr=(), status='LISTEN'),
            psutil._common.sconn(fd=2, family=2, type=2, laddr=('/var/run/docker.sock',), raddr=(), status='NONE')])
        self.use_metrics.update_use_metrics()
        self.assertEqual(self.use_metrics.network_connections_usage_metric.get_value(
            {"service_name": "test_service", "asv": "test_asv", "bap_component": "test_component",
             "environment": "test_env", "cluster_name": "test_cluster"}), 2)

    def test_update_use_metrics_disk_io_usage(self):
        psutil.disk_io_counters = MagicMock(
            return_value=psutil._common.sdiskio(read_count=10000, write_count=5000, read_bytes=10000000,
                                                write_bytes=5000000, read_time=500, write_time=300))
        self.use_metrics.update_use_metrics()
        self.assertEqual(self.use_metrics.disk_io_usage_metric.get_value(
            {"service_name": "test_service", "asv": "test_asv", "bap_component": "test_component",
             "environment": "test_env", "cluster_name": "test_cluster"}), 80.0)

    def test_update_use_metrics_gpu_usage(self):
        psutil.sensors_gpu = MagicMock(
            return_value=[psutil._common.sensors_gpu(index=0, fan=50, temperature=60, power_draw=100, utilization=75)])
        self.use_metrics.update_use_metrics()
        self.assertEqual(self.use_metrics.gpu_usage_metric.get_value(
            {"service_name": "test_service", "asv": "test_asv", "bap_component": "test_component",
             "environment": "test_env", "cluster_name": "test_cluster"}), 75.0)
