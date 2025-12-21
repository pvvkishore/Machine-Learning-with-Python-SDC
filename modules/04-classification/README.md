# Module 4: Supervised Learning - Classification

## Overview

This module covers classification algorithms, one of the most important types of supervised learning. You'll learn to build models that predict categorical outcomes and understand when to use each algorithm.

## Learning Objectives

By the end of this module, you will be able to:

- Implement various classification algorithms
- Understand the mathematics behind each algorithm
- Choose the right algorithm for a given problem
- Evaluate classification models using appropriate metrics
- Handle imbalanced datasets
- Apply ensemble learning techniques

## Topics Covered

### Week 7: Core Classification Algorithms

#### 1. Logistic Regression
- Sigmoid function and probability
- Binary classification
- Multiclass classification (One-vs-Rest, Softmax)
- Cost function and gradient descent
- Regularization (L1 and L2)

#### 2. K-Nearest Neighbors (KNN)
- Distance metrics (Euclidean, Manhattan, Minkowski)
- Choosing optimal K
- Weighted KNN
- Computational complexity
- Curse of dimensionality

#### 3. Decision Trees
- Tree construction algorithms (ID3, C4.5, CART)
- Splitting criteria:
  - Information Gain
  - Gini Impurity
  - Gain Ratio
- Pruning techniques (pre-pruning and post-pruning)
- Handling continuous and categorical features
- Feature importance

### Week 8: Advanced Algorithms

#### 4. Support Vector Machines (SVM)
- Maximum margin classifier
- Support vectors concept
- Kernel trick:
  - Linear kernel
  - Polynomial kernel
  - RBF (Radial Basis Function) kernel
  - Sigmoid kernel
- Soft margin classification
- Multi-class SVM

#### 5. Naive Bayes
- Bayes theorem
- Conditional independence assumption
- Types:
  - Gaussian Naive Bayes
  - Multinomial Naive Bayes
  - Bernoulli Naive Bayes
- Applications in text classification

### Week 9: Ensemble Methods

#### 6. Ensemble Learning
- Wisdom of crowds
- Voting classifiers (hard and soft)
- Bagging (Bootstrap Aggregating)
- **Random Forest**:
  - How it works
  - Feature randomness
  - Out-of-bag evaluation
  - Hyperparameter tuning
- Boosting algorithms:
  - **AdaBoost** (Adaptive Boosting)
  - **Gradient Boosting**
  - **XGBoost** (Extreme Gradient Boosting)
  - **LightGBM**
  - **CatBoost**
- Stacking

### 7. Evaluation Metrics

- **Basic Metrics**:
  - Accuracy
  - Precision
  - Recall (Sensitivity)
  - F1-Score
  - Specificity
- **Advanced Metrics**:
  - Confusion Matrix
  - Classification Report
  - ROC Curve
  - AUC (Area Under Curve)
  - Precision-Recall Curve
  - Matthews Correlation Coefficient
- **Multi-class Metrics**:
  - Macro average
  - Micro average
  - Weighted average

### 8. Handling Imbalanced Data

- Understanding class imbalance
- Techniques:
  - Resampling (oversampling, undersampling)
  - SMOTE (Synthetic Minority Over-sampling)
  - Class weights
  - Ensemble methods for imbalanced data
- Evaluation strategies for imbalanced datasets

## Prerequisites

- Completion of Modules 1-3
- Understanding of linear algebra basics
- Probability and statistics fundamentals

## Materials

### Code Examples
- `logistic_regression.py` - Logistic regression implementation
- `knn_classifier.py` - KNN from scratch
- `decision_tree_example.py` - Decision tree visualization
- `svm_demonstration.py` - SVM with different kernels
- `ensemble_methods.py` - Random Forest and boosting
- `evaluation_metrics.py` - All classification metrics

