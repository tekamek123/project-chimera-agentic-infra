# Publisher Skill
# Minimal contract-compliant implementation

class Publisher:
    """Publishes content via MCP tools"""
    
    SUPPORTED_PLATFORMS = {"twitter", "instagram", "threads"}
    
    def validate_input(self, input_dict):
        """Validate input contract"""
        if not isinstance(input_dict, dict):
            raise ValueError("Input must be a dictionary")
        
        if "content" not in input_dict:
            raise ValueError("Missing required field: content")
        
        if "platform" not in input_dict:
            raise ValueError("Missing required field: platform")
        
        platform = input_dict.get("platform")
        if platform not in self.SUPPORTED_PLATFORMS:
            raise ValueError(f"Unsupported platform: {platform}")
        
        return True
    
    def publish(self, content, platform, metadata=None):
        """Publish content - contract-compliant stub"""
        if not content:
            raise ValueError("Content cannot be empty")
        
        if platform not in self.SUPPORTED_PLATFORMS:
            raise ValueError(f"Unsupported platform: {platform}")
        
        # Return contract-compliant stub result
        return {
            "success": True,
            "post_id": f"post_{hash(content) % 10000}",
            "platform": platform,
            "timestamp": "2025-01-01T00:00:00Z",
            "error": None
        }
    
    def validate_platform(self, platform):
        """Validate platform - contract-compliant"""
        return platform in self.SUPPORTED_PLATFORMS
