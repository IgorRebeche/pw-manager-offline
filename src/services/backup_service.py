import os
import shutil
from datetime import datetime
from pathlib import Path

class BackupService:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        self.root_folder = os.path.join(current_dir, '..', '..')
        
        self.output_folder = os.path.join(self.root_folder, 'output')
        self.backup_folder = os.path.join(self.output_folder, 'backup')
        self.data_file = os.path.join(self.output_folder, 'data.db')
        self.max_backup_files = 5  # You can adjust this as needed

    def create(self):
        # Get current date and time
        current_datetime = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        backup_file_name = f"data-{current_datetime}.db"
        backup_file_path = os.path.join(self.backup_folder, backup_file_name)
        
        # Create backup folder if it doesn't exist
        os.makedirs(self.backup_folder, exist_ok=True)

        # Copy data.db to backup folder with new name
        shutil.copy(self.data_file, backup_file_path)
        print(f"Backup created: {backup_file_name}")

    def remove_old_backup(self):
        # Get list of backup files sorted by modification time
        backup_files = sorted(Path(self.backup_folder).glob('data-*.db'), key=os.path.getmtime)

        # Check if there are more than max_backup_files
        if len(backup_files) > self.max_backup_files:
            # Delete oldest backup files until count is equal to max_backup_files
            files_to_delete = len(backup_files) - self.max_backup_files
            for i in range(files_to_delete):
                os.remove(backup_files[i])
                print(f"Old Deleted backup: {backup_files[i].name}")