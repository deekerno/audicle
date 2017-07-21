This serves as an explanation of why certain aspects or characteristics of the networks were chosen.

# Genre Detection Network (Convolutional Recurrent Neural Network)

## Convolution
One-dimensional (1D) convolution was chosen for our network as we are really only interested in changes over one axis (time). Each of the spectrograms should be the same height (y-axis), which would mean that the only variable dimension would be the length (x-axis). Thus, the network filter will travel and do calculations along the the time axis.

## Dropout
We use dropout regularization to prevent the network from overfitting, which is when a model becomes excessively complex. During this process, neurons are selected at random and are effectively ignored during the training. In general, this prevents both neurons from specializing and the network from relying on the decisions from said specialized neurons.

## Long Short-Term Memory
We also make use of Long Short-Term Memory (LSTM) units in order to better predict (or at least try to do so) the genre of the song. With a regular recurrent neural network, a decision reached at time `t-1` affects the decision it makes at time `t` as it takes input from the time step immediately prior in addition to the other input(s). However, the decisions at time steps less than `t-1`, such as `t-3` and `t-4`, have less of an effect on the decision at time step `t` as the difference increases. LSTMs function as four network layers instead of a singular one with each layer interacting with one another, which allows for prior decisions to exert effects upon current ones for a longer duration.

## Max Pooling
The network filter will take the max of each region represent by it and create a new output matrix in which each element is the max of a region from the original input. This helps to further mitigate overfitting as the network is provided with a more abstract representation on which to train, leading to less complexity in the model.