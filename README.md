# MINDFULTEEN
MINDFULTEEN dFC CAPs analysis

## File Upload Utility

This project includes a file upload utility for managing research data files.

### Features

- Support for common research data formats (CSV, TSV, JSON, NIfTI, MATLAB, NumPy, Excel)
- File validation (size limits, extension checking)
- Automatic handling of duplicate filenames
- Directory traversal protection

### Usage

```python
from upload import FileUploader

# Initialize uploader
uploader = FileUploader(upload_dir='./data_uploads')

# Upload a file
success, result = uploader.upload('path/to/your/data.csv')
if success:
    print(f"File uploaded to: {result}")

# List uploaded files
files = uploader.list_uploads()
print(f"Uploaded files: {files}")

# Delete a file
success, message = uploader.delete('data.csv')
print(message)
```

### Supported File Types

- **Data formats**: .csv, .tsv, .json, .txt
- **Neuroimaging**: .nii, .nii.gz
- **MATLAB/NumPy**: .mat, .npy, .npz
- **Excel**: .xlsx, .xls

### Configuration

```python
# Custom configuration
uploader = FileUploader(
    upload_dir='./my_uploads',
    allowed_extensions={'.csv', '.json', '.nii.gz'},
    max_file_size=50 * 1024 * 1024  # 50 MB
)
```
