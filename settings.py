CPU_METRICS = ["usage", "user", "system", "iowait", "idle"]
CORE_METRICS = ["usage", "user", "system", "iowait"]

CPU_LABEL_CPU = "cpu"
CPU_LABEL_CORE = "core"
CPU_STATES = ["user", "system", "iowait", "idle"]
CPU_LABEL_STATE = "state"

METRIC_CPU_USAGE = "system.cpu.usage"
METRIC_CPU_USER = "system.cpu.user"
METRIC_CPU_SYSTEM = "system.cpu.system"
METRIC_CPU_IOWAIT = "system.cpu.iowait"
METRIC_CPU_IDLE = "system.cpu.idle"

METRIC_CORE_USAGE = "system.cpu.core.usage"
METRIC_CORE_USER = "system.cpu.core.user"
METRIC_CORE_SYSTEM = "system.cpu.core.system"
METRIC_CORE_IOWAIT = "system.cpu.core.iowait"

# memory metrics
MEMORY_METRICS = ["total", "available", "used", "free", "active", "inactive", "wired"]
METRIC_MEMORY_TOTAL = "system.memory.total"
METRIC_MEMORY_AVAILABLE = "system.memory.available"
METRIC_MEMORY_USED = "system.memory.used"
METRIC_MEMORY_FREE = "system.memory.free"
METRIC_MEMORY_ACTIVE = "system.memory.active"
METRIC_MEMORY_INACTIVE = "system.memory.inactive"
METRIC_MEMORY_WIRED = "system.memory.wired"
METRIC_MEMORY_PERCENT = "system.memory.percent"

# Disk Metrics
METRICS_DISK_READ_BYTES = "system.disk.read_bytes"
METRICS_DISK_WRITE_BYTES = "system.disk.write_bytes"
METRICS_DISK_READ_TIME = "system.disk.read_time"
METRICS_DISK_WRITE_TIME = "system.disk.write_time"
METRICS_DISK_IO_TIME = "system.disk.io_time"
METRICS_DISK_BUSY_TIME = "system.disk.busy_time"

# Label Keys
METRICS_DISK_LABEL_DEVICE = "device"

# HTTP metrics
METRICS_HTTP_DURATION_NAME = "http_duration"
METRICS_HTTP_DURATION_DESCRIPTION = "HTTP request duration"
METRICS_HTTP_DURATION_UNIT = "ms"
METRICS_HTTP_ERROR_NAME = "http_error"
METRICS_HTTP_ERROR_DESCRIPTION = "HTTP request error count"
METRICS_HTTP_ERROR_UNIT = "count"
METRICS_HTTP_IN_PROGRESS_NAME = "http_in_progress"
METRICS_HTTP_IN_PROGRESS_DESCRIPTION = "HTTP request in progress count"
METRICS_HTTP_IN_PROGRESS_UNIT = "count"
METRICS_HTTP_COMPLETED_NAME = "http_completed"
METRICS_HTTP_COMPLETED_DESCRIPTION = "HTTP request completed count"
METRICS_HTTP_COMPLETED_UNIT = "count"
METRICS_HTTP_COUNT_NAME = "http_count"
METRICS_HTTP_COUNT_DESCRIPTION = "HTTP request count"
METRICS_HTTP_COUNT_UNIT = "count"
METRICS_HTTP_REQUEST_SIZE_NAME = "http_request_size"
METRICS_HTTP_REQUEST_SIZE_DESCRIPTION = "HTTP request size"
METRICS_HTTP_REQUEST_SIZE_UNIT = "bytes"
METRICS_HTTP_RESPONSE_SIZE_NAME = "http_response_size"
METRICS_HTTP_RESPONSE_SIZE_DESCRIPTION = "HTTP response size"
METRICS_HTTP_RESPONSE_SIZE_UNIT = "bytes"
METRICS_HTTP_DURATION_PERCENTILE_NAME = "http_duration_percentile"
METRICS_HTTP_DURATION_PERCENTILE_DESCRIPTION = "HTTP request duration percentile"
METRICS_HTTP_DURATION_PERCENTILE_UNIT = "ms"

