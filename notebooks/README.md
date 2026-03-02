# Jupyter Notebooks

This directory contains interactive Jupyter notebooks that complement the course modules. These notebooks provide hands-on coding examples and exercises.

## Organization

Notebooks are organized by module:

```
notebooks/
├── module-01-introduction/      # ML basics and Python libraries
├── module-02-preprocessing/     # Data preparation techniques
├── module-03-regression/        # Regression algorithms
├── module-04-classification/    # Classification algorithms
├── module-05-unsupervised/      # Clustering and dimensionality reduction
├── module-06-optimization/      # Model tuning and evaluation
├── module-07-deep-learning/     # Neural networks and CNNs
└── module-08-projects/          # Complete project examples
```

## How to Use These Notebooks

### 1. Setup
First, ensure you have Jupyter installed:
```bash
pip install jupyter jupyterlab
```

### 2. Launch Jupyter
```bash
# From the repository root
jupyter notebook

# Or for JupyterLab
jupyter lab
```

### 3. Navigate
Open the notebooks directory and select a notebook to explore.

### 4. Interactive Learning
- Read through the explanations
- Run each code cell (Shift + Enter)
- Modify code to experiment
- Complete exercises at the end

## Notebook Types

### 📘 Tutorial Notebooks
Step-by-step guides with explanations:
- Clear explanations of concepts
- Code examples with outputs
- Visualizations
- Best practices

**Example**: `module-01-introduction/numpy_tutorial.ipynb`

### 🔬 Experiment Notebooks
Explore and compare different approaches:
- Side-by-side comparisons
- Performance analysis
- Parameter exploration

**Example**: `module-04-classification/comparing_classifiers.ipynb`

### 💪 Exercise Notebooks
Practice problems with solutions:
- Problem statements
- Starter code
- Hints
- Solutions (in separate file)

**Example**: `module-02-preprocessing/data_cleaning_exercises.ipynb`

### 🚀 Project Notebooks
End-to-end project examples:
- Real-world datasets
- Complete workflow
- Best practices
- Professional documentation

**Example**: `module-08-projects/customer_churn_prediction.ipynb`

## Best Practices

### Working with Notebooks

1. **Always Run Cells in Order**
   - Cells may depend on previous cells
   - Use "Run All" to ensure consistency

2. **Save Frequently**
   - Jupyter auto-saves, but manual saves are safer
   - Ctrl+S (Cmd+S on Mac)

3. **Clear Outputs Before Committing**
   - Keeps repository clean
   - Cell → All Output → Clear

4. **Add Markdown Explanations**
   - Document your thought process
   - Explain non-obvious code
   - Include observations

5. **Use Descriptive Variable Names**
   ```python
   # Good
   customer_age = 25
   
   # Bad
   x = 25
   ```

### Markdown Tips

Notebooks support rich formatting:

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*

- Bullet point
- Another point

1. Numbered list
2. Second item

`inline code`

```python
# Code block
def hello():
    print("Hello!")
```

[Link text](https://example.com)

![Image](image.png)

$$ LaTeX Math: y = mx + b $$
```

## Keyboard Shortcuts

### Command Mode (press Esc)
- `A` - Insert cell above
- `B` - Insert cell below
- `D, D` - Delete cell
- `M` - Change to markdown
- `Y` - Change to code
- `Z` - Undo cell deletion

### Edit Mode (press Enter)
- `Shift + Enter` - Run cell, select below
- `Ctrl + Enter` - Run cell
- `Alt + Enter` - Run cell, insert below
- `Ctrl + /` - Comment/uncomment

## Troubleshooting

### Kernel Issues

**Problem**: Kernel keeps dying
```python
# Solution: Reduce memory usage
# Use smaller datasets or sampling
df_sample = df.sample(n=10000)
```

**Problem**: Kernel not found
```bash
# Install ipykernel
pip install ipykernel
python -m ipykernel install --user
```

### Import Errors

**Problem**: Module not found
```bash
# Install in the correct environment
pip install package_name

# Or install from notebook
!pip install package_name
```

### Display Issues

**Problem**: Plots not showing
```python
# Add this at the beginning of notebook
%matplotlib inline

# Or use
import matplotlib.pyplot as plt
plt.show()
```

## Tips for Learning

1. **Don't Just Read - Code!**
   - Type code yourself
   - Don't just run existing cells
   - Experiment with modifications

2. **Break Things**
   - Change parameters to see effects
   - Try different approaches
   - Learn from errors

3. **Visualize Often**
   - Plot data frequently
   - Understand distributions
   - Verify transformations

4. **Document Your Learning**
   - Add markdown notes
   - Explain in your own words
   - Keep a learning journal

5. **Complete All Exercises**
   - Don't skip exercises
   - Try before checking solutions
   - Understand why solutions work

## Creating Your Own Notebooks

### Template Structure

```python
# Title: Project Name
# Author: Your Name
# Date: YYYY-MM-DD
# Description: Brief description

# 1. Setup and Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 2. Load Data
# ...

# 3. Exploratory Data Analysis
# ...

# 4. Data Preprocessing
# ...

# 5. Model Training
# ...

# 6. Evaluation
# ...

# 7. Conclusions
# ...
```

### Naming Conventions

- Use lowercase with underscores
- Include module number
- Be descriptive
- Examples:
  - `01_intro_to_pandas.ipynb`
  - `04_random_forest_classification.ipynb`
  - `08_customer_segmentation_project.ipynb`

## Notebook Collections

### Getting Started (Week 1-2)
- `python_refresher.ipynb`
- `numpy_essentials.ipynb`
- `pandas_fundamentals.ipynb`
- `matplotlib_basics.ipynb`

### Data Preparation (Week 3-4)
- `exploratory_data_analysis.ipynb`
- `handling_missing_data.ipynb`
- `feature_engineering.ipynb`
- `data_scaling_techniques.ipynb`

### Machine Learning (Week 5-14)
- `linear_regression_from_scratch.ipynb`
- `logistic_regression_tutorial.ipynb`
- `decision_trees_visualization.ipynb`
- `random_forest_deep_dive.ipynb`
- `svm_kernel_comparison.ipynb`
- `clustering_algorithms.ipynb`
- `pca_dimensionality_reduction.ipynb`
- `neural_networks_keras.ipynb`

### Projects (Week 15-16)
- `house_price_prediction.ipynb`
- `customer_churn_analysis.ipynb`
- `sentiment_analysis_nlp.ipynb`
- `image_classification_cnn.ipynb`

## Additional Resources

### Jupyter Extensions
```bash
# Useful extensions
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

# Popular extensions:
# - Table of Contents
# - Variable Inspector
# - ExecuteTime
# - Code folding
```

### JupyterLab Extensions
```bash
# Modern interface
pip install jupyterlab

# Extensions for JupyterLab 3.x+
pip install jupyterlab-git
pip install jupyterlab-lsp
```

### Export Options

Export notebooks to different formats:
```bash
# HTML
jupyter nbconvert --to html notebook.ipynb

# PDF (requires LaTeX)
jupyter nbconvert --to pdf notebook.ipynb

# Python script
jupyter nbconvert --to script notebook.ipynb

# Markdown
jupyter nbconvert --to markdown notebook.ipynb
```

## Contributing Notebooks

Want to add your own notebooks?

1. Follow the template structure
2. Clear all outputs
3. Test that all cells run in order
4. Add to appropriate module folder
5. Update this README
6. Submit pull request

## Questions?

- Check Jupyter documentation: https://jupyter.org/documentation
- Ask in course forum
- Open an issue on GitHub

---

**Happy Coding! Remember: The best way to learn is by doing! 💻🚀**
