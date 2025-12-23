# Course Organization Guide

This document explains how to organize and structure course materials in this repository following benchmark course standards.

## Directory Structure

Course materials should be organized in numbered modules following this structure:

```
Machine-Learning-with-Python-SDC/
│
├── 01-Introduction/
│   ├── README.md
│   ├── 01-course-overview.ipynb
│   ├── 02-python-basics.ipynb
│   └── resources/
│
├── 02-Data-Preprocessing/
│   ├── README.md
│   ├── 01-data-loading.ipynb
│   ├── 02-data-cleaning.ipynb
│   ├── 03-feature-engineering.ipynb
│   └── datasets/
│
├── 03-Supervised-Learning/
│   ├── README.md
│   ├── 01-linear-regression.ipynb
│   ├── 02-logistic-regression.ipynb
│   └── exercises/
│
└── [Additional modules...]
```

## Naming Conventions

### Module Directories
- Use two-digit numbering: `01-`, `02-`, `03-`, etc.
- Use Title Case with hyphens: `01-Introduction`, `02-Data-Preprocessing`
- Order modules logically from foundational to advanced topics

### Notebook Files
- Use two-digit numbering within each module: `01-`, `02-`, `03-`, etc.
- Use lowercase with hyphens: `01-course-overview.ipynb`, `02-linear-regression.ipynb`
- Names should be descriptive but concise

## Standard Module Structure

Each module directory should contain:

1. **README.md** - Module overview and learning objectives
2. **Numbered notebooks** - Lessons in sequential order
3. **resources/** (optional) - Additional materials, images, references
4. **datasets/** (optional) - Data files used in the module
5. **exercises/** (optional) - Practice problems and solutions

## Notebook Structure

Each notebook should follow this structure:

### 1. Title Cell (Markdown)
```markdown
# Lesson Title
```

### 2. Overview Cell (Markdown)
```markdown
## Overview
Brief description of what this notebook covers and learning objectives.
```

### 3. Main Content
- Use H2 (`##`) for main sections
- Use H3 (`###`) for subsections
- Include code cells with clear comments
- Add markdown cells for explanations

### 4. Summary Cell (Optional)
```markdown
## Summary
Key takeaways from this lesson.
```

### 5. Exercises Cell (Optional)
```markdown
## Exercises
Practice problems for students.
```

## Automatic Description Generation

This repository includes a `notebook_analyzer.py` tool that automatically generates descriptions for notebooks.

### Usage

Analyze a single notebook:
```bash
python notebook_analyzer.py path/to/notebook.ipynb
```

Analyze all notebooks in the repository:
```bash
python notebook_analyzer.py . -o NOTEBOOKS.md
```

This will create a `NOTEBOOKS.md` file with descriptions of all notebooks.

## Recommended Module Sequence

For a Machine Learning course, consider this sequence:

1. **01-Introduction** - Course overview, Python basics, Jupyter notebooks
2. **02-Data-Preprocessing** - Loading, cleaning, and preparing data
3. **03-Exploratory-Data-Analysis** - Visualization and statistical analysis
4. **04-Supervised-Learning** - Regression and classification algorithms
5. **05-Unsupervised-Learning** - Clustering, dimensionality reduction
6. **06-Model-Evaluation** - Metrics, cross-validation, hyperparameter tuning
7. **07-Deep-Learning** - Neural networks, TensorFlow/PyTorch basics
8. **08-Advanced-Topics** - Ensemble methods, time series, NLP
9. **09-Projects** - End-to-end machine learning projects
10. **10-Resources** - Additional materials, references, datasets

## Workflow for Adding New Notebooks

1. **Create or place notebook in appropriate module directory**
   - Follow naming conventions
   - Ensure proper numbering

2. **Structure notebook content**
   - Add clear title and overview
   - Use consistent heading hierarchy
   - Include explanations and code comments

3. **Generate description**
   ```bash
   python notebook_analyzer.py .
   ```

4. **Commit and push**
   ```bash
   git add .
   git commit -m "Add: [module-name] - [notebook-topic]"
   git push
   ```

## Best Practices

### For Notebooks
- Keep notebooks focused on a single topic
- Use meaningful variable names
- Include sufficient markdown explanations
- Test all code cells before committing
- Clear output cells if they're very large

### For Documentation
- Update module READMEs when adding notebooks
- Keep the main README.md updated with course structure
- Use the notebook analyzer to maintain NOTEBOOKS.md

### For Code Quality
- Follow PEP 8 style guidelines for Python code
- Add comments for complex code sections
- Include error handling examples where appropriate

## GitHub Actions Integration (Optional)

You can automate description generation with GitHub Actions:

Create `.github/workflows/update-descriptions.yml`:

```yaml
name: Update Notebook Descriptions

on:
  push:
    paths:
      - '**.ipynb'

jobs:
  update-descriptions:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - name: Generate descriptions
        run: python notebook_analyzer.py . -o NOTEBOOKS.md
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add NOTEBOOKS.md
          git diff --quiet && git diff --staged --quiet || git commit -m "Auto-update notebook descriptions"
          git push
```

This will automatically update notebook descriptions whenever `.ipynb` files are modified.

## Questions or Suggestions?

If you have suggestions for improving this organization system, please open an issue or submit a pull request.
