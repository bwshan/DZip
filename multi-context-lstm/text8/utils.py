import numpy as np
import keras

def iterate_minibatches(inputs, targets, batchsize, n_classes, shuffle=False):
    assert inputs.shape[0] == targets.shape[0]
    if shuffle:
        indices = np.arange(inputs.shape[0])
        np.random.shuffle(indices)
    for start_idx in range(0, inputs.shape[0] - batchsize + 1, batchsize):
        # if(start_idx + batchsize >= inputs.shape[0]):
        #   break;

        if shuffle:
            excerpt = indices[start_idx:start_idx + batchsize]
        else:
            excerpt = slice(start_idx, start_idx + batchsize)
        yield inputs[excerpt], keras.utils.to_categorical(targets[excerpt], num_classes=n_classes)
