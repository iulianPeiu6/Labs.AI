import os
import math

def sigmoid_function(x):
    #Logistic Sigmoid Function Formula
    return math.exp(x) / (math.exp(x) + 1)

def read_parameters():
    nr_max_epochs = input("DEBUG:\t Enter maximum number of epochs: ")
    learning_rate = input("DEBUG:\t Enter the learning rate: ")
    vector_of_parameters = [nr_max_epochs, learning_rate]
    return vector_of_parameters

def read_dataset(file):
    f = open(file, "r")
    data_set = f.read()
    f.close()
    return data_set


#TEST
print("Sigmoid function result: ", sigmoid_function(3))
print("\nDataset: ")
print(read_dataset("dataset.txt"))
