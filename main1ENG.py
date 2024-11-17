import numpy as np
import matplotlib.pyplot as plt
import lib1

# Definitions of the functions f1 to f4 and their domain of definition


def f1(x):
    return np.power(x, 3)


def f2(x):
    return np.power(x, 4) - 2 * np.power(x, 3) + 3


def f3(x):
    return 2 * np.power(x, 1/7)


def f4(x):
    return 2 * np.sin(x)


interval_dict = {f1: [-1, 2], f2: [0, 2], f3: [0, 128], f4: [0, 31*np.pi]}


# Implementation of a function to store the true function values:
def true_result(f):
    dict_result = {f1: 3.75, f2: 4.4, f3: 448, f4: 4}
    return dict_result[f]


# List of smallest subintervals
Anzahlen = []

for f in f1, f2, f3, f4:
    Anzahlen.append(lib1.n_Teilintervalle(
        f, interval_dict[f][0], interval_dict[f][1], true_result(f), 1/10, 'Sh', p=False))


if __name__ == "__main__":
    
    
   # Determination of number of subintervals for
    for Regel in 'Rh', 'Th', 'Sh':
        for f in f1, f2, f3, f4:
            lib1.n_Teilintervalle(
                f, interval_dict[f][0], interval_dict[f][1], true_result(f), 1/10, Regel, p=True)

   # Test Gaussian function:
    for a in 0, 1, 2:
        for b in 1, 4, 10**7:
            lib1.Gauß(a, b)

    # Output of functions f1 - f4 as graphic plot:
    x = np.linspace(-1, 2, 100)

    plt.plot(x, f1(x), label="f1")
    plt.plot(x, f2(x), label="f2")
    plt.plot(x, f3(x), label="f3")
    plt.plot(x, f4(x), label="f4")
    plt.legend()
    plt.show()
