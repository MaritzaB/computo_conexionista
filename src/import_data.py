#!/usr/bin/env python3
# -*- coding: utf-8 -*-

data_dir = 'data/cifar-10-python/cifar-10-batches-py/'


def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict