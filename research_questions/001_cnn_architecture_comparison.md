# Research Study 001 — CNN Architecture Comparison

## Research Question

Does a customized multi-scale dilated CNN provide measurable performance differences compared with a standard residual CNN when both models receive the same dataset, preprocessing, training budget, and evaluation protocol?

## Hypothesis

Multi-scale receptive fields may improve recognition of patterns occurring at different spatial scales. The experiment should test this rather than assume it.

## Experimental Controls

- Same dataset
- Same train/validation/test split
- Same preprocessing
- Same augmentation policy
- Same optimizer family
- Same training budget
- Fixed random seeds
- Common evaluation metrics

## Candidate Models

1. Baseline CNN
2. Standard ResNet
3. Dilated CNN
4. Multi-scale dilated CNN

## Metrics

- Accuracy
- Precision
- Recall
- F1
- ROC-AUC where appropriate
- Training time
- Inference latency
- Parameter count

## Required Analysis

- Learning curves
- Confusion matrix
- Per-class performance
- Error analysis
- Ablation study
- Variability across seeds
- Operational interpretation

## Expected Deliverables

- Reproducible notebook
- Configuration file
- Model implementations
- Results table
- Research figures
- Error-analysis report
- Final research report
