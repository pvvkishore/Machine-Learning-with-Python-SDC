# Machine Learning with Python - Course Syllabus

## Course Information

**Course Title**: Machine Learning with Python - Skill Development Course  
**Institution**: KL Deemed to be University  
**Academic Year**: 2025-2026  
**Level**: Undergraduate/Graduate  
**Credits**: TBD  
**Prerequisites**: Basic Python programming, Mathematics (Algebra, Statistics)

## Course Description

This comprehensive course provides a solid foundation in Machine Learning using Python. Students will learn to design, implement, and evaluate machine learning models to solve real-world problems. The course combines theoretical understanding with extensive hands-on practice, covering supervised learning, unsupervised learning, and an introduction to deep learning.

## Learning Outcomes

Upon successful completion of this course, students will be able to:

1. Explain fundamental machine learning concepts, algorithms, and their applications
2. Preprocess and prepare data for machine learning tasks
3. Implement and evaluate supervised learning algorithms for classification and regression
4. Apply unsupervised learning techniques for clustering and dimensionality reduction
5. Select appropriate algorithms and evaluation metrics for specific problems
6. Optimize model performance through hyperparameter tuning and feature engineering
7. Develop end-to-end machine learning projects from problem definition to deployment
8. Write clean, efficient, and well-documented Python code for ML applications
9. Interpret and communicate machine learning results effectively
10. Apply ethical considerations in ML development and deployment

## Course Structure

### Duration
- **Total Weeks**: 16
- **Lecture Hours**: 3 hours per week
- **Lab Hours**: 2 hours per week
- **Self-Study**: 4-6 hours per week

---

## Detailed Module Breakdown

### Module 1: Introduction to Machine Learning (Week 1-2)

#### Topics Covered
- What is Machine Learning? History and evolution
- Types of Machine Learning:
  - Supervised Learning
  - Unsupervised Learning
  - Semi-supervised Learning
  - Reinforcement Learning
- Applications of ML in various domains
- ML workflow and development lifecycle
- Python ecosystem for ML:
  - NumPy for numerical computing
  - Pandas for data manipulation
  - Matplotlib and Seaborn for visualization

#### Learning Objectives
- Understand ML fundamentals and terminology
- Set up Python ML development environment
- Perform basic operations with NumPy and Pandas
- Create data visualizations with Matplotlib

#### Assignments
- Assignment 1: Python and NumPy basics exercises
- Quiz 1: ML concepts and Python libraries

#### Readings
- Chapter 1: Introduction to ML (recommended textbook)
- Python NumPy tutorial documentation

---

### Module 2: Data Preprocessing and Exploration (Week 3-4)

#### Topics Covered
- Data collection and loading (CSV, JSON, APIs)
- Exploratory Data Analysis (EDA):
  - Statistical summaries
  - Data visualization techniques
  - Identifying patterns and relationships
- Data cleaning:
  - Handling missing values
  - Removing duplicates
  - Dealing with outliers
- Feature engineering:
  - Creating new features
  - Feature transformation
  - Encoding categorical variables
- Feature scaling and normalization
- Train-test split and cross-validation

#### Learning Objectives
- Perform comprehensive EDA on datasets
- Clean and preprocess data effectively
- Engineer meaningful features
- Split data appropriately for model training

#### Assignments
- Assignment 2: Complete EDA on provided dataset
- Lab Exercise: Data preprocessing pipeline

#### Readings
- Data preprocessing best practices
- Feature engineering techniques article

---

### Module 3: Supervised Learning - Regression (Week 5-6)

#### Topics Covered
- Introduction to regression problems
- Simple Linear Regression:
  - Gradient descent
  - Cost function
  - Implementation from scratch
- Multiple Linear Regression
- Polynomial Regression
- Regularization techniques:
  - Ridge Regression (L2)
  - Lasso Regression (L1)
  - Elastic Net
- Evaluation metrics:
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)
  - Mean Absolute Error (MAE)
  - R-squared score

#### Learning Objectives
- Understand regression theory and mathematics
- Implement various regression algorithms
- Apply regularization to prevent overfitting
- Evaluate regression models appropriately

#### Assignments
- Assignment 3: Housing price prediction project
- Quiz 2: Regression concepts

#### Readings
- Linear regression mathematics
- Regularization techniques paper

---

### Module 4: Supervised Learning - Classification (Week 7-9)

#### Topics Covered
- Introduction to classification problems
- Logistic Regression:
  - Sigmoid function
  - Binary and multiclass classification
- K-Nearest Neighbors (KNN)
- Decision Trees:
  - Information gain
  - Gini impurity
  - Pruning techniques
