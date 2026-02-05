import pytest
from skills.skill_trend_fetcher import TrendFetcher


def test_trend_fetcher_input_contract():
    """Test that trend fetcher accepts correct input schema"""
    fetcher = TrendFetcher()
    
    # Valid input should not raise exception
    valid_input = {
        "platform": "twitter",
        "region": "ethiopia"
    }
    assert fetcher.validate_input(valid_input) == True


def test_trend_fetcher_output_contract():
    """Test that trend fetcher returns correct output schema"""
    fetcher = TrendFetcher()
    
    # Should return list of trend objects
    result = fetcher.fetch_trends("twitter", "ethiopia")
    
    assert isinstance(result, list)
    if len(result) > 0:
        assert all(isinstance(trend, dict) for trend in result)
        assert all("topic" in trend for trend in result)
        assert all("score" in trend for trend in result)


def test_trend_fetcher_error_handling():
    """Test that trend fetcher handles errors gracefully"""
    fetcher = TrendFetcher()
    
    # Invalid platform should raise specific error
    with pytest.raises(ValueError, match="Invalid platform"):
        fetcher.fetch_trends("invalid_platform", "ethiopia")