import numpy as np

# R, T and S are functions that return the integral of f in the interval [a,b] using different numerical integration methods


def R(f, a, b):
    """rectangle rule"""
    return (b-a) * f((a+b)/2)


def T(f, a, b):
    """trapezoid rule"""
    return 1/2 * (b-a) * (f(a) + f(b))


def S(f, a, b):
    """Simpson rule"""
    return (b-a)/6 * (f(a) + f(b) + 4*f((a+b)/2))

# Rh, Th and Sh are functions that return the summed variants of these approximations with n equally wide subintervals


def Rh(f, a, b, n):
    """rectangle rule"""
    h = (b - a) / n  # width of each subinterval
    # The summed rectangle rule
    return h * sum(f(a + i * h + h / 2) for i in range(n))


def Th(f, a, b, n):
    """trapezoid rule"""
    h = (b - a) / n  # width of each subinterval
    # The summed trapezoid rule
    return h * ((f(a) + f(b)) / 2 + sum(f(a + i * h) for i in range(1, n)))


def Sh(f, a, b, n):
    """Simpson rule"""
    h = (b - a) / n  # width of each subinterval
    # The summed Simpson rule
    return h/6 * (f(a) + f(b) + 2 * sum(f(a + i * h) for i in range(1, n)) + 4 * sum(f(a + i * h + h/2) for i in range(0, n)))

# Test funciton


def test(f):
    print(f)

#Function for evaluating the number of subintervals 


def n_Teilintervalle(f, a, b, true_result, max_abs_fehler, Regel='Rh', p=False):
    if (Regel == 'Rh'):
        n = 1
        while (abs((Rh(f, a, b, n) - true_result)) >= max_abs_fehler):
            n += 1
        print(
            f'Anz. Intervalle mit summierter Rechtecksregel für abs. Fehler < {max_abs_fehler} für Funktion {f.__name__}: {n}. Abs. Fehler = {round(abs(Rh(f,a,b,n) - true_result), 5)}') if p == True else None
        return n
    elif (Regel == 'Th'):
        n = 1
        while (abs((Th(f, a, b, n) - true_result)) >= max_abs_fehler):
            n += 1
        print(
            f'Anz. Intervalle mit summierter Trapezregel für abs. Fehler < {max_abs_fehler} für Funktion {f.__name__}: {n}. Abs. Fehler = {round(abs(Th(f,a,b,n) - true_result), 5)}') if p == True else None
        return n
    elif (Regel == 'Sh'):
        n = 1
        while (abs((Sh(f, a, b, n) - true_result)) >= max_abs_fehler):
            n += 1
        print(
            f'Anz. Intervalle mit summierter Simpsonsregel für abs. Fehler < {max_abs_fehler} für Funktion {f.__name__}: {n}. Abs. Fehler = {round(abs(Sh(f,a,b,n) - true_result), 5)}') if p == True else None
        return n
    else:
        print('Falsche Eingabe (Regel)')

# density function


def phi(x):
    return np.exp((-x**2)/2) / np.sqrt(2*np.pi)

# Gauß-function


def Gauß(a, b):
    # Limit upper limit
    if b > 50:
        b = 50

    # Maximum of the 4th derivative given in specification
    M = 3 / np.sqrt(2*np.pi)

    # Calculate the number n of subintervals to 10 decimal places
    max_fehler = 10**(-11)
    n = int(np.power((M*(abs(b-a))**5)/(2880*max_fehler), 1/4)) + 1
    print(n)
    return Sh(phi, a, b, n)
