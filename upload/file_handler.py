"""
File upload handler for MINDFULTEEN research data.

This module provides utilities for uploading and validating research data files.
"""

import os
import shutil
from pathlib import Path
from typing import Optional, List


class FileUploader:
    """
    A file upload handler for research data files.
    
    Supports common research data formats including CSV, TSV, JSON, and various
    neuroimaging formats.
    
    Attributes:
        upload_dir: The directory where uploaded files will be stored.
        allowed_extensions: Set of allowed file extensions.
        max_file_size: Maximum allowed file size in bytes.
    """
    
    DEFAULT_ALLOWED_EXTENSIONS = {
        '.csv', '.tsv', '.json', '.txt',  # Data formats
        '.nii', '.nii.gz',                 # Neuroimaging formats
        '.mat', '.npy', '.npz',            # MATLAB/NumPy formats
        '.xlsx', '.xls',                   # Excel formats
    }
    
    DEFAULT_MAX_SIZE = 100 * 1024 * 1024  # 100 MB
    
    def __init__(
        self,
        upload_dir: str = './uploads',
        allowed_extensions: Optional[set] = None,
        max_file_size: Optional[int] = None
    ):
        """
        Initialize the FileUploader.
        
        Args:
            upload_dir: Directory path where uploaded files will be stored.
            allowed_extensions: Set of allowed file extensions. If None, uses defaults.
            max_file_size: Maximum file size in bytes. If None, uses default of 100MB.
        """
        self.upload_dir = Path(upload_dir)
        self.allowed_extensions = allowed_extensions or self.DEFAULT_ALLOWED_EXTENSIONS
        self.max_file_size = max_file_size or self.DEFAULT_MAX_SIZE
        
    def setup(self) -> None:
        """Create the upload directory if it doesn't exist."""
        self.upload_dir.mkdir(parents=True, exist_ok=True)
        
    def validate_file(self, filepath: str) -> tuple[bool, str]:
        """
        Validate a file before upload.
        
        Args:
            filepath: Path to the file to validate.
            
        Returns:
            A tuple of (is_valid, message).
        """
        path = Path(filepath)
        
        # Check if file exists
        if not path.exists():
            return False, f"File not found: {filepath}"
        
        # Check file extension
        suffix = path.suffix.lower()
        # Handle double extensions like .nii.gz
        if path.name.endswith('.nii.gz'):
            suffix = '.nii.gz'
            
        if suffix not in self.allowed_extensions:
            return False, f"File type '{suffix}' not allowed. Allowed types: {self.allowed_extensions}"
        
        # Check file size
        file_size = path.stat().st_size
        if file_size > self.max_file_size:
            return False, f"File size ({file_size} bytes) exceeds maximum ({self.max_file_size} bytes)"
        
        return True, "File is valid"
    
    def upload(self, source_path: str, destination_name: Optional[str] = None) -> tuple[bool, str]:
        """
        Upload a file to the upload directory.
        
        Args:
            source_path: Path to the source file.
            destination_name: Optional custom name for the uploaded file.
            
        Returns:
            A tuple of (success, message or destination path).
        """
        # Ensure upload directory exists
        self.setup()
        
        # Validate file
        is_valid, message = self.validate_file(source_path)
        if not is_valid:
            return False, message
        
        source = Path(source_path)
        dest_name = destination_name or source.name
        destination = self.upload_dir / dest_name
        
        # Handle existing files
        if destination.exists():
            base = destination.stem
            suffix = destination.suffix
            counter = 1
            while destination.exists():
                destination = self.upload_dir / f"{base}_{counter}{suffix}"
                counter += 1
        
        try:
            shutil.copy2(source, destination)
            return True, str(destination)
        except (IOError, OSError) as e:
            return False, f"Failed to upload file: {e}"
    
    def list_uploads(self) -> List[str]:
        """
        List all files in the upload directory.
        
        Returns:
            List of filenames in the upload directory.
        """
        if not self.upload_dir.exists():
            return []
        
        return [f.name for f in self.upload_dir.iterdir() if f.is_file()]
    
    def delete(self, filename: str) -> tuple[bool, str]:
        """
        Delete an uploaded file.
        
        Args:
            filename: Name of the file to delete.
            
        Returns:
            A tuple of (success, message).
        """
        filepath = self.upload_dir / filename
        
        if not filepath.exists():
            return False, f"File not found: {filename}"
        
        # Security check: prevent directory traversal
        try:
            filepath.resolve().relative_to(self.upload_dir.resolve())
        except ValueError:
            return False, "Invalid file path"
        
        try:
            filepath.unlink()
            return True, f"Successfully deleted: {filename}"
        except OSError as e:
            return False, f"Failed to delete file: {e}"


def main():
    """Example usage of FileUploader."""
    uploader = FileUploader(upload_dir='./data_uploads')
    uploader.setup()
    
    print("MINDFULTEEN File Upload Utility")
    print(f"Upload directory: {uploader.upload_dir}")
    print(f"Allowed extensions: {uploader.allowed_extensions}")
    print(f"Maximum file size: {uploader.max_file_size / (1024 * 1024):.1f} MB")
    

if __name__ == '__main__':
    main()
