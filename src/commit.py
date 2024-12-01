import os
import json
from datetime import datetime
from typing import Dict, Any
from .repository import Repository
from .index import Index

class Commit:
    """
    Manages commit operations in the source control system.
    
    Handles:
    - Creating commits
    - Storing commit metadata
    """
    
    def __init__(self, repo_path: str = '.'):
        """
        Initialize Commit manager.
        
        Args:
            repo_path (str): Path to the repository
        """
        self.repo = Repository(repo_path)
        self.index = Index(repo_path)
        self.commits_dir = os.path.join(self.repo.srccontrol_dir, 'commits')
    
    def create_commit(self, message: str) -> str:
        """
        Create a new commit from staged files.
        
        Args:
            message (str): Commit message
        
        Returns:
            str: Commit hash, or empty string if commit fails
        """
        try:
            # Get staged files
            staged_files = self.index.get_staged_files()
            
            if not staged_files:
                print("No changes to commit.")
                return ""
            
            # Create commit metadata
            commit_data = {
                'timestamp': datetime.now().isoformat(),
                'message': message,
                'files': staged_files,
                'branch': self.repo.get_config().get('current_branch', 'main')
            }
            
            # Generate unique commit hash
            commit_hash = self.repo.generate_commit_hash(json.dumps(commit_data))
            
            # Store commit metadata
            commit_file = os.path.join(self.commits_dir, commit_hash)
            with open(commit_file, 'w') as f:
                json.dump(commit_data, f, indent=4)
            
            # Clear staging index after commit
            for file in staged_files:
                self.index.unstage_file(file)
            
            return commit_hash
        
        except Exception as e:
            print(f"Commit failed: {e}")
            return ""
    
    def get_commit_details(self, commit_hash: str) -> Dict[str, Any]:
        """
        Retrieve details of a specific commit.
        
        Args:
            commit_hash (str): Hash of the commit to retrieve
        
        Returns:
            Dict[str, Any]: Commit details or empty dict if not found
        """
        commit_file = os.path.join(self.commits_dir, commit_hash)
        
        try:
            with open(commit_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Commit {commit_hash} not found.")
            return {}