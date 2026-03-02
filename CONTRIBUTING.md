# Contributing to Machine Learning with Python SDC

Thank you for your interest in contributing to this educational repository! We welcome contributions from students, educators, and the broader community. This guide will help you get started.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How Can I Contribute?](#how-can-i-contribute)
3. [Getting Started](#getting-started)
4. [Contribution Guidelines](#contribution-guidelines)
5. [Style Guide](#style-guide)
6. [Submitting Changes](#submitting-changes)
7. [Review Process](#review-process)

## Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

## How Can I Contribute?

### 🐛 Reporting Bugs

If you find a bug in the code or documentation:

1. Check if the bug has already been reported in [Issues](../../issues)
2. If not, create a new issue with:
   - Clear, descriptive title
   - Steps to reproduce the problem
   - Expected vs actual behavior
   - Screenshots (if applicable)
   - Your environment (OS, Python version, etc.)

**Example:**
```
Title: TypeError in linear regression example

Description:
When running the linear_regression.py example in Module 3, 
I get a TypeError on line 45.

Steps to reproduce:
1. Navigate to modules/03-regression/
2. Run: python linear_regression.py
3. Error occurs at model.fit() call

Environment:
- OS: Windows 10
- Python: 3.9.7
- NumPy: 1.21.0
```

### 📝 Improving Documentation

Documentation improvements are always welcome:

- Fix typos or grammatical errors
- Clarify confusing explanations
- Add missing documentation
- Improve code comments
- Create or enhance examples

### ✨ Adding New Features

Before adding new features:

1. Open an issue to discuss your idea
2. Wait for feedback from maintainers
3. Fork the repository
4. Implement your feature
5. Submit a pull request

### 📚 Adding Learning Resources

You can contribute by:

- Adding new example notebooks
- Creating practice exercises
- Adding datasets with proper documentation
- Contributing explanatory articles
- Creating visualization examples

### 🎓 Sharing Your Projects

Completed an interesting project using course materials? Share it!

1. Create a folder in `modules/08-projects/student-projects/`
2. Include:
   - Your code
   - README explaining the project
   - Requirements/dependencies
   - Results/visualizations
   - Your name and contact (optional)

## Getting Started

### Fork and Clone

1. **Fork** this repository to your GitHub account
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Machine-Learning-with-Python-SDC.git
   cd Machine-Learning-with-Python-SDC
   ```

3. **Add upstream** remote:
   ```bash
   git remote add upstream https://github.com/pvvkishore/Machine-Learning-with-Python-SDC.git
   ```

### Create a Branch

Always create a new branch for your changes:

```bash
git checkout -b feature/your-feature-name
```

Branch naming conventions:
- `feature/` - for new features
- `fix/` - for bug fixes
- `docs/` - for documentation changes
- `example/` - for new examples

Examples:
- `feature/add-neural-network-example`
- `fix/regression-notebook-error`
- `docs/improve-installation-guide`

### Make Your Changes

1. Set up your development environment (see [GETTING_STARTED.md](GETTING_STARTED.md))
2. Make your changes
3. Test your changes thoroughly
4. Update documentation if needed

## Contribution Guidelines

### Code Quality

- **Follow PEP 8**: Use Python's style guide
- **Add Comments**: Explain complex logic
- **Write Docstrings**: Document functions and classes
- **Keep it Simple**: Prioritize readability
- **Avoid Duplication**: Reuse existing code

Example:
```python
def calculate_accuracy(y_true, y_pred):
    """
    Calculate classification accuracy.
    
    Parameters:
    -----------
    y_true : array-like
        True labels
    y_pred : array-like
        Predicted labels
    
    Returns:
    --------
    float
        Accuracy score between 0 and 1
    
    Examples:
    ---------
    >>> y_true = [0, 1, 1, 0]
    >>> y_pred = [0, 1, 0, 0]
    >>> calculate_accuracy(y_true, y_pred)
    0.75
    """
    return sum(y_t == y_p for y_t, y_p in zip(y_true, y_pred)) / len(y_true)
```

### Jupyter Notebooks

When contributing notebooks:

1. **Clear Outputs**: Clear all outputs before committing
   - In Jupyter: Cell → All Output → Clear
2. **Add Markdown Cells**: Explain each section
3. **Include Visualizations**: Add plots where helpful
4. **Provide Examples**: Show expected output
5. **Add References**: Cite sources when applicable

### Documentation

- Use clear, concise language
- Include code examples
- Add screenshots for UI-related changes
- Check spelling and grammar
- Update table of contents if needed

### Datasets

When adding datasets:

- Ensure proper licensing
- Document data source and description
- Include data dictionary
- Keep file sizes reasonable (<10MB)
- Add preprocessing scripts if needed

## Style Guide

### Python Code

```python
# Good
def train_model(X_train, y_train, learning_rate=0.01):
    """Train a machine learning model."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Bad
def f(x,y,lr=0.01):
    m=LinearRegression()
    m.fit(x,y)
    return m
```

### Markdown

```markdown
# Use proper heading hierarchy

## Second level
### Third level

- Use bullet points for lists
- Keep lines under 100 characters
- Add blank lines between sections

Use `code blocks` for code snippets

```python
# Code example
print("Hello, World!")
```
```

## Submitting Changes

### Before Submitting

1. **Test Your Code**: Ensure everything works
2. **Run Linters**: Check code quality
   ```bash
   pip install flake8
   flake8 your_file.py
   ```
3. **Update Documentation**: Reflect your changes
4. **Check Notebook Outputs**: Clear all cell outputs
5. **Commit Messages**: Write clear commit messages

### Commit Message Format

```
type: brief description

Detailed explanation of what changed and why.

Fixes #issue_number (if applicable)
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

Examples:
```
feat: add logistic regression example notebook

Added a comprehensive notebook demonstrating logistic regression
with the iris dataset. Includes data preprocessing, model training,
evaluation, and visualization.

docs: fix typo in README installation section

Fixed incorrect command in the pip install instructions.

Fixes #42
```

### Create a Pull Request

1. **Push to Your Fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open Pull Request** on GitHub:
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill in the template

3. **PR Description Should Include**:
   - What changed
   - Why the change was made
   - How to test it
   - Screenshots (if applicable)
   - Related issues

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## How to Test
Steps to test your changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] Notebook outputs cleared
```

## Review Process

### What to Expect

1. **Initial Review**: Within 3-5 days
2. **Feedback**: Reviewers may request changes
3. **Iteration**: Make requested changes
4. **Approval**: Once approved, your PR will be merged

### Review Criteria

- Code quality and readability
- Adherence to style guide
- Documentation completeness
- Test coverage
- Educational value

### Addressing Feedback

- Be open to suggestions
- Respond to comments
- Make requested changes promptly
- Ask questions if unclear
- Be respectful and professional

## Recognition

Contributors will be:
- Listed in the project's contributors
- Acknowledged in release notes
- Given credit in relevant documentation

## Questions?

- **General Questions**: Open a discussion in [Discussions](../../discussions)
- **Bug Reports**: Create an issue
- **Feature Requests**: Open an issue with "Feature Request" label
- **Security Issues**: Email the maintainers directly

## Resources

### Learning Git
- [GitHub Guides](https://guides.github.com/)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)

### Python Style
- [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

### Markdown
- [Markdown Guide](https://www.markdownguide.org/)

---

Thank you for contributing to Machine Learning education! 🎓

Your contributions help students worldwide learn and grow in their ML journey.
