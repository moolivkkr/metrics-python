import time

from opentelemetry.sdk.metrics import Counter, ValueRecorder

from settings import *


class HTTPMetrics:
    def __init__(self, meter_provider, service_name, asv, bap_component, environment, cluster_name):
        self.metrics = {
            METRICS_HTTP_DURATION_NAME: ValueRecorder(METRICS_HTTP_DURATION_DESCRIPTION, METRICS_HTTP_DURATION_UNIT,
                                                      meter_provider,
                                                      [SERVICE_NAME, ASV, BAP_COMPONENT, ENVIRONMENT, CLUSTER_NAME]),
            METRICS_HTTP_ERROR_NAME: Counter(METRICS_HTTP_ERROR_DESCRIPTION, METRICS_HTTP_ERROR_UNIT,
                                             [HTTP_LABEL_METHOD, HTTP_LABEL_STATUS_CODE], int, meter_provider,
                                             [SERVICE_NAME, ASV, BAP_COMPONENT, ENVIRONMENT, CLUSTER_NAME]),
            METRICS_HTTP_IN_PROGRESS_NAME: Counter(METRICS_HTTP_IN_PROGRESS_DESCRIPTION, METRICS_HTTP_IN_PROGRESS_UNIT,
                                                   [HTTP_LABEL_METHOD], int, meter_provider,
                                                   [SERVICE_NAME, ASV, BAP_COMPONENT, ENVIRONMENT, CLUSTER_NAME]),
            METRICS_HTTP_COMPLETED_NAME: Counter(METRICS_HTTP_COMPLETED_DESCRIPTION, METRICS_HTTP_COMPLETED_UNIT,
                                                 [HTTP_LABEL_METHOD, HTTP_LABEL_STATUS_CODE], int, meter_provider,
                                                 [SERVICE_NAME, ASV, BAP_COMPONENT, ENVIRONMENT, CLUSTER_NAME]),
            METRICS_HTTP_COUNT_NAME: Counter(METRICS_HTTP_COUNT_DESCRIPTION, METRICS_HTTP_COUNT_UNIT,
                                             [HTTP_LABEL_METHOD], int, meter_provider,
                                             [SERVICE_NAME, ASV, BAP_COMPONENT, ENVIRONMENT, CLUSTER_NAME]),
            METRICS_HTTP_REQUEST_SIZE_NAME: ValueRecorder(METRICS_HTTP_REQUEST_SIZE_DESCRIPTION,
                                                          METRICS_HTTP_REQUEST_SIZE_UNIT, meter_provider,
                                                          [SERVICE_NAME, ASV, BAP_COMPONENT, ENVIRONMENT,
                                                           CLUSTER_NAME]),
            METRICS_HTTP_RESPONSE_SIZE_NAME: ValueRecorder(METRICS_HTTP_RESPONSE_SIZE_DESCRIPTION,
                                                           METRICS_HTTP_RESPONSE_SIZE_UNIT, meter_provider,
                                                           [SERVICE_NAME, ASV, BAP_COMPONENT, ENVIRONMENT,
                                                            CLUSTER_NAME]),
            METRICS_HTTP_DURATION_PERCENTILE_NAME: ValueRecorder(METRICS_HTTP_DURATION_PERCENTILE_DESCRIPTION,
                                                                 METRICS_HTTP_DURATION_PERCENTILE_UNIT, meter_provider,
                                                                 [SERVICE_NAME, ASV, BAP_COMPONENT, ENVIRONMENT,
                                                                  CLUSTER_NAME, HTTP_LABEL_METHOD],
                                                                 aggregator=MinMaxSumCountAggregator()),
        }

    def update_http_metrics(self, method, status_code, start_time, request_size, response_size):
        duration = int((time.time() - start_time) * 1000)
        self.metrics[METRICS_HTTP_DURATION_NAME].record(duration)
        self.metrics[METRICS_HTTP_COUNT_NAME].labels(method=method).inc()
        self.metrics[METRICS_HTTP_IN_PROGRESS_NAME].labels(method=method).dec()
        if status_code < 200 or status_code >= 400:
            self.metrics[METRICS_HTTP_ERROR_NAME].labels(method=method, status_code=str(status_code)).inc()
        else:
            self.metrics[METRICS_HTTP_COMPLETED_NAME].labels(method=method, status_code=str(status_code)).inc()
        self.metrics[METRICS_HTTP_REQUEST_SIZE_NAME].record(request_size)
        self.metrics[METRICS_HTTP_RESPONSE_SIZE_NAME].record(response_size)
        self.metrics[METRICS_HTTP_DURATION_PERCENTILE_NAME].record(duration, labels={HTTP_LABEL_METHOD: method})

    def shutdown(self):
        pass
