# -*- coding: utf-8 -*-

# Created on Tue May 5 08:39:57 2026, @author: github.com/seneviratneranasingha-alt
# Updated on Sat Jun 6 2026, @author: github.com/aditya1962

# This script trains a custom PyTorch deep learning model to predict solubility from molecular structures

import deepchem as dc
import torch

# Initialize a standard multilayer perceptron
# Input Layer: Takes an input vector of size 1024 and maps it to 1000 hidden units.
# Activation: Applies a ReLU (Rectified Linear Unit) function to introduce non-linearity.
# Regularization: Applies a Dropout layer with a 50% probability to prevent overfitting.
# Output Layer: Maps the 1000 hidden units down to a single continuous output (1).

pytorch_model =	torch.nn.Sequential(torch.nn.Linear(1024,	1000),
									torch.nn.ReLU(),
									torch.nn.Dropout(0.5),
									torch.nn.Linear(1000,	1))

# Loads the Delaney (ESOL) dataset
# featurizer 'ECFP' converts the raw chemical structures (SMILES strings) into Extended-Connectivity Fingerprints

tasks, datasets, transformers =	dc.molnet.load_delaney(featurizer='ECFP', splitter='random')
train_dataset, valid_dataset, test_dataset = datasets

# R^2 performance metric or coefficient of determination using Pearson correlation
metric = dc.metrics.Metric(dc.metrics.pearson_r2_score)

# Create the model and trains it on the train_dataset for 20 epochs.
model =	dc.models.TorchModel(pytorch_model,	dc.models.losses.L2Loss())
model.fit(train_dataset, nb_epoch=20)

print('training	set	score: ', model.evaluate(train_dataset,[metric]))
print('test	set	score: ', model.evaluate(test_dataset,[metric]))