### Notebooks
- `01_logistic_regression.ipynb` - Binary and multiclass classification
- `02_knn_algorithm.ipynb` - KNN implementation and tuning
- `03_decision_trees.ipynb` - Tree construction and visualization
- `04_svm_kernel_methods.ipynb` - SVM with various kernels
- `05_naive_bayes.ipynb` - Text classification example
- `06_random_forest.ipynb` - Forest building and tuning
- `07_boosting_algorithms.ipynb` - AdaBoost, XGBoost comparison
- `08_evaluation_metrics.ipynb` - Comprehensive metrics guide
- `09_imbalanced_data.ipynb` - Handling class imbalance

### Datasets
- Iris dataset (multiclass)
- Breast cancer dataset (binary)
- Wine quality dataset
- Credit card fraud detection (imbalanced)
- SMS spam collection (text classification)

## Assignments

### Assignment 4: Binary Classification Project
**Due**: End of Week 8  
**Weight**: Part of 30% assignments grade

**Project**: Medical Diagnosis Prediction

**Tasks**:
1. Load and explore medical diagnosis dataset
2. Preprocess data (handling missing values, encoding)
3. Implement at least 3 different classification algorithms
4. Compare model performance using appropriate metrics
5. Visualize results with confusion matrix and ROC curves
6. Write a report explaining your findings

**Deliverables**:
- Jupyter notebook with complete analysis
- PDF report (2-3 pages)
- Trained model files

### Assignment 5: Ensemble Methods Challenge
**Due**: End of Week 9  
**Weight**: Part of 30% assignments grade

**Project**: Multiclass Classification with Ensemble Learning

**Tasks**:
1. Work with a multiclass dataset
2. Build baseline models (logistic regression, decision tree)
3. Implement Random Forest with hyperparameter tuning
4. Implement at least one boosting algorithm (XGBoost/LightGBM)
5. Compare all models comprehensively
6. Handle class imbalance if present
7. Feature importance analysis

**Bonus**: Implement voting ensemble combining best models

### Mid-term Project
**Due**: End of Week 9  
**Weight**: 20% of total grade

**Project**: Complete Classification Pipeline

Build an end-to-end classification system including:
- Data preprocessing pipeline
- Feature engineering
- Model selection and training
- Hyperparameter optimization
- Model evaluation and comparison
- Documentation and presentation

See `midterm_project_guidelines.md` for detailed requirements.

### Quiz 3: Classification Algorithms
**Date**: Week 9  
**Format**: Multiple choice, short answer, and coding problems  
**Duration**: 45 minutes  
**Coverage**: All classification algorithms and evaluation metrics

## Key Concepts to Master

- [ ] Logistic regression mathematics and implementation
- [ ] KNN algorithm and choosing K
- [ ] Decision tree construction and pruning
- [ ] SVM and kernel methods
- [ ] Naive Bayes assumptions and applications
- [ ] Random Forest and bagging
- [ ] Boosting algorithms (AdaBoost, Gradient Boosting)
- [ ] All evaluation metrics and when to use each
- [ ] Handling imbalanced datasets
- [ ] Feature importance interpretation

## Practical Skills

### By the end of this module, you should be able to:

1. **Algorithm Selection**
   - Choose appropriate algorithm based on problem characteristics
   - Consider interpretability vs performance tradeoffs

2. **Implementation**
   - Implement algorithms using Scikit-learn
   - Understand hyperparameters for each algorithm
   - Build custom preprocessing pipelines

3. **Evaluation**
   - Select appropriate metrics for your problem
   - Interpret confusion matrices
   - Generate and analyze ROC curves
   - Compare multiple models fairly

4. **Optimization**
   - Tune hyperparameters systematically
   - Use cross-validation properly
   - Prevent overfitting

5. **Production Readiness**
   - Save and load trained models
   - Create reproducible pipelines
   - Handle edge cases

## Algorithm Comparison Guide

