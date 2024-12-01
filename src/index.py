import os
import json
from typing import List, Dict

class Index:
    """
    Manages the staging area for files to be committed.
    
    Handles:
    - Tracking changes
    - Staging files
    - Unstaging files
    """
    
    def __init__(self, repo_path: str = '.'):
        """
        Initialize the staging index.
        
        Args:
            repo_path (str): Path to the repository
        """
        self.repo_path = os.path.abspath(repo_path)
        self.index_file = os.path.join(self.repo_path, '.srccontrol', 'index.json')
    
    def stage_file(self, filepath: str) -> bool:
        """
        Stage a file for commit.
        
        Args:
            filepath (str): Relative path of the file to stage
        
        Returns:
            bool: True if staging successful, False otherwise
        """
        try:
            # Ensure the file exists
            full_path = os.path.join(self.repo_path, filepath)
            if not os.path.exists(full_path):
                print(f"File not found: {filepath}")
                return False
            
            # Read current index
            index = self._read_index()
            
            # Add or update file in index
            index[filepath] = {
                'mtime': os.path.getmtime(full_path),
                'size': os.path.getsize(full_path)
            }
            
            # Write updated index
            self._write_index(index)
            return True
        
        except Exception as e:
            print(f"Error staging file: {e}")
            return False
    
    def unstage_file(self, filepath: str) -> bool:
        """
        Remove a file from the staging area.
        
        Args:
            filepath (str): Relative path of the file to unstage
        
        Returns:
            bool: True if unstaging successful, False otherwise
        """
        try:
            index = self._read_index()
            
            if filepath in index:
                del index[filepath]
                self._write_index(index)
                return True
            
            return False
        
        except Exception as e:
            print(f"Error unstaging file: {e}")
            return False
    
    def get_staged_files(self) -> List[str]:
        """
        Retrieve list of currently staged files.
        
        Returns:
            List[str]: Staged file paths
        """
        return list(self._read_index().keys())
    
    def _read_index(self) -> Dict[str, Dict]:
        """
        Read the current index from file.
        
        Returns:
            Dict[str, Dict]: Staged files and their metadata
        """
        try:
            with open(self.index_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def _write_index(self, index: Dict[str, Dict]):
        """
        Write the index to file.
        
        Args:
            index (Dict[str, Dict]): Index to write
        """
        with open(self.index_file, 'w') as f:
            json.dump(index, f, indent=4)