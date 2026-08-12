# PQD Classifier

A Machine Learning algorithm capable of classifying Power Quality Disturbances from a signal according to IEEE 1159.

This repository holds the code to reproduce and analyze experiment results in an orderly fashion.

## Installation

Clone this repository

```$ git clone https://github.com/josephlinares/PQD-Classifier.git```

Set up a python environment, in Windows

```> cd PQD-Classifier```
```> py -3.12 -m venv .venv```
```> .venv/Scripts/activate```
```> py tensorflow keras scipy numpy pandas matplotlib seaborn scikit-learn ai-edge-litert PyYAML```

Usage:

Activate your environment every new session

```> .venv/Scripts/activate```
```> cd src```
```> py main.py```

Currently datasets are not included, but weights are, they can be used with the architecture found at models.py