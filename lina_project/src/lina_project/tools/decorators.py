import os
import json
from datetime import datetime, timedelta
from crewai import CrewOutput
from crewai.tools import BaseTool
from crewai.project import CrewBase, agent, crew, task


from datetime import datetime
from typing import Any, Dict, Optional
from crewai.tools import BaseTool

class decorators(BaseTool):
    name: str = "Decorators"
    description: str = "Decorators for CrewAI crews."
    #args_schema: Type[BaseModel] = None

    def _run(self, argument: str) -> str:
        return "Decorators for CrewAI crews."
    
    @before_kickoff
    def validate_inputs(self, inputs: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Validate and preprocess inputs before the crew starts."""
        if inputs is None:
            return None
            
        if 'topic' not in inputs:
            raise ValueError("Topic is required")
        
        # Add additional context
        inputs['timestamp'] = datetime.now().isoformat()
        inputs['topic'] = inputs['topic'].strip().lower()
        return inputs

    @after_kickoff
    def process_results(self, result: CrewOutput) -> CrewOutput:
        """Process and format the results after the crew completes."""
        result.raw = result.raw.strip()
        result.raw = f"""
        # Research Results
        Generated on: {datetime.now().isoformat()}
        
        {result.raw}
        """
        return result
    @callback
    def log_task_completion(self, task: Task, output: str):
        """Log task completion details for monitoring."""
        print(f"Task '{task.description}' completed")
        print(f"Output length: {len(output)} characters")
        print(f"Agent used: {task.agent.role}")
        print("-" * 50)   
    
    @cache_handler
    def custom_cache(self, key: str) -> Optional[str]:
        """Custom cache implementation for storing task results."""
        cache_file = f"cache/{key}.json"
        
        if os.path.exists(cache_file):
            with open(cache_file, 'r') as f:
                data = json.load(f)
                # Check if cache is still valid (e.g., not expired)
                if datetime.fromisoformat(data['timestamp']) > datetime.now() - timedelta(days=1):
                    return data['result']
        return None