import numpy as np


def sigmoid(x):
    return 1/(1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


class NeuralNetwork(object):
    def __init__(self, num_epochs, learning_rate):
        self.num_epochs = num_epochs
        self.learning_rate = learning_rate

        self.inputs = np.array([
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]])

        self.expected_output = np.array([
            [0],
            [0],
            [0],
            [1]])

        self.input_layer_neurons = 2
        self.hidden_layer_neurons = 2
        self.output_layer_neurons = 1

        self.hidden_weights = np.random.uniform(size=(self.input_layer_neurons, self.hidden_layer_neurons))
        self.hidden_bias = np.random.uniform(size=(1, self.hidden_layer_neurons))
        self.output_weights = np.random.uniform(size=(self.hidden_layer_neurons, self.output_layer_neurons))
        self.output_bias = np.random.uniform(size=(1, self.output_layer_neurons))

    def init(self):
        for epoch in range(self.num_epochs + 1):
            hidden_layer_output, predicted_output = self.run_forward_pass_iteration()
            if epoch % 100 == 0:
                self.print_output_prediction(epoch, predicted_output)
            self.run_backpropagation_iteration(hidden_layer_output, predicted_output)

    def run_forward_pass_iteration(self):
        hidden_layer_activation = np.dot(self.inputs, self.hidden_weights)
        hidden_layer_activation += self.hidden_bias
        hidden_layer_output = sigmoid(hidden_layer_activation)
        output_layer_activation = np.dot(hidden_layer_output, self.output_weights)
        output_layer_activation += self.output_bias
        predicted_output = sigmoid(output_layer_activation)
        return hidden_layer_output, predicted_output

    def run_backpropagation_iteration(self, hidden_layer_output, predicted_output):
        error = self.expected_output - predicted_output
        d_predicted_output = error * sigmoid_derivative(predicted_output)

        error_hidden_layer = d_predicted_output.dot(self.output_weights.T)
        d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

        self.output_weights += hidden_layer_output.T.dot(d_predicted_output) * self.learning_rate
        self.output_bias += np.sum(d_predicted_output, axis=0, keepdims=True) * self.learning_rate
        self.hidden_weights += self.inputs.T.dot(d_hidden_layer) * self.learning_rate
        self.hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True) * self.learning_rate

    @staticmethod
    def print_output_prediction(epoch, predicted_output):
        print(f"[DEBUG]\t Epoch {epoch}. Predicted Output:")
        print(f"\t\t 0 & 0 = {predicted_output[0]}")
        print(f"\t\t 0 & 1 = {predicted_output[1]}")
        print(f"\t\t 1 & 0 = {predicted_output[2]}")
        print(f"\t\t 1 & 1 = {predicted_output[3]}")


if __name__ == '__main__':
    neural_network = NeuralNetwork(1000, 0.5)
    neural_network.init()


