import psutil
from opentelemetry.sdk.metrics import MeterProvider
from settings import *


class UseMetrics:
    def __init__(self, meter_provider, service_name, asv, bap_component, environment, cluster_name):
        self.meter_provider = meter_provider
        self.cpu_usage_metric = self.meter_provider.get_meter("use").create_metric(
            name=METRICS_USE_CPU_USAGE_NAME, description=METRICS_USE_CPU_USAGE_DESCRIPTION, unit=METRICS_USE_CPU_USAGE_UNIT, value_type=float, label_keys=["service_name", "asv", "bap_component", "environment", "cluster_name"])
        self.memory_usage_metric = self.meter_provider.get_meter("use").create_metric(
            name=METRICS_USE_MEMORY_USAGE_NAME, description=METRICS_USE_MEMORY_USAGE_DESCRIPTION, unit=METRICS_USE_MEMORY_USAGE_UNIT, value_type=float, label_keys=["service_name", "asv", "bap_component", "environment", "cluster_name"])
        self.network_bandwidth_usage_metric = self.meter_provider.get_meter("use").create_metric(
            name=METRICS_USE_NETWORK_BANDWIDTH_USAGE_NAME, description=METRICS_USE_NETWORK_BANDWIDTH_USAGE_DESCRIPTION, unit=METRICS_USE_NETWORK_BANDWIDTH_USAGE_UNIT, value_type=float, label_keys=["service_name", "asv", "bap_component", "environment", "cluster_name"])
        self.disk_io_usage_metric = self.meter_provider.get_meter("use").create_metric(
            name=METRICS_USE_DISK_IO_USAGE_NAME, description=METRICS_USE_DISK_IO_USAGE_DESCRIPTION, unit=METRICS_USE_DISK_IO_USAGE_UNIT, value_type=float, label_keys=["service_name", "asv", "bap_component", "environment", "cluster_name"])
        self.gpu_usage_metric = self.meter_provider.get_meter("use").create_metric(
            name=METRICS_USE_GPU_USAGE_NAME, description=METRICS_USE_GPU_USAGE_DESCRIPTION, unit=METRICS_USE_GPU_USAGE_UNIT, value_type=float, label_keys=["service_name", "asv", "bap_component", "environment", "cluster_name"])
        self.service_name, self.asv, self.bap_component, self.environment, self.cluster_name = service_name, asv, bap_component, environment, cluster_name


def update_use_metrics(self):
    try:
        self.cpu_usage_metric.add(psutil.cpu_percent(interval=0.1), {"service_name": self.service_name, "asv": self.asv,
                                                                     "bap_component": self.bap_component,
                                                                     "environment": self.environment,
                                                                     "cluster_name": self.cluster_name})
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass

    try:
        self.memory_usage_metric.add(psutil.virtual_memory().percent,
                                     {"service_name": self.service_name, "asv": self.asv,
                                      "bap_component": self.bap_component, "environment": self.environment,
                                      "cluster_name": self.cluster_name})
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass

    try:
        network_io_counters = psutil.net_io_counters()
        self.network_bandwidth_usage_metric.add(
            (network_io_counters.bytes_sent + network_io_counters.bytes_recv) / network_io_counters.speed * 100,
            {"service_name": self.service_name, "asv": self.asv, "bap_component": self.bap_component,
             "environment": self.environment, "cluster_name": self.cluster_name})
        self.network_connections_usage_metric.add(len(psutil.net_connections()),
                                                  {"service_name": self.service_name, "asv": self.asv,
                                                   "bap_component": self.bap_component, "environment": self.environment,
                                                   "cluster_name": self.cluster_name})
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass

    try:
        self.disk_io_usage_metric.add(psutil.disk_io_counters().percent,
                                      {"service_name": self.service_name, "asv": self.asv,
                                       "bap_component": self.bap_component, "environment": self.environment,
                                       "cluster_name": self.cluster_name})
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass

    try:
        gpu_usage = psutil.sensors_gpu()[0].utilization
        self.gpu_usage_metric.add(gpu_usage, {"service_name": self.service_name, "asv": self.asv,
                                              "bap_component": self.bap_component, "environment": self.environment,
                                              "cluster_name": self.cluster_name})
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass
