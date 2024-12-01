import os
import json
from typing import List, Dict, Any

class History:
    """
    Manages the commit history of the source control system.
    
    Handles:
    - Listing commits
    - Retrieving commit details
    """
    
    def __init__(self, repo_path: str = '.'):
        """
        Initialize History manager.
        
        Args:
            repo_path (str): Path to the repository
        """
        self.commits_dir = os.path.join(repo_path, '.srccontrol', 'commits')
    
    def list_commits(self, limit: int = 10, branch: str = None) -> List[Dict[str, Any]]:
        """
        List recent commits.
        
        Args:
            limit (int): Maximum number of commits to return
            branch (str, optional): Filter commits by branch
        
        Returns:
            List[Dict[str, Any]]: List of commit details
        """
        try:
            # Get all commit files, sorted by modification time
            commits = sorted(
                os.listdir(self.commits_dir),
                key=lambda x: os.path.getmtime(os.path.join(self.commits_dir, x)),
                reverse=True
            )
            
            # Filter and process commits
            commit_list = []
            for commit_hash in commits[:limit]:
                commit_file = os.path.join(self.commits_dir, commit_hash)
                
                try:
                    with open(commit_file, 'r') as f:
                        commit_data = json.load(f)
                        
                        # Optional branch filtering
                        if branch and commit_data.get('branch') != branch:
                            continue
                        
                        commit_data['hash'] = commit_hash
                        commit_list.append(commit_data)
                
                except json.JSONDecodeError:
                    continue
            
            return commit_list
        
        except FileNotFoundError:
            print("No commits found.")
            return []