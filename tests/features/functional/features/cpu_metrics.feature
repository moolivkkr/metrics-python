Feature: CPU Metrics

  Background:
    Given the Python Metrics application is running
    And the "/metrics" endpoint is available

  Scenario: Verify CPU metrics are collected
    When I make a GET request to "/metrics"
    Then the response body contains "python_cpu_percent_usage"
    And the response body contains "python_cpu_total_usage"
    And the response body contains "python_cpu_per_core_usage"
