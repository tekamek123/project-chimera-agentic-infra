# Content Generator Skill
# Minimal contract-compliant implementation

class ContentGenerator:
    """Generates content based on trends and persona"""
    
    SUPPORTED_PERSONAS = {"witty", "empathetic", "technical", "gen-z", "persona"}
    SUPPORTED_FORMATS = {"caption", "post", "reply"}
    
    def validate_input(self, input_dict):
        """Validate input contract"""
        if not isinstance(input_dict, dict):
            raise ValueError("Input must be a dictionary")
        
        required_fields = ["topic", "persona", "format"]
        for field in required_fields:
            if field not in input_dict:
                raise ValueError(f"Missing required field: {field}")
        
        persona = input_dict.get("persona")
        format_type = input_dict.get("format")
        
        if persona not in self.SUPPORTED_PERSONAS:
            raise ValueError(f"Unsupported persona: {persona}")
        
        if format_type not in self.SUPPORTED_FORMATS:
            raise ValueError(f"Unsupported format: {format_type}")
        
        return True
    
    def generate_content(self, topic, persona, format="caption"):
        """Generate content - contract-compliant stub"""
        if persona not in self.SUPPORTED_PERSONAS:
            raise ValueError(f"Invalid persona: {persona}")
        
        if format not in self.SUPPORTED_FORMATS:
            raise ValueError(f"Invalid format: {format}")
        
        # Return contract-compliant stub content as string
        return f"Generated {format} about {topic} with {persona} tone"
    
    def validate_persona(self, persona):
        """Validate persona - contract-compliant"""
        if persona not in self.SUPPORTED_PERSONAS:
            raise ValueError(f"Invalid persona: {persona}")
        return True
