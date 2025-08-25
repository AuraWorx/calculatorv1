"""Unit tests for the main application."""

import pytest
from fastapi.testclient import TestClient
from app.main import app, calculate

client = TestClient(app)


class TestCalculateFunction:
    """Test cases for the calculate function."""

    def test_add_operation(self):
        """Test addition operation."""
        assert calculate(5, 3, "add") == 8
        assert calculate(-1, 1, "add") == 0
        assert calculate(0.5, 0.3, "add") == 0.8

    def test_subtract_operation(self):
        """Test subtraction operation."""
        assert calculate(5, 3, "subtract") == 2
        assert calculate(1, 1, "subtract") == 0
        assert calculate(0.5, 0.3, "subtract") == 0.2

    def test_multiply_operation(self):
        """Test multiplication operation."""
        assert calculate(5, 3, "multiply") == 15
        assert calculate(-2, 3, "multiply") == -6
        assert calculate(0.5, 0.3, "multiply") == 0.15

    def test_divide_operation(self):
        """Test division operation."""
        assert calculate(6, 2, "divide") == 3
        assert calculate(5, 2, "divide") == 2.5
        assert calculate(-6, 2, "divide") == -3

    def test_divide_by_zero(self):
        """Test division by zero raises error."""
        with pytest.raises(ValueError, match="Division by zero is not allowed"):
            calculate(5, 0, "divide")

    def test_invalid_operation(self):
        """Test invalid operation raises error."""
        with pytest.raises(ValueError, match="Unsupported operation: invalid"):
            calculate(5, 3, "invalid")


class TestAPIEndpoints:
    """Test cases for API endpoints."""

    def test_root_endpoint(self):
        """Test root endpoint returns correct information."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Calculator API"
        assert data["version"] == "1.0.0"
        assert "calculate" in data["endpoints"]
        assert "health" in data["endpoints"]

    def test_health_endpoint(self):
        """Test health endpoint returns healthy status."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"

    def test_calculate_endpoint_add(self):
        """Test calculate endpoint with addition."""
        request_data = {"a": 5, "b": 3, "operation": "add"}
        response = client.post("/calculate", json=request_data)
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 8
        assert data["operation"] == "add"
        assert data["a"] == 5
        assert data["b"] == 3

    def test_calculate_endpoint_subtract(self):
        """Test calculate endpoint with subtraction."""
        request_data = {"a": 10, "b": 4, "operation": "subtract"}
        response = client.post("/calculate", json=request_data)
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 6
        assert data["operation"] == "subtract"

    def test_calculate_endpoint_multiply(self):
        """Test calculate endpoint with multiplication."""
        request_data = {"a": 6, "b": 7, "operation": "multiply"}
        response = client.post("/calculate", json=request_data)
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 42
        assert data["operation"] == "multiply"

    def test_calculate_endpoint_divide(self):
        """Test calculate endpoint with division."""
        request_data = {"a": 15, "b": 3, "operation": "divide"}
        response = client.post("/calculate", json=request_data)
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 5
        assert data["operation"] == "divide"

    def test_calculate_endpoint_divide_by_zero(self):
        """Test calculate endpoint with division by zero."""
        request_data = {"a": 5, "b": 0, "operation": "divide"}
        response = client.post("/calculate", json=request_data)
        assert response.status_code == 400
        assert "Division by zero is not allowed" in response.json()["detail"]

    def test_calculate_endpoint_invalid_operation(self):
        """Test calculate endpoint with invalid operation."""
        request_data = {"a": 5, "b": 3, "operation": "invalid"}
        response = client.post("/calculate", json=request_data)
        assert response.status_code == 400
        assert "Unsupported operation: invalid" in response.json()["detail"]

    def test_calculate_endpoint_float_numbers(self):
        """Test calculate endpoint with float numbers."""
        request_data = {"a": 0.5, "b": 0.3, "operation": "add"}
        response = client.post("/calculate", json=request_data)
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 0.8
        assert data["operation"] == "add"


class TestErrorHandling:
    """Test cases for error handling."""

    def test_missing_required_fields(self):
        """Test missing required fields in request."""
        request_data = {"a": 5, "operation": "add"}  # Missing 'b'
        response = client.post("/calculate", json=request_data)
        assert response.status_code == 422  # Validation error

    def test_invalid_data_types(self):
        """Test invalid data types in request."""
        request_data = {"a": "invalid", "b": 3, "operation": "add"}
        response = client.post("/calculate", json=request_data)
        assert response.status_code == 422  # Validation error
