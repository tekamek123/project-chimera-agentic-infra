import pytest
from skills.skill_trend_fetcher import TrendFetcher
from skills.skill_content_generator import ContentGenerator
from skills.skill_publisher import Publisher


def test_skill_trend_fetcher_interface():
    """Test that trend fetcher skill follows contract"""
    fetcher = TrendFetcher()
    
    # Test input validation
    assert hasattr(fetcher, 'validate_input')
    assert hasattr(fetcher, 'fetch_trends')
    
    # Test with correct parameters
    valid_params = {"platform": "twitter", "region": "ethiopia"}
    assert fetcher.validate_input(valid_params) == True


def test_skill_content_generator_interface():
    """Test that content generator skill follows contract"""
    generator = ContentGenerator()
    
    # Test required methods exist
    assert hasattr(generator, 'generate_content')
    assert hasattr(generator, 'validate_persona')
    
    # Test input validation
    valid_input = {
        "topic": "fashion trends",
        "persona": "witty",
        "format": "caption"
    }
    assert generator.validate_input(valid_input) == True


def test_skill_publisher_interface():
    """Test that publisher skill follows contract"""
    publisher = Publisher()
    
    # Test required methods exist
    assert hasattr(publisher, 'publish')
    assert hasattr(publisher, 'validate_platform')
    
    # Test platform validation
    assert publisher.validate_platform("twitter") == True
    assert publisher.validate_platform("instagram") == True
    assert publisher.validate_platform("invalid") == False


def test_all_skills_return_expected_types():
    """Test that all skills return expected data types"""
    # This test will fail until skills are implemented
    # which is the point of TDD
    
    fetcher = TrendFetcher()
    generator = ContentGenerator()
    publisher = Publisher()
    
    # These should return specific types
    # trends: List[Dict]
    # content: String  
    # publish_result: Dict
    
    assert isinstance(fetcher.fetch_trends("twitter", "ethiopia"), list)
    assert isinstance(generator.generate_content("topic", "persona"), str)
    assert isinstance(publisher.publish("content", "twitter"), dict)
