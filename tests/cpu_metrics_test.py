import unittest
from unittest.mock import patch, MagicMock

from opentelemetry.sdk.metrics import MeterProvider

from cpu_metrics import CPUMetrics
from settings import *


class TestCPUMetrics(unittest.TestCase):
    def setUp(self):
        self.meter_provider = MeterProvider()
        self.labels = {
            "service_name": "my_service",
            "asv": "123",
            "bap_component": "my_component",
            "environment": "dev",
            "cluster_name": "my_cluster"
        }
        self.cpu_metrics = CPUMetrics(self.meter_provider, **self.labels)

    @patch("psutil.cpu_times")
    def test_create_cpu_metrics(self, mock_cpu_times):
        mock_cpu_times.return_value = [
            MagicMock(user=1000, system=500, idle=500, iowait=0),
            MagicMock(user=500, system=200, idle=700, iowait=0)
        ]
        self.cpu_metrics.create_cpu_metrics()
        cpu_counters = self.cpu_metrics.cpu_counters

        self.assertEqual(len(cpu_counters), 10)
        for i in range(2):
            for metric in CPU_METRICS:
                cpu_usage_metric = cpu_counters[f"cpu_{metric}_{i}"]
                self.assertEqual(cpu_usage_metric.name, f"system.cpu.{metric}")
                self.assertEqual(cpu_usage_metric.description, f"CPU {metric.capitalize()}")
                self.assertEqual(cpu_usage_metric.unit, "1")
                self.assertEqual(cpu_usage_metric.value_type, int)
                self.assertIsInstance(cpu_usage_metric, Counter)
                self.assertEqual(cpu_usage_metric.labels,
                                 {CPU_LABEL_CPU: str(i), **self.labels, CPU_LABEL_STATE: CPU_STATES})
                self.assertEqual(cpu_usage_metric.instrument,
                                 self.meter_provider.get_meter(__name__).instruments[cpu_usage_metric.name])

    @patch("psutil.cpu_times")
    def test_create_core_metrics(self, mock_cpu_times):
        mock_cpu_times.return_value = [
            MagicMock(user=1000, system=500, idle=500, iowait=0),
            MagicMock(user=500, system=200, idle=700, iowait=0)
        ]
        self.cpu_metrics.create_core_metrics()
        core_counters = self.cpu_metrics.core_counters

        self.assertEqual(len(core_counters), 8)
        for i, j in [(i, j) for i in range(2) for j in range(4)]:
            for metric in CORE_METRICS:
                core_usage_metric = core_counters[f"core_{metric}_{i}.{j}"]
                self.assertEqual(core_usage_metric.name, f"system.cpu.{metric}")
                self.assertEqual(core_usage_metric.description, f"CPU {metric.capitalize()} per core")
                self.assertEqual(core_usage_metric.unit, "1")
                self.assertEqual(core_usage_metric.value_type, int)
                self.assertIsInstance(core_usage_metric, Counter)
                self.assertEqual(core_usage_metric.labels,
                                 {CPU_LABEL_CPU: str(i), CPU_LABEL_CORE: str(j), **self.labels,
                                  CPU_LABEL_STATE: CPU_STATES})
                self.assertEqual(core_usage_metric.instrument,
                                 self.meter_provider.get_meter(__name__).instruments[core_usage_metric.name])


if __name__ == "__main__":
    unittest.main()
