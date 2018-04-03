import numpy as np

__author__ = 'Otilia Stretcu'


def accuracy(predictions, targets):
	# TODO: implement this.
    return np.sum(np.array([1 if prediction==target for prediction,target in zip(predictions,targets)]))/targets.shape[0]