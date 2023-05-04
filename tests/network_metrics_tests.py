import time
import unittest
from unittest.mock import Mock, patch
from opentelemetry.sdk.metrics.export import MetricRecord, MetricsExportResult, MetricsExporter
from opentelemetry.sdk.metrics import MeterProvider
from network_metrics import NetworkMetrics
from settings import *


class TestNetworkMetrics(unittest.TestCase):
    def setUp(self):
        self.meter_provider = MeterProvider()
        self.network_metrics = NetworkMetrics(self.meter_provider, "test_service", "test_asv", "test_bap_component", "test_environment", "test_cluster")
        self.host = "http://www.example.com"
        self.response_mock = Mock()
        self.response_mock.status_code = 200

    def test_update_network_metrics(self):
        net_io_counters_mock = Mock(bytes_sent=1000, bytes_recv=2000, errin=1, errout=2, packets_sent=10, packets_recv=20, dropin=5, dropout=10)
        psutil_mock = Mock(net_io_counters=lambda: net_io_counters_mock)
        with patch("psutil.net_io_counters", psutil_mock.net_io_counters):
            self.network_metrics.update_network_metrics()
        records = self.meter_provider.get_meter("test").collect()
        self.assertEqual(len(records), 7)
        for i, (name, aggregator_current) in enumerate([
            (METRICS_NETWORK_BYTES_SENT_NAME, 1000),
            (METRICS_NETWORK_BYTES_RECEIVED_NAME, 2000),
            (METRICS_NETWORK_ERRORS_NAME, 3),
            (METRICS_NETWORK_PACKETS_SENT_NAME, 10),
            (METRICS_NETWORK_PACKETS_RECEIVED_NAME, 20),
            (METRICS_NETWORK_DROP_IN_NAME, 5),
            (METRICS_NETWORK_DROP_OUT_NAME, 10),
        ]):
            self.assertEqual(records[i].name, name)
            self.assertEqual(records[i].labels, {"service_name": "test_service", "asv": "test_asv", "bap_component": "test_bap_component", "environment": "test_environment", "cluster_name": "test_cluster"})
            self.assertEqual(records[i].aggregator.current, aggregator_current)