- Support Vector Machines (SVM):
  - Linear SVM
  - Kernel trick
  - RBF kernel
- Naive Bayes classifier
- Ensemble methods:
  - Bagging
  - Random Forest
  - AdaBoost
  - Gradient Boosting (XGBoost, LightGBM)
- Evaluation metrics:
  - Accuracy, Precision, Recall, F1-score
  - Confusion matrix
  - ROC curve and AUC
  - Classification report

#### Learning Objectives
- Implement various classification algorithms
- Understand ensemble learning principles
- Select appropriate evaluation metrics
- Handle imbalanced datasets

#### Assignments
- Assignment 4: Binary classification project (medical diagnosis)
- Assignment 5: Multiclass classification with ensemble methods
- Quiz 3: Classification algorithms

#### Readings
- Decision trees and random forests
- Ensemble learning survey paper

---

### Module 5: Unsupervised Learning (Week 10-11)

#### Topics Covered
- Introduction to unsupervised learning
- Clustering algorithms:
  - K-Means clustering
  - Hierarchical clustering (Agglomerative and Divisive)
  - DBSCAN (Density-based clustering)
  - Mean Shift
- Clustering evaluation metrics:
  - Silhouette score
  - Davies-Bouldin index
  - Elbow method
- Dimensionality reduction:
  - Principal Component Analysis (PCA)
  - t-SNE
  - UMAP (introduction)
- Association rule learning (introduction)

#### Learning Objectives
- Apply clustering algorithms to real datasets
- Evaluate clustering quality
- Reduce data dimensionality while preserving information
- Visualize high-dimensional data

#### Assignments
- Assignment 6: Customer segmentation project
- Lab Exercise: Dimensionality reduction comparison

#### Readings
- Clustering algorithms comparison
- PCA mathematical foundations

---

### Module 6: Model Evaluation and Optimization (Week 12)

#### Topics Covered
- Bias-variance tradeoff
- Overfitting and underfitting
- Cross-validation techniques:
  - K-fold cross-validation
  - Stratified K-fold
  - Leave-one-out CV
- Hyperparameter tuning:
  - Grid Search
  - Random Search
  - Bayesian Optimization
- Model selection strategies
- Feature selection methods:
  - Filter methods
  - Wrapper methods
  - Embedded methods
- Pipeline creation in Scikit-learn

#### Learning Objectives
- Diagnose model performance issues
- Implement cross-validation properly
- Optimize model hyperparameters
- Build ML pipelines for reproducibility

#### Assignments
- Assignment 7: Model optimization challenge
- Quiz 4: Model evaluation concepts

#### Readings
- Cross-validation best practices
- Hyperparameter tuning strategies

---

### Module 7: Introduction to Deep Learning (Week 13-14)

#### Topics Covered
- Neural Networks fundamentals:
  - Perceptron
  - Activation functions
  - Backpropagation
  - Gradient descent variants
- Building neural networks with TensorFlow/Keras:
  - Sequential API
  - Model compilation and training
  - Callbacks and early stopping
- Deep learning architectures:
  - Feedforward Neural Networks
  - Convolutional Neural Networks (CNNs) for images
  - Introduction to Recurrent Neural Networks (RNNs)
- Transfer learning
- Introduction to Natural Language Processing:
  - Text preprocessing
  - Word embeddings
  - Sentiment analysis

#### Learning Objectives
- Understand neural network fundamentals
- Build and train neural networks
- Apply CNNs for image classification
- Implement basic NLP tasks

#### Assignments
- Assignment 8: Image classification with CNN
- Lab Exercise: Neural network architecture exploration

#### Readings
- Deep learning book (selected chapters)
- CNN architectures paper

---

### Module 8: ML Project Development and Best Practices (Week 15-16)

#### Topics Covered
- End-to-end ML project workflow:
  - Problem definition
  - Data collection and preparation
  - Model development
  - Evaluation and iteration
  - Deployment considerations
- ML best practices:
  - Code organization
  - Version control with Git
  - Experiment tracking
  - Documentation
- Model deployment basics:
  - Saving and loading models
  - Creating APIs with Flask/FastAPI
  - Basic cloud deployment
- Ethical considerations in ML:
  - Bias and fairness
  - Privacy and security
  - Interpretability and explainability
- Common pitfalls and debugging strategies
- Career paths in ML

#### Learning Objectives
- Execute complete ML projects independently
- Follow industry best practices
- Consider ethical implications of ML systems
- Prepare models for deployment

#### Assignments
- **Final Project**: End-to-end ML project (see project guidelines)
- Presentation: Project demonstration

#### Readings
- ML engineering best practices
- Ethics in AI and ML

---

## Assessment and Grading

### Grade Distribution

