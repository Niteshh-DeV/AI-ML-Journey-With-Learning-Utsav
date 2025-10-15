# Machine Learning: Overview and Types

Machine learning (ML) is a subset of artificial intelligence that enables systems to learn patterns from data and make predictions or decisions with minimal explicit programming. Instead of hard‑coded rules, models infer relationships from examples.

## Why it matters
- Automates decisions at scale (recommendations, fraud detection).
- Extracts insights from complex, high‑dimensional data (images, text, logs).
- Continuously improves as more data arrives.

## Core types of machine learning

1) Supervised Learning
- Goal: Learn a mapping from inputs (X) to labeled outputs (y).
- Tasks: Classification (categorical y), Regression (continuous y).
- Algorithms: Linear/Logistic Regression, Decision Trees, Random Forests, Gradient Boosting (XGBoost, LightGBM), SVM, k‑NN, Neural Networks.
- Examples:
    - Email spam detection (classification).
    - House price prediction from features (regression).
    - Credit risk scoring.

2) Unsupervised Learning
- Goal: Discover structure in unlabeled data.
- Tasks: Clustering, Dimensionality Reduction, Density Estimation, Anomaly Detection.
- Algorithms: k‑Means, DBSCAN, Hierarchical Clustering, PCA, t‑SNE/UMAP, Isolation Forest.
- Examples:
    - Customer segmentation for marketing.
    - Compressing features with PCA before modeling.
    - Identifying unusual network traffic.

3) Semi‑Supervised Learning
- Goal: Leverage a small labeled set plus a large unlabeled set.
- Techniques: Self‑training, Label propagation, Consistency regularization.
- Examples:
    - Classifying documents when only a fraction are labeled.
    - Medical imaging with limited expert annotations.

4) Self‑Supervised Learning
- Goal: Create surrogate tasks on unlabeled data to learn useful representations.
- Domains: Vision (contrastive learning), NLP (masked language modeling).
- Examples:
    - Pretraining BERT on text, then fine‑tuning for sentiment.
    - Learning image embeddings with SimCLR, then classifying with few labels.

5) Reinforcement Learning (RL)
- Goal: Learn actions that maximize cumulative reward through trial and error.
- Elements: Agent, Environment, Policy, Reward.
- Algorithms: Q‑Learning, DQN, Policy Gradients, PPO.
- Examples:
    - Game playing (Atari, Go).
    - Recommendation ranking with long‑term engagement objectives.
    - Robotics path planning.

6) Deep Learning (cross‑cutting)
- What: Neural networks with many layers; excels at unstructured data.
- Architectures: CNNs (images), RNN/LSTM/GRU (sequences), Transformers (text/audio/vision).
- Examples:
    - Image classification, object detection.
    - Speech recognition, machine translation, large language models.

7) Transfer Learning
- Goal: Adapt a model pretrained on one task/domain to another.
- Examples:
    - Fine‑tuning ResNet on a small medical dataset.
    - Adapting a pretrained language model for intent classification.

## Typical ML workflow
- Problem framing and metrics
- Data collection and labeling
- Feature engineering or representation learning
- Model selection and training
- Validation, hyperparameter tuning, and evaluation
- Deployment, monitoring, and iteration

## Choosing an approach (quick guide)
- Labeled data and clear target: Supervised.
- No labels, explore structure: Unsupervised.
- Few labels, many unlabeled: Semi/Self‑supervised + fine‑tune.
- Sequential decisions with feedback: Reinforcement Learning.
- Images/audio/text: Prefer deep learning; consider transfer learning.
