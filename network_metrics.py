import time
import psutil
from opentelemetry.sdk.metrics import Counter, ValueRecorder, MeterProvider
from settings import *


class NetworkMetrics:
    def __init__(self, meter_provider, service_name, asv, bap_component, environment, cluster_name):
        self.metrics = {
            METRICS_NETWORK_BYTES_SENT_NAME: Counter(METRICS_NETWORK_BYTES_SENT_DESCRIPTION,
                                                     METRICS_NETWORK_BYTES_SENT_UNIT, int, meter_provider,
                                                     [SERVICE_NAME, ASV, BAP_COMPONENT, ENVIRONMENT, CLUSTER_NAME]),
            METRICS_NETWORK_BYTES_RECEIVED_NAME: Counter(METRICS_NETWORK_BYTES_RECEIVED_DESCRIPTION,
                                                         METRICS_NETWORK_BYTES_RECEIVED_UNIT, int, meter_provider,
                                                         [SERVICE_NAME, ASV, BAP_COMPONENT, ENVIRONMENT, CLUSTER_NAME]),
            METRICS_NETWORK_ERRORS_NAME: Counter(METRICS_NETWORK_ERRORS_DESCRIPTION, METRICS_NETWORK_ERRORS_UNIT, int,
                                                 meter_provider,
                                                 [SERVICE_NAME, ASV, BAP_COMPONENT, ENVIRONMENT, CLUSTER_NAME]),
            METRICS_NETWORK_LATENCY_NAME: ValueRecorder(METRICS_NETWORK_LATENCY_DESCRIPTION,
                                                        METRICS_NETWORK_LATENCY_UNIT, meter_provider,
                                                        [SERVICE_NAME, ASV, BAP_COMPONENT, ENVIRONMENT, CLUSTER_NAME]),
            METRICS_NETWORK_PACKETS_SENT_NAME: Counter(METRICS_NETWORK_PACKETS_SENT_DESCRIPTION,
                                                       METRICS_NETWORK_PACKETS_SENT_UNIT, int, meter_provider,
                                                       [SERVICE_NAME, ASV, BAP_COMPONENT, ENVIRONMENT, CLUSTER_NAME]),
            METRICS_NETWORK_PACKETS_RECEIVED_NAME: Counter(METRICS_NETWORK_PACKETS_RECEIVED_DESCRIPTION,
                                                           METRICS_NETWORK_PACKETS_RECEIVED_UNIT, int, meter_provider,
                                                           [SERVICE_NAME, ASV, BAP_COMPONENT, ENVIRONMENT,
                                                            CLUSTER_NAME]),
            METRICS_NETWORK_DROP_IN_NAME: Counter(METRICS_NETWORK_DROP_IN_DESCRIPTION, METRICS_NETWORK_DROP_IN_UNIT,
                                                  int, meter_provider,
                                                  [SERVICE_NAME, ASV, BAP_COMPONENT, ENVIRONMENT, CLUSTER_NAME]),
            METRICS_NETWORK_DROP_OUT_NAME: Counter(METRICS_NETWORK_DROP_OUT_DESCRIPTION, METRICS_NETWORK_DROP_OUT_UNIT,
                                                   int, meter_provider,
                                                   [SERVICE_NAME, ASV, BAP_COMPONENT, ENVIRONMENT, CLUSTER_NAME]),
        }

    def update_network_metrics(self):
        net_io_counters = psutil.net_io_counters()
        self.metrics[METRICS_NETWORK_BYTES_SENT_NAME].add(net_io_counters.bytes_sent)
        self.metrics[METRICS_NETWORK_BYTES_RECEIVED_NAME].add(net_io_counters.bytes_recv)
        self.metrics[METRICS_NETWORK_ERRORS_NAME].add(net_io_counters.errin + net_io_counters.errout)
        self.metrics[METRICS_NETWORK_PACKETS_SENT_NAME].add(net_io_counters.packets_sent)
        self.metrics[METRICS_NETWORK_PACKETS_RECEIVED_NAME].add(net_io_counters.packets_recv)
        self.metrics[METRICS_NETWORK_DROP_IN_NAME].add(net_io_counters.dropin)
        self.metrics[METRICS_NETWORK_DROP_OUT_NAME].add(net_io_counters.dropout)

    def update_network_latency(self, host):
        try:
            start_time = time.monotonic()
            response = requests.get(host)
            duration = int((time.monotonic() - start_time) * 1000)
            self.metrics[METRICS_NETWORK_LATENCY_NAME].record(duration)
        except requests.exceptions.RequestException:
            pass

    def shutdown(self):
        pass
