# Getting Started with Machine Learning in Python

Welcome to the Machine Learning with Python course! This guide will help you set up your development environment and get started with the course materials.

## Table of Contents

1. [System Requirements](#system-requirements)
2. [Installing Python](#installing-python)
3. [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)
4. [Installing Dependencies](#installing-dependencies)
5. [Installing Jupyter Notebook](#installing-jupyter-notebook)
6. [Verifying Your Installation](#verifying-your-installation)
7. [IDE Recommendations](#ide-recommendations)
8. [Troubleshooting](#troubleshooting)

## System Requirements

- **Operating System**: Windows 10+, macOS 10.14+, or Linux
- **RAM**: Minimum 4GB (8GB or more recommended)
- **Disk Space**: At least 5GB free space
- **Internet Connection**: Required for downloading libraries and datasets

## Installing Python

### Windows

1. Download Python 3.8 or later from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important**: Check "Add Python to PATH" during installation
4. Verify installation by opening Command Prompt and running:
   ```bash
   python --version
   ```

### macOS

1. Install Homebrew if not already installed:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Install Python:
   ```bash
   brew install python@3.11
   ```

3. Verify installation:
   ```bash
   python3 --version
   ```

### Linux (Ubuntu/Debian)

1. Update package list:
   ```bash
   sudo apt update
   ```

2. Install Python:
   ```bash
   sudo apt install python3 python3-pip python3-venv
   ```

3. Verify installation:
   ```bash
   python3 --version
   ```

## Setting Up a Virtual Environment

Virtual environments help keep project dependencies isolated. Follow these steps:

### Windows

```bash
# Navigate to the course directory
cd Machine-Learning-with-Python-SDC

# Create a virtual environment
python -m venv ml_env

# Activate the virtual environment
ml_env\Scripts\activate
```

### macOS/Linux

```bash
# Navigate to the course directory
cd Machine-Learning-with-Python-SDC

# Create a virtual environment
python3 -m venv ml_env

# Activate the virtual environment
source ml_env/bin/activate
```

You should see `(ml_env)` at the beginning of your command prompt when the environment is active.

## Installing Dependencies

With your virtual environment activated, install the required packages:

```bash
# Upgrade pip
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

This will install:
- NumPy: Numerical computing
- Pandas: Data manipulation
- Matplotlib & Seaborn: Data visualization
- Scikit-learn: Machine learning algorithms
- Jupyter: Interactive notebooks
- And other essential libraries

## Installing Jupyter Notebook

Jupyter Notebook should be installed as part of the requirements. To launch it:

```bash
# Start Jupyter Notebook
jupyter notebook
```

This will open a browser window with the Jupyter interface. You can now navigate to the course notebooks and start learning!

### Alternative: JupyterLab

For a more modern interface, you can use JupyterLab:

```bash
# Install JupyterLab (if not already installed)
pip install jupyterlab

# Launch JupyterLab
jupyter lab
```

## Verifying Your Installation

Create a new Python file or Jupyter notebook and run the following code to verify all packages are installed correctly:

```python
import sys
print(f"Python version: {sys.version}")

import numpy as np
print(f"NumPy version: {np.__version__}")

import pandas as pd
print(f"Pandas version: {pd.__version__}")

import matplotlib
print(f"Matplotlib version: {matplotlib.__version__}")

import sklearn
print(f"Scikit-learn version: {sklearn.__version__}")

print("\n✅ All packages installed successfully!")
```

Expected output should show version numbers without any errors.

## IDE Recommendations

### For Beginners
- **Jupyter Notebook**: Best for interactive learning and experimentation
- **Google Colab**: Free cloud-based Jupyter notebooks (no installation required)
  - Visit [colab.research.google.com](https://colab.research.google.com)

### For Development
- **Visual Studio Code**: Excellent Python support with extensions
  - Install Python extension
  - Install Jupyter extension
- **PyCharm Community Edition**: Powerful Python IDE
- **Spyder**: Scientific Python IDE (comes with Anaconda)

## Using Google Colab (Alternative to Local Setup)

If you face installation issues, you can use Google Colab:

1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Sign in with your Google account
3. Click "File" → "Open Notebook" → "GitHub"
4. Enter the repository URL
5. Select a notebook to start learning

**Note**: Most common ML libraries are pre-installed in Colab.

## Common Commands

### Activating Virtual Environment

```bash
# Windows
ml_env\Scripts\activate

# macOS/Linux
source ml_env/bin/activate
```

### Deactivating Virtual Environment

```bash
deactivate
```

### Updating Packages

```bash
pip install --upgrade -r requirements.txt
```

### Installing Additional Packages

```bash
pip install package_name
```

## Troubleshooting

### Issue: "python is not recognized" (Windows)

**Solution**: Add Python to PATH
1. Search for "Environment Variables" in Windows
2. Edit PATH variable
3. Add Python installation directory
4. Restart Command Prompt

### Issue: "No module named 'xyz'"

**Solution**: Install the missing package
```bash
pip install xyz
```

### Issue: Permission denied when installing packages

**Solution**: Use `--user` flag
```bash
pip install --user package_name
```

Or use `sudo` on Linux/macOS (not recommended in virtual environments):
```bash
sudo pip install package_name
```

### Issue: Jupyter Notebook kernel keeps dying

**Solutions**:
1. Update Jupyter: `pip install --upgrade jupyter`
2. Check RAM usage (close other applications)
3. Restart the kernel: Kernel → Restart

### Issue: Import errors after installation

**Solution**: Ensure virtual environment is activated
- Check for `(ml_env)` in command prompt
- Restart terminal/IDE
- Reinstall packages: `pip install -r requirements.txt`

## Getting Help

If you encounter issues not covered here:

1. **Check Module READMEs**: Each module has specific setup instructions
2. **Search Online**: Stack Overflow is a great resource
3. **Ask Instructors**: During office hours or via course forum
4. **GitHub Issues**: Open an issue in this repository

## Next Steps

Once your environment is set up:

1. Read the [SYLLABUS.md](SYLLABUS.md) for course details
2. Start with Module 1: Introduction to Machine Learning
3. Work through the notebooks sequentially
4. Complete practice exercises
5. Join the course community

## Additional Resources

### Learning Python Basics
- [Python.org Beginners Guide](https://www.python.org/about/gettingstarted/)
- [Real Python Tutorials](https://realpython.com/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)

### Git and GitHub
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [GitHub Learning Lab](https://lab.github.com/)

### Command Line Basics
- [Command Line Crash Course](https://learnpythonthehardway.org/book/appendixa.html)

---

**You're all set! Happy Learning! 🚀**

If you found this guide helpful, consider giving this repository a ⭐ on GitHub!
