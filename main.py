import os
import argparse
from src.repository import Repository
from src.index import Index
from src.commit import Commit
from src.history import History

def main():
    """
    Command-line interface for the source control system.
    
    Provides commands for:
    - Initializing repositories
    - Staging files
    - Committing changes
    - Viewing commit history
    """
    parser = argparse.ArgumentParser(description='Simple Source Control System')
    
    # Repository commands
    parser.add_argument('--init', action='store_true', 
                        help='Initialize a new repository')
    
    # Staging commands
    parser.add_argument('--stage', type=str, 
                        help='Stage a file for commit')
    parser.add_argument('--unstage', type=str, 
                        help='Unstage a file')
    
    # Commit commands
    parser.add_argument('--commit', type=str, 
                        help='Commit staged changes with a message')
    
    # History commands
    parser.add_argument('--history', action='store_true', 
                        help='View commit history')
    parser.add_argument('--limit', type=int, default=10, 
                        help='Limit number of history entries')
    
    args = parser.parse_args()
    
    # Repository initialization
    if args.init:
        repo = Repository()
        if repo.init():
            print("Repository initialized successfully.")
    
    # Staging files
    if args.stage:
        index = Index()
        if index.stage_file(args.stage):
            print(f"Staged: {args.stage}")
    
    # Unstaging files
    if args.unstage:
        index = Index()
        if index.unstage_file(args.unstage):
            print(f"Unstaged: {args.unstage}")
    
    # Committing changes
    if args.commit:
        committer = Commit()
        commit_hash = committer.create_commit(args.commit)
        if commit_hash:
            print(f"Commit created: {commit_hash}")
    
    # View commit history
    if args.history:
        history = History()
        commits = history.list_commits(limit=args.limit)
        for commit in commits:
            print(f"Commit {commit['hash']}:")
            print(f"  Message: {commit['message']}")
            print(f"  Timestamp: {commit['timestamp']}")
            print(f"  Branch: {commit['branch']}")
            print(f"  Files: {', '.join(commit['files'])}\n")

if __name__ == '__main__':
    main()