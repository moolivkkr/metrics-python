
## Usage

To use the `python_metrics` package, you need to create instances of the metric classes, call their `collect` methods to collect the metrics, and then call their `export` methods to export the metrics to your desired destination.

Here's an example of how to use the `python_metrics` package to collect and export all available metrics:

```python
from python_metrics import CPUMetrics, DiskMetrics, HTTPMetrics, ProcessMetrics, REDMetrics, USEMetrics

# Create instances of the metric classes
cpu_metrics = CPUMetrics()
disk_metrics = DiskMetrics()
http_metrics = HTTPMetrics()
process_metrics = ProcessMetrics()
red_metrics = REDMetrics()
use_metrics = USEMetrics()

# Collect the metrics
cpu_metrics.collect()
disk_metrics.collect()
http_metrics.collect()
process_metrics.collect()
red_metrics.collect()
use_metrics.collect()

# Export the metrics
cpu_metrics.export()
disk_metrics.export()
http_metrics.export()
process_metrics.export()
red_metrics.export()
use_metrics.export()


CPU Metrics
The CPUMetrics class provides metrics for CPU usage. It collects the following metrics:

cpu_total_usage: Total CPU usage across all cores.
cpu_per_core_usage: CPU usage broken down by core.
cpu_percent_usage: CPU usage as a percentage of total CPU capacity.