| Algorithm | Pros | Cons | Best For |
|-----------|------|------|----------|
| Logistic Regression | Fast, interpretable, probabilistic | Linear decision boundary | Baseline, interpretable models |
| KNN | Simple, no training, non-parametric | Slow prediction, memory intensive | Small datasets, non-linear |
| Decision Tree | Interpretable, handles non-linear | Overfitting, unstable | Feature importance, rules |
| SVM | Effective in high dimensions | Slow, hard to interpret | Small to medium datasets |
| Naive Bayes | Fast, works well with text | Strong independence assumption | Text classification, real-time |
| Random Forest | Robust, handles overfitting | Less interpretable, memory | General purpose, best performance |
| XGBoost/LightGBM | State-of-art performance | Computationally expensive | Competitions, best accuracy |

## Common Pitfalls

1. **Using accuracy for imbalanced datasets**
   - Solution: Use F1-score, precision-recall, or AUC

2. **Not scaling features for KNN/SVM**
   - Solution: Always standardize features

3. **Overfitting decision trees**
   - Solution: Limit depth, min samples, pruning

4. **Not tuning hyperparameters**
   - Solution: Use GridSearchCV or RandomizedSearchCV

5. **Training on full data without validation**
   - Solution: Always use train-test split and cross-validation

6. **Ignoring class imbalance**
   - Solution: Use class weights or resampling

## Tips for Success

1. **Start Simple**: Begin with logistic regression, then try complex models
2. **Understand Metrics**: Know which metric matters for your problem
3. **Visualize**: Plot decision boundaries when possible
4. **Feature Engineering**: Often more important than algorithm choice
5. **Cross-Validate**: Always use CV for reliable performance estimates
6. **Document**: Keep notes on what works and what doesn't
7. **Experiment**: Try different algorithms and compare

## Recommended Readings

### Required
- "Hands-On ML" Chapter 3 (Classification)
- Scikit-learn Classification documentation
- XGBoost documentation and tutorials

### Optional
- "The Elements of Statistical Learning" (Chapters 4, 9, 10, 15)
- Research papers on ensemble methods
- Kaggle competition winning solutions

## Online Resources

- [Scikit-learn Classification Guide](https://scikit-learn.org/stable/supervised_learning.html)
- [StatQuest YouTube - Classification Algorithms](https://www.youtube.com/c/joshstarmer)
- [Kaggle Learn - Intermediate ML](https://www.kaggle.com/learn/intermediate-machine-learning)
- [Google's Classification Course](https://developers.google.com/machine-learning/crash-course/classification)

## Week-by-Week Guide

### Week 7: Foundation
- Mon-Tue: Logistic Regression theory and practice
- Wed-Thu: KNN implementation and optimization
- Fri: Start Assignment 4

### Week 8: Advanced Algorithms
- Mon-Tue: Decision Trees and visualization
- Wed-Thu: SVM and kernel methods
- Fri: Complete Assignment 4, start Assignment 5

### Week 9: Ensemble & Evaluation
- Mon-Tue: Random Forest and bagging
- Wed: Boosting algorithms (XGBoost)
- Thu: Evaluation metrics deep dive
- Fri: Complete Assignment 5 and mid-term project

## Lab Exercises

1. **Lab 7.1**: Implement logistic regression from scratch
2. **Lab 7.2**: KNN with custom distance metric
3. **Lab 8.1**: Visualize decision tree boundaries
4. **Lab 8.2**: SVM kernel comparison
5. **Lab 9.1**: Build Random Forest manually
6. **Lab 9.2**: Compare all ensemble methods

## Project Ideas for Practice

- Credit card fraud detection
- Customer churn prediction
- Email spam classification
- Disease diagnosis from symptoms
- Product recommendation (classification version)
- Sentiment analysis
- Image classification (digits, animals)

## Next Steps

After completing this module:
1. Review mid-term project feedback
2. Compare your solutions with sample solutions
3. Practice with Kaggle classification competitions
4. Preview Module 5: Unsupervised Learning

**Ready to move on?** Ensure you can:
- ✓ Implement and explain major classification algorithms
- ✓ Choose appropriate evaluation metrics
- ✓ Handle imbalanced datasets
- ✓ Use ensemble methods effectively
- ✓ Complete mid-term project successfully

---

**Congratulations on mastering classification! This is a major milestone in your ML journey! 🎉**
