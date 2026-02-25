# Quick Start Guide

This guide will help you get started with the Machine Learning with Python course materials.

## For Students

### 1. Clone the Repository

```bash
git clone https://github.com/pvvkishore/Machine-Learning-with-Python-SDC.git
cd Machine-Learning-with-Python-SDC
```

### 2. Set Up Your Environment

Install Python 3.8 or higher, then install dependencies:

```bash
pip install -r requirements.txt
```

Or use conda:

```bash
conda create -n ml-course python=3.10
conda activate ml-course
pip install -r requirements.txt
```

### 3. Launch Jupyter Notebook

```bash
jupyter notebook
```

### 4. Navigate to Course Materials

- Start with `01-Introduction/01-course-overview.ipynb`
- Follow the numbered sequence within each module
- Complete exercises and practice problems

### 5. View Notebook Descriptions

Check [NOTEBOOKS.md](NOTEBOOKS.md) for a complete list and description of all notebooks.

## For Instructors

### Adding New Notebooks

1. **Create or place notebook in appropriate module**
   ```bash
   # Example: Adding to module 02
   cp my-notebook.ipynb 02-Data-Preprocessing/03-feature-scaling.ipynb
   ```

2. **Follow naming conventions**
   - Use two-digit numbering: `01-`, `02-`, `03-`, etc.
   - Use lowercase with hyphens: `feature-scaling`, `data-cleaning`

3. **Structure your notebook properly**
   - Start with H1 title
   - Add overview/description in first markdown cell
   - Use H2 for main sections
   - Include code comments

4. **Generate descriptions**
   ```bash
   python notebook_analyzer.py . -o NOTEBOOKS.md
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: [module] - [topic]"
   git push
   ```

### Creating a New Module

1. **Create module directory**
   ```bash
   mkdir 05-Deep-Learning
   ```

2. **Copy template README**
   ```bash
   cp MODULE_README_TEMPLATE.md 05-Deep-Learning/README.md
   ```

3. **Customize the README**
   - Update module number and name
   - Add learning objectives
   - List planned notebooks
   - Add key concepts

4. **Add notebooks**
   - Follow naming conventions
   - Number sequentially: 01-, 02-, 03-

### Automatic Updates with GitHub Actions

The repository includes a GitHub Actions workflow that automatically:
- Detects when `.ipynb` files are added or modified
- Runs the notebook analyzer
- Updates NOTEBOOKS.md
- Commits the changes

To trigger manually:
1. Go to Actions tab on GitHub
2. Select "Update Notebook Descriptions"
3. Click "Run workflow"

## Using the Notebook Analyzer

### Analyze a Single Notebook

```bash
python notebook_analyzer.py path/to/notebook.ipynb
```

Output will be printed to console.

### Analyze All Notebooks

```bash
python notebook_analyzer.py .
```

This creates/updates `NOTEBOOKS.md` with descriptions of all notebooks.

### Specify Custom Output File

```bash
python notebook_analyzer.py . -o MY_NOTEBOOKS.md
```

### Analyze Specific Directory

```bash
python notebook_analyzer.py 01-Introduction/
```

## Best Practices

### For Notebooks
1. **Clear and descriptive titles** - Use H1 for main title
2. **Structured content** - Use H2 and H3 for sections
3. **Explanatory text** - Don't rely only on code comments
4. **Working code** - Test all cells before committing
5. **Reasonable output** - Clear large outputs if not essential

### For Module Organization
1. **Logical progression** - Order from simple to complex
2. **Self-contained** - Each notebook should be complete
3. **Cross-references** - Link to previous/next notebooks
4. **Prerequisites** - State clearly in module README

### For Collaboration
1. **Descriptive commits** - Use clear commit messages
2. **Regular updates** - Keep NOTEBOOKS.md current
3. **Documentation** - Update READMEs when adding content
4. **Review changes** - Check diffs before committing

## Troubleshooting

### Notebook Analyzer Not Working

**Problem**: `ModuleNotFoundError` when running analyzer

**Solution**: The analyzer uses only Python standard library, no external dependencies needed. Check Python version (3.7+).

### GitHub Actions Not Running

**Problem**: NOTEBOOKS.md not updated after pushing

**Solution**: 
1. Check `.github/workflows/update-notebook-descriptions.yml` exists
2. Verify GitHub Actions are enabled in repository settings
3. Check Actions tab for error messages

### Jupyter Kernel Issues

**Problem**: Kernel keeps dying or not starting

**Solution**:
```bash
pip install --upgrade jupyter notebook ipykernel
python -m ipykernel install --user
```

### Git Issues with Large Notebooks

**Problem**: Notebooks with large outputs causing push issues

**Solution**:
1. Clear outputs: Cell → All Output → Clear
2. Or use nbstripout: `pip install nbstripout`

## Getting Help

- **Course Issues**: Open an issue on GitHub
- **Technical Problems**: Check [ORGANIZATION_GUIDE.md](ORGANIZATION_GUIDE.md)
- **Suggestions**: Submit a pull request
- **Questions**: Contact the instructor

## Additional Resources

- [ORGANIZATION_GUIDE.md](ORGANIZATION_GUIDE.md) - Detailed organization guidelines
- [NOTEBOOKS.md](NOTEBOOKS.md) - Auto-generated notebook descriptions
- [MODULE_README_TEMPLATE.md](MODULE_README_TEMPLATE.md) - Template for module READMEs
- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)
- [Python Documentation](https://docs.python.org/)

---

**Happy Learning! 📚🚀**
