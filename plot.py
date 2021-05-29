import matplotlib.pyplot as plt

def plot(xArray, yArray):
    plt.plot(xArray, yArray)
    plt.xlabel('n - array size')
    plt.ylabel("iteration - repeat counts")
    plt.title("Plot of Size vs Iterations")
    plt.show()