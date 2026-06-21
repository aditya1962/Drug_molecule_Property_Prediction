<h1 align="center"> DRUG MOLECULAR PROPERTY FORECASTING USING DEEP LEARNING </h1>

By [Sena Seneviratne](https://scholar.google.com/citations?hl=en&user=RE91Ra8AAAAJ), Udaya Seneviratne, [Aditya Abeysinghe](https://scholar.google.com/citations?user=ECuFNBQAAAAJ&hl=en), [Liyanage C De Silva](https://scholar.google.com/citations?user=utF5BG0AAAAJ&hl=en&oi=sra)

This repository contains Machine Learning models used for the paper. Any publication that discloses findings arising from using this source code or the model parameters should [cite](#cite) the Drug Molecular Property Forecasting Using Deep Learning paper.

# Installation

To run this script, you need a Python environment with two libraries installed: [PyTorch](https://pytorch.org/get-started/locally/) and DeepChem. Because [DeepChem](https://github.com/deepchem/deepchem#installation) relies on specialized chemistry libraries (like [RDKit](https://github.com/rdkit/rdkit/tree/master)), setting this up in a virtual environment is highly recommended.

Please follow the following steps:

1. Install [Python](https://www.python.org/downloads/).
2. Run following commands in a command prompt

```python
# Create and activate a virtual environment
python -m venv dc_env
source dc_env/bin/activate  # On Windows use: dc_env\Scripts\activate

# Install PyTorch and DeepChem
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install deepchem rdkit
```

# Run the scripts

For each script in this codebase run the following in a command prompt

```python
python Solution_pred_PyTorch.py
```

```python
python tox21_MLP_Torch.py
```