| Component | Weight | Description |
|-----------|--------|-------------|
| Weekly Assignments (7) | 30% | Individual assignments, best 6 of 7 count |
| Module Quizzes (4) | 20% | Closed-book quizzes on theory |
| Mid-term Project | 20% | Classification project (Week 9) |
| Final Project | 25% | End-to-end ML project (Week 16) |
| Participation & Labs | 5% | Class participation and lab exercises |

### Grading Scale

| Grade | Percentage | Description |
|-------|------------|-------------|
| A | 90-100% | Excellent |
| B | 80-89% | Good |
| C | 70-79% | Satisfactory |
| D | 60-69% | Passing |
| F | Below 60% | Fail |

### Late Policy

- **Assignments**: 10% penalty per day late (max 3 days)
- **Projects**: 15% penalty per day late (max 2 days)
- **Quizzes**: No make-up quizzes except for documented emergencies

---

## Required Materials

### Textbooks (Recommended)

1. **"Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow"** by Aurélien Géron (3rd Edition)
2. **"Python Machine Learning"** by Sebastian Raschka (3rd Edition)

### Software Requirements

- Python 3.8 or later
- Jupyter Notebook or JupyterLab
- Libraries: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, TensorFlow/Keras
- Git for version control

### Additional Resources

- Course GitHub repository (this repository)
- Online tutorials and documentation
- Kaggle for datasets and competitions
- Stack Overflow for troubleshooting

---

## Course Policies

### Attendance

- Regular attendance is strongly encouraged
- Lab sessions are mandatory
- Missing more than 25% of classes may result in grade penalties

### Academic Integrity

- All work must be your own
- Collaboration is encouraged for learning, but submissions must be individual
- Plagiarism will result in zero grade and potential disciplinary action
- See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details

### Communication

- **Questions**: Use course discussion forum or GitHub issues
- **Office Hours**: To be announced
- **Response Time**: Expect replies within 48 hours
- **Email**: For personal or sensitive matters only

### Accessibility

- Accommodations available for students with documented disabilities
- Contact instructor early in the semester to arrange accommodations

---

## Weekly Schedule

| Week | Module | Topics | Deliverables |
|------|--------|--------|--------------|
| 1 | Module 1 | Introduction to ML, Python setup | - |
| 2 | Module 1 | NumPy, Pandas, Matplotlib | Assignment 1, Quiz 1 |
| 3 | Module 2 | EDA and data visualization | - |
| 4 | Module 2 | Data preprocessing, feature engineering | Assignment 2 |
| 5 | Module 3 | Linear and polynomial regression | - |
| 6 | Module 3 | Regularization, evaluation | Assignment 3, Quiz 2 |
| 7 | Module 4 | Logistic regression, KNN | - |
| 8 | Module 4 | Decision trees, SVM | Assignment 4 |
| 9 | Module 4 | Ensemble methods | Assignment 5, Mid-term Project |
| 10 | Module 5 | Clustering algorithms | Quiz 3 |
| 11 | Module 5 | Dimensionality reduction | Assignment 6 |
| 12 | Module 6 | Model evaluation and optimization | Assignment 7, Quiz 4 |
| 13 | Module 7 | Neural networks, TensorFlow/Keras | - |
| 14 | Module 7 | CNNs, NLP basics | Assignment 8 |
| 15 | Module 8 | ML project workflow, best practices | - |
| 16 | Module 8 | Ethics, deployment, career paths | Final Project |

---

## Additional Learning Opportunities

### Optional Topics (Time Permitting)

- Advanced deep learning architectures
- Time series analysis and forecasting
- Recommender systems
- Anomaly detection
- AutoML tools

### Suggested Activities

- Participate in Kaggle competitions
- Contribute to open-source ML projects
- Attend ML meetups and conferences
- Read ML research papers
- Build portfolio projects

---

## Support and Resources

### Getting Help

1. Review module materials and documentation
2. Search course discussion forum
3. Attend office hours
4. Form study groups with peers
5. Contact teaching assistants
6. Email instructor for complex issues

### Mental Health and Wellness

- University counseling services available
- Don't hesitate to reach out if struggling
- Workload management strategies provided

---

## Course Improvements

This course is continuously improved based on student feedback. Please share:

- What's working well
- What could be improved
- Suggestions for new topics
- Resource recommendations

Feedback can be shared:
- Through mid-semester survey
- During office hours
- Via anonymous suggestion box
- In end-of-course evaluation

---

**We're excited to embark on this ML journey with you! Let's make it a great learning experience! 🚀**

---

*This syllabus is subject to change with advance notice. Any changes will be communicated through official course channels.*

*Last Updated: December 2024*
