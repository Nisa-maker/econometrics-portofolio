# Optimizing Social Assistance Targeting: An Econometric Simulation

## Overview

This project presents an econometric evaluation of social assistance (Bansos) targeting efficiency using a structured household-level simulation dataset. 

By applying Logistic Regression (Logit Model) to 5,000 simulated households, this study estimates how socio-economic indicators influence eligibility and assesses the prevalence of targeting errors.

The objective is to demonstrate applied econometric modeling for public policy optimization and fiscal efficiency analysis.

---

## Research Objective

This study aims to model the probability of a household being eligible for social assistance based on:

- **Monthly Income** – Proxy for economic status  
- **Number of Dependents** – Proxy for household burden  
- **Housing Condition** – Qualitative proxy for wealth  

The model seeks to minimize:

- **Inclusion Error** – Assistance granted to non-eligible households  
- **Exclusion Error** – Eligible households left without assistance  

This aligns with broader public economics objectives of improving redistributive efficiency and fiscal targeting performance.

---

## Methodology

### Model Specification

A Logistic Regression (Logit) model is employed due to the binary nature of eligibility:

![Yi](https://latex.codecogs.com/svg.image?Y_i%20%5Cin%20%7B0,1%7D)


The probability function is defined as:

![Logistic Model](https://latex.codecogs.com/svg.image?P(Y_i=1)=\frac{1}{1+e^{-(\beta_0+\beta_1%20Income_i+\beta_2%20Dependents_i+\beta_3%20Housing_i)}})


### Dataset

- Structured simulation dataset  
- **Sample Size:** N = 5,000 households  
- Cross-sectional micro-level analysis  
- Generated using `numpy.random` to preserve realistic socio-economic distributions  

---

## Model Performance

### Statistical Robustness

- **Pseudo R-squared:** 0.3451  
- **LLR p-value:** 4.214 × 10⁻²⁰¹  
- Indicates strong explanatory power for a social cross-sectional model  

### Regression Results

| Variable         | Coefficient   | P-value | Significance |
|------------------|--------------|---------|-------------|
| Intercept        | 0.5854       | 0.004   | **          |
| Monthly Income   | -3.929e-06   | 0.000   | ***         |
| Dependents       | 0.5382       | 0.000   | ***         |

**Interpretation:**
- Income has a statistically significant negative relationship with eligibility.
- The number of dependents significantly increases the probability of receiving assistance.

---

## Targeting Accuracy

| Status              | Count | Percentage |
|---------------------|-------|------------|
| Correctly Targeted  | 4,211 | 84.22%     |
| Inclusion Error     | 663   | 13.26%     |
| Exclusion Error     | 126   | 2.52%      |

Overall model accuracy: **84.2%**

---

## Policy Implications

While the model demonstrates high targeting accuracy, the 126 exclusion errors represent vulnerable households not reached by the system.

From a public policy perspective, reducing exclusion errors should be prioritized, as they directly affect social welfare outcomes.

This project illustrates the integration of econometric modeling and policy interpretation — translating statistical outputs into actionable governance insights.

---

## Tech Stack

- **Python 3.12**
- `pandas`
- `numpy`
- `statsmodels`
- `scikit-learn`
- `matplotlib`
- `seaborn`

---

## Repository Structure

econometrics-portofolio/
│
├── project/
│ └── regression/
│ ├── regression.ipynb
│ │ ├── Data generation (N = 5,000 households)
│ │ ├── Descriptive statistics
│ │ ├── Logistic regression estimation
│ │ ├── Model evaluation (Pseudo R², LLR test)
│ │ └── Confusion matrix analysis
│ │
│ ├── dummy_social_assistance_targeting.csv
│ │ └── Simulated household-level dataset
│ │
│ └── readme.md
│ └── Project-specific documentation
│
├── README.md
│ └── Main project documentation
│
└── .gitignore
└── Excludes virtual environment and cache files
