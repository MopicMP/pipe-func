"""Tests for pipe-func."""

import pytest
from pipe_func import func


class TestFunc:
    """Test suite for func."""

    def test_basic(self):
        """Test basic usage."""
        result = func("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            func("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = func(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
