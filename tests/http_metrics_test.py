from unittest.mock import MagicMock

import pytest
from opentelemetry.metrics import MeterProvider

from http_metrics import HttpMetrics


@pytest.fixture
def http_metrics():
    meter_provider = MeterProvider()
    return HttpMetrics(meter_provider, "test_service", "test_asv", "test_component", "test_env", "test_cluster")


def test_record_duration(http_metrics):
    http_metrics.http_duration_metric.record = MagicMock()
    http_metrics.record_duration(100, {"http_method": "GET", "http_status_code": "200"})
    http_metrics.http_duration_metric.record.assert_called_once_with(100, {**http_metrics.labels,
                                                                           **{"http_method": "GET",
                                                                              "http_status_code": "200"}})


def test_record_error(http_metrics):
    http_metrics.http_error_metric.record = MagicMock()
    http_metrics.record_error({"http_method": "GET", "http_status_code": "404"})
    http_metrics.http_error_metric.record.assert_called_once_with(1, {**http_metrics.labels, **{"http_method": "GET",
                                                                                                "http_status_code": "404"}})


def test_record_in_progress(http_metrics):
    http_metrics.http_in_progress_metric.record = MagicMock()
    http_metrics.record_in_progress({"http_method": "POST", "http_status_code": "201"})
    http_metrics.http_in_progress_metric.record.assert_called_once_with(1, {**http_metrics.labels,
                                                                            **{"http_method": "POST",
                                                                               "http_status_code": "201"}})


def test_record_completed(http_metrics):
    http_metrics.http_completed_metric.record = MagicMock()
    http_metrics.record_completed({"http_method": "PUT", "http_status_code": "204"})
    http_metrics.http_completed_metric.record.assert_called_once_with(1, {**http_metrics.labels,
                                                                          **{"http_method": "PUT",
                                                                             "http_status_code": "204"}})


def test_record_count(http_metrics):
    http_metrics.http_count_metric.record = MagicMock()
    http_metrics.record_count({"http_method": "GET", "http_status_code": "200"})
    http_metrics.http_count_metric.record.assert_called_once_with(1, {**http_metrics.labels, **{"http_method": "GET",
                                                                                                "http_status_code": "200"}})


def test_record_duration_no_labels(http_metrics):
    http_metrics.http_duration_metric.record = MagicMock()
    http_metrics.record_duration(100)
    http_metrics.http_duration_metric.record.assert_called_once_with(100, http_metrics.labels)


def test_record_error_no_labels(http_metrics):
    http_metrics.http_error_metric.record = MagicMock()
    http_metrics.record_error()
    http_metrics.http_error_metric.record.assert_called_once_with(1, http_metrics.labels)


def test_record_in_progress_no_labels(http_metrics):
    http_metrics.http_in_progress_metric.record = MagicMock()
    http_metrics.record_in_progress()
    http_metrics.http_in_progress_metric.record.assert_called_once_with(1, http_metrics.labels)


def test_record_completed_no_labels(http_metrics):
    http_metrics.http_completed_metric.record = MagicMock()
    http_metrics.record_completed()
    http_metrics.http_completed_metric.record.assert_called_once_with(1, http_metrics.labels)


def test_record_count_no_labels(http_metrics):
    http_metrics.http_count_metric.record = MagicMock()
    http_metrics.record_count()
    http_metrics.http_count_metric.record.assert_called_once_with(1, http_metrics.labels)
