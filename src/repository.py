import os
import json
from typing import Dict, Any
import hashlib
from datetime import datetime

class Repository:
    """
    Manages the creation and basic operations of a source control repository.
    
    Handles:
    - Repository initialization
    - Configuration management
    - Basic repository metadata
    """
    
    def __init__(self, path: str = '.'):
        """
        Initialize a new repository or load an existing one.
        
        Args:
            path (str): Path where the repository should be created/loaded
        """
        self.repo_path = os.path.abspath(path)
        self.srccontrol_dir = os.path.join(self.repo_path, '.srccontrol')
        
        # Key repository directories and files
        self.commits_dir = os.path.join(self.srccontrol_dir, 'commits')
        self.branches_dir = os.path.join(self.srccontrol_dir, 'branches')
        self.config_file = os.path.join(self.srccontrol_dir, 'config.json')
        
    def init(self) -> bool:
        """
        Initialize a new source control repository.
        
        Creates necessary directories and configuration files.
        
        Returns:
            bool: True if initialization successful, False otherwise
        """
        try:
            # Create repository directories
            os.makedirs(self.srccontrol_dir, exist_ok=True)
            os.makedirs(self.commits_dir, exist_ok=True)
            os.makedirs(self.branches_dir, exist_ok=True)
            
            # Create initial configuration
            config = {
                'initialized_at': datetime.now().isoformat(),
                'current_branch': 'main',
                'version': '0.1.0'
            }
            
            # Write configuration to file
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=4)
            
            # Create initial main branch
            open(os.path.join(self.branches_dir, 'main'), 'w').close()
            
            return True
        
        except Exception as e:
            print(f"Repository initialization failed: {e}")
            return False
    
    def get_config(self) -> Dict[str, Any]:
        """
        Retrieve repository configuration.
        
        Returns:
            Dict[str, Any]: Repository configuration
        """
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def generate_commit_hash(self, content: str) -> str:
        """
        Generate a unique hash for a commit.
        
        Args:
            content (str): Content to hash
        
        Returns:
            str: Generated hash
        """
        return hashlib.scrypt(content.encode()).hexdigest()