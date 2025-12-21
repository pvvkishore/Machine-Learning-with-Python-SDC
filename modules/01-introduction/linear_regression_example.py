"""
Example: Simple Linear Regression
==================================

This script demonstrates a complete machine learning workflow:
1. Generate synthetic data
2. Split into train/test sets
3. Train a linear regression model
4. Evaluate and visualize results

Author: ML Course Team
Date: December 2024
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def generate_data(n_samples=100, noise=10, random_state=42):
    """
    Generate synthetic data for linear regression.
    
    Parameters:
    -----------
    n_samples : int
        Number of samples to generate
    noise : float
        Standard deviation of Gaussian noise
    random_state : int
        Random seed for reproducibility
    
    Returns:
    --------
    X : ndarray, shape (n_samples, 1)
        Feature matrix
    y : ndarray, shape (n_samples,)
        Target values
    """
    np.random.seed(random_state)
    X = np.random.rand(n_samples, 1) * 100
    y = 2.5 * X.ravel() + 10 + np.random.randn(n_samples) * noise
    return X, y


def train_model(X_train, y_train):
    """
    Train a linear regression model.
    
    Parameters:
    -----------
    X_train : ndarray
        Training features
    y_train : ndarray
        Training targets
    
    Returns:
    --------
    model : LinearRegression
        Trained model
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """
    Evaluate model performance.
    
    Parameters:
    -----------
    model : LinearRegression
        Trained model
    X_test : ndarray
        Test features
    y_test : ndarray
        Test targets
    
    Returns:
    --------
    metrics : dict
        Dictionary containing evaluation metrics
    """
    y_pred = model.predict(X_test)
    
    metrics = {
        'mse': mean_squared_error(y_test, y_pred),
        'rmse': np.sqrt(mean_squared_error(y_test, y_pred)),
        'r2': r2_score(y_test, y_pred)
    }
    
    return metrics, y_pred


def plot_results(X_test, y_test, y_pred):
    """
    Visualize actual vs predicted values.
    
    Parameters:
    -----------
    X_test : ndarray
        Test features
    y_test : ndarray
        Actual test targets
    y_pred : ndarray
        Predicted values
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(X_test, y_test, color='blue', alpha=0.5, label='Actual')
    plt.scatter(X_test, y_pred, color='red', alpha=0.5, label='Predicted')
    plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
    plt.xlabel('Feature (X)')
    plt.ylabel('Target (y)')
    plt.title('Linear Regression: Actual vs Predicted')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('linear_regression_results.png', dpi=150)
    print("Plot saved as 'linear_regression_results.png'")
    plt.show()


def main():
    """
    Main function to run the complete workflow.
    """
    print("=" * 50)
    print("Linear Regression Example")
    print("=" * 50)
    
    # 1. Generate data
    print("\n1. Generating data...")
    X, y = generate_data(n_samples=200, noise=15)
    print(f"   Generated {len(X)} samples")
    
    # 2. Split data
    print("\n2. Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"   Training samples: {len(X_train)}")
    print(f"   Testing samples: {len(X_test)}")
    
    # 3. Train model
    print("\n3. Training model...")
    model = train_model(X_train, y_train)
    print(f"   Coefficient: {model.coef_[0]:.4f}")
    print(f"   Intercept: {model.intercept_:.4f}")
    
    # 4. Evaluate model
    print("\n4. Evaluating model...")
    metrics, y_pred = evaluate_model(model, X_test, y_test)
    print(f"   Mean Squared Error: {metrics['mse']:.4f}")
    print(f"   Root Mean Squared Error: {metrics['rmse']:.4f}")
    print(f"   R² Score: {metrics['r2']:.4f}")
    
    # 5. Visualize results
    print("\n5. Creating visualization...")
    plot_results(X_test, y_test, y_pred)
    
    print("\n" + "=" * 50)
    print("Analysis complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
