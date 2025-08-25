"""Integration tests for the Calculator API."""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestIntegrationScenarios:
    """Integration test scenarios for the Calculator API."""

    def test_complete_calculation_workflow(self):
        """Test complete workflow of multiple calculations."""
        # Test addition
        add_response = client.post("/calculate", json={"a": 10, "b": 5, "operation": "add"})
        assert add_response.status_code == 200
        assert add_response.json()["result"] == 15

        # Test subtraction
        sub_response = client.post("/calculate", json={"a": 20, "b": 8, "operation": "subtract"})
        assert sub_response.status_code == 200
        assert sub_response.json()["result"] == 12

        # Test multiplication
        mul_response = client.post("/calculate", json={"a": 6, "b": 7, "operation": "multiply"})
        assert mul_response.status_code == 200
        assert mul_response.json()["result"] == 42

        # Test division
        div_response = client.post("/calculate", json={"a": 100, "b": 4, "operation": "divide"})
        assert div_response.status_code == 200
        assert div_response.json()["result"] == 25

    def test_api_consistency_across_endpoints(self):
        """Test API consistency across different endpoints."""
        # Check root endpoint
        root_response = client.get("/")
        assert root_response.status_code == 200
        root_data = root_response.json()
        
        # Check health endpoint
        health_response = client.get("/health")
        assert health_response.status_code == 200
        health_data = health_response.json()
        
        # Verify consistency
        assert root_data["version"] == "1.0.0"
        assert health_data["status"] == "healthy"

    def test_error_handling_integration(self):
        """Test error handling across different scenarios."""
        # Test invalid operation
        invalid_op_response = client.post("/calculate", json={"a": 5, "b": 3, "operation": "power"})
        assert invalid_op_response.status_code == 400
        
        # Test division by zero
        div_zero_response = client.post("/calculate", json={"a": 10, "b": 0, "operation": "divide"})
        assert div_zero_response.status_code == 400
        
        # Test malformed request
        malformed_response = client.post("/calculate", json={"a": "invalid", "b": 3, "operation": "add"})
        assert malformed_response.status_code == 422

    def test_concurrent_requests(self):
        """Test handling of concurrent requests."""
        import concurrent.futures
        import time
        
        def make_request():
            response = client.post("/calculate", json={"a": 5, "b": 3, "operation": "add"})
            return response.json()["result"]
        
        # Make 5 concurrent requests
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(make_request) for _ in range(5)]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]
        
        # All results should be the same
        assert all(result == 8 for result in results)

    def test_data_persistence_consistency(self):
        """Test that API responses are consistent and don't affect subsequent requests."""
        # First request
        response1 = client.post("/calculate", json={"a": 10, "b": 5, "operation": "add"})
        result1 = response1.json()["result"]
        
        # Second request with same parameters
        response2 = client.post("/calculate", json={"a": 10, "b": 5, "operation": "add"})
        result2 = response2.json()["result"]
        
        # Results should be identical
        assert result1 == result2 == 15
        
        # Different request should not affect previous results
        response3 = client.post("/calculate", json={"a": 20, "b": 10, "operation": "multiply"})
        result3 = response3.json()["result"]
        assert result3 == 200
        
        # Verify first result is still correct
        response4 = client.post("/calculate", json={"a": 10, "b": 5, "operation": "add"})
        result4 = response4.json()["result"]
        assert result4 == 15
