# Trend Fetcher Skill
# Minimal contract-compliant implementation

class TrendFetcher:
    """Fetches trending topics from social platforms"""
    
    SUPPORTED_PLATFORMS = {"twitter", "tiktok", "instagram"}
    
    def validate_input(self, input_dict):
        """Validate input contract"""
        if not isinstance(input_dict, dict):
            raise ValueError("Input must be a dictionary")
        
        platform = input_dict.get("platform")
        region = input_dict.get("region")
        
        if not platform or not region:
            raise ValueError("Missing required parameters: platform and region")
        
        if platform not in self.SUPPORTED_PLATFORMS:
            raise ValueError(f"Unsupported platform: {platform}")
        
        return True
    
    def fetch_trends(self, platform, region):
        """Fetch trends - contract-compliant stub"""
        if platform not in self.SUPPORTED_PLATFORMS:
            raise ValueError(f"Invalid platform: {platform}")
        
        # Return contract-compliant stub data
        return [
            {
                "topic": "AI trends",
                "score": 0.9,
                "source": platform,
                "timestamp": "2025-01-01T00:00:00Z"
            },
            {
                "topic": "Tech news", 
                "score": 0.8,
                "source": platform,
                "timestamp": "2025-01-01T00:00:00Z"
            }
        ]