# Labels
SERVICE_NAME = "service_name"
ASV = "asv"
BAP_COMPONENT = "bap_component"
ENVIRONMENT = "environment"
CLUSTER_NAME = "cluster_name"
HTTP_LABEL_METHOD = "http_method"
HTTP_LABEL_STATUS_CODE = "http_status_code"


# Network metrics
METRICS_NETWORK_BYTES_SENT_NAME = "network.bytes_sent"
METRICS_NETWORK_BYTES_SENT_DESCRIPTION = "Bytes sent over network"
METRICS_NETWORK_BYTES_SENT_UNIT = "bytes"

METRICS_NETWORK_BYTES_RECEIVED_NAME = "network.bytes_received"
METRICS_NETWORK_BYTES_RECEIVED_DESCRIPTION = "Bytes received over network"
METRICS_NETWORK_BYTES_RECEIVED_UNIT = "bytes"

METRICS_NETWORK_ERRORS_NAME = "network.errors"
METRICS_NETWORK_ERRORS_DESCRIPTION = "Number of network errors"
METRICS_NETWORK_ERRORS_UNIT = "errors"

METRICS_NETWORK_LATENCY_NAME = "network.latency"
METRICS_NETWORK_LATENCY_DESCRIPTION = "Network latency"
METRICS_NETWORK_LATENCY_UNIT = "ms"

METRICS_NETWORK_PACKETS_SENT_NAME = "network.packets_sent"
METRICS_NETWORK_PACKETS_SENT_DESCRIPTION = "Number of packets sent over network"
METRICS_NETWORK_PACKETS_SENT_UNIT = "packets"

METRICS_NETWORK_PACKETS_RECEIVED_NAME = "network.packets_received"
METRICS_NETWORK_PACKETS_RECEIVED_DESCRIPTION = "Number of packets received over network"
METRICS_NETWORK_PACKETS_RECEIVED_UNIT = "packets"

METRICS_NETWORK_DROP_IN_NAME = "network.drop_in"
METRICS_NETWORK_DROP_IN_DESCRIPTION = "Number of incoming packets dropped by the network interface"
METRICS_NETWORK_DROP_IN_UNIT = "packets"

METRICS_NETWORK_DROP_OUT_NAME = "network.drop_out"
METRICS_NETWORK_DROP_OUT_DESCRIPTION = "Number of outgoing packets dropped by the network interface"
METRICS_NETWORK_DROP_OUT_UNIT = "packets"


# Metric names
METRICS_CPU_USAGE_NAME = "cpu_usage"
METRICS_MEMORY_USAGE_NAME = "memory_usage"
METRICS_NETWORK_BANDWIDTH_USAGE_NAME = "network_bandwidth_usage"
METRICS_DISK_IO_USAGE_NAME = "disk_io_usage"
METRICS_GPU_USAGE_NAME = "gpu_usage"

# Metric descriptions
METRICS_CPU_USAGE_DESCRIPTION = "CPU usage percentage"
METRICS_MEMORY_USAGE_DESCRIPTION = "Memory usage percentage"
METRICS_NETWORK_BANDWIDTH_USAGE_DESCRIPTION = "Network bandwidth usage percentage"
METRICS_DISK_IO_USAGE_DESCRIPTION = "Disk I/O usage percentage"
METRICS_GPU_USAGE_DESCRIPTION = "GPU usage percentage"

# Metric units
METRICS_CPU_USAGE_UNIT = "percent"
METRICS_MEMORY_USAGE_UNIT = "percent"
METRICS_NETWORK_BANDWIDTH_USAGE_UNIT = "percent"
METRICS_DISK_IO_USAGE_UNIT = "percent"
METRICS_GPU_USAGE_UNIT = "percent"

# Label keys
METRICS_LABEL_SERVICE_NAME = "service_name"
METRICS_LABEL_ASV = "asv"
METRICS_LABEL_BAP_COMPONENT = "bap_component"
METRICS_LABEL_ENVIRONMENT = "environment"
METRICS_LABEL_CLUSTER_NAME = "cluster_name"
