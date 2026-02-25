# Datasets

This directory contains sample datasets used throughout the course for practice and assignments.

## Available Datasets

### Beginner Level

#### 1. Iris Dataset
- **File**: `iris.csv`
- **Description**: Classic dataset for classification
- **Features**: 4 (sepal/petal length and width)
- **Classes**: 3 (Setosa, Versicolor, Virginica)
- **Samples**: 150
- **Use**: Introduction to classification

#### 2. Boston Housing
- **File**: `boston_housing.csv`
- **Description**: Housing price prediction
- **Features**: 13 (crime rate, rooms, etc.)
- **Target**: Median home value
- **Samples**: 506
- **Use**: Regression practice

#### 3. Wine Quality
- **File**: `wine_quality.csv`
- **Description**: Wine quality assessment
- **Features**: 11 physicochemical properties
- **Target**: Quality score (0-10)
- **Samples**: 1599
- **Use**: Classification/Regression

### Intermediate Level

#### 4. Titanic Survival
- **File**: `titanic.csv`
- **Description**: Passenger survival prediction
- **Features**: Age, class, gender, fare, etc.
- **Target**: Survived (binary)
- **Samples**: 891
- **Use**: Binary classification, handling missing data

#### 5. Credit Card Fraud
- **File**: `credit_card_fraud.csv`
- **Description**: Fraud detection
- **Features**: 30 (anonymized)
- **Target**: Fraud (binary)
- **Samples**: 284,807 (highly imbalanced)
- **Use**: Imbalanced classification

#### 6. Mall Customers
- **File**: `mall_customers.csv`
- **Description**: Customer segmentation
- **Features**: Age, income, spending score
- **Samples**: 200
- **Use**: Clustering, customer segmentation

### Advanced Level

#### 7. SMS Spam Collection
- **File**: `sms_spam.csv`
- **Description**: SMS spam detection
- **Features**: Text messages
- **Classes**: Spam/Ham
- **Samples**: 5,574
- **Use**: Text classification, NLP

#### 8. Fashion MNIST
- **File**: Available via TensorFlow datasets
- **Description**: Clothing images
- **Features**: 28x28 grayscale images
- **Classes**: 10 (T-shirt, Trouser, etc.)
- **Samples**: 70,000
- **Use**: Image classification with CNNs

## Dataset Sources

All datasets are publicly available and used for educational purposes:

- **UCI ML Repository**: https://archive.ics.uci.edu/ml/
- **Kaggle Datasets**: https://www.kaggle.com/datasets
- **Scikit-learn**: Built-in datasets
- **TensorFlow Datasets**: https://www.tensorflow.org/datasets

## Loading Datasets

### Using Pandas
```python
import pandas as pd

# Load CSV file
df = pd.read_csv('datasets/iris.csv')
print(df.head())
```

### Using Scikit-learn Built-in Datasets
```python
from sklearn.datasets import load_iris, load_boston

# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Load boston dataset
boston = load_boston()
X, y = boston.data, boston.target
```

### Using TensorFlow Datasets
```python
import tensorflow_datasets as tfds

# Load Fashion MNIST
dataset, info = tfds.load('fashion_mnist', with_info=True)
train_dataset = dataset['train']
```

## Dataset Information Files

Each dataset includes a companion `_info.md` file with:
- Detailed description
- Feature explanations
- Data dictionary
- Known issues or biases
- Suggested preprocessing steps
- Example use cases
- Related research papers

Example: `iris_info.md`, `titanic_info.md`

## Adding Your Own Datasets

When adding datasets:

1. **Check License**: Ensure data can be used for education
2. **Create Info File**: Document data source and features
3. **Keep Size Reasonable**: <50MB preferred
4. **Clean Format**: CSV or standard format
5. **Add to README**: Update this file

## Data Ethics and Privacy

- All datasets are publicly available
- No personally identifiable information (PII)
- Datasets used only for educational purposes
- Respect data licenses and citations
- Be aware of potential biases in data

## Downloading Large Datasets

Some datasets are too large for the repository. Download instructions:

```bash
# Create data directory if needed
mkdir -p datasets

# Download from Kaggle (requires kaggle CLI)
kaggle datasets download -d dataset-name -p datasets/

# Download from URL
wget https://example.com/dataset.csv -P datasets/
```

## Data Preprocessing Scripts

Common preprocessing scripts available in `preprocessing/`:
- `load_data.py` - Standard data loading functions
- `clean_data.py` - Common cleaning operations
- `split_data.py` - Train-test splitting utilities

## Best Practices

1. **Never Modify Original Data**: Always work on copies
2. **Document Changes**: Keep track of preprocessing steps
3. **Version Control**: Use Git for data versions when possible
4. **Reproducibility**: Save preprocessing scripts
5. **Validation**: Always validate data after loading

## Common Issues

### Missing Values
- Check for NaN, None, empty strings
- Decide on imputation strategy
- Document handling approach

### Data Types
- Verify numeric vs categorical
- Convert types as needed
- Watch for mixed types

### Duplicates
- Check for duplicate rows
- Decide on deduplication strategy

### Outliers
- Visualize data distributions
- Identify legitimate vs error outliers
- Document outlier handling

## Need More Data?

### Free Dataset Resources
- **Kaggle**: Thousands of datasets
- **Google Dataset Search**: https://datasetsearch.research.google.com/
- **AWS Open Data**: https://registry.opendata.aws/
- **Data.gov**: US government datasets
- **UCI Repository**: Classic ML datasets
- **HuggingFace Datasets**: NLP and more

### Creating Synthetic Data
```python
from sklearn.datasets import make_classification, make_regression

# Create synthetic classification data
X, y = make_classification(n_samples=1000, n_features=20)

# Create synthetic regression data
X, y = make_regression(n_samples=1000, n_features=10)
```

## Questions?

For dataset-related questions:
- Check the dataset's info file
- Review module notebooks using the dataset
- Ask in course discussion forum
- Open an issue on GitHub

---

**Remember**: Good data is the foundation of good models! 📊
