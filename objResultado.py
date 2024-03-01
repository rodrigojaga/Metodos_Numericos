class NRMResultado:
    def __init__(self, i, Xi, fXi, fXiDerivada, fXiSegundaDerivada, XiSiguiente, error):
        self.i = i
        self.Xi = Xi
        self.fXi = fXi
        self.fXiDerivada = fXiDerivada
        self.fXiSegundaDerivada = fXiSegundaDerivada
        self.XiSiguiente = XiSiguiente
        self.error = error


class NRSimpleResultado:
    def __init__(self, i, Xi, fXi, fXiDerivada, XiSiguiente, error):
        self.i = i
        self.Xi = Xi
        self.fXi = fXi
        self.fXiDerivada = fXiDerivada
        self.XiSiguiente = XiSiguiente
        self.error = error


class biseccionResultado:
    def __init__(self, i, Xl, fXl, Xu, fXu, Xr, fXr, error):
        self.i = i
        self.Xl = Xl
        self.fXl = fXl
        self.Xu = Xu
        self.fXu = fXu
        self.Xr = Xr
        self.fXr = fXr
        self.error = error


class ecuacionCuadraticaResultado:
    def __init__(self, a, b, c, X1, X2):
        self.a = a
        self.b = b
        self.c = c
        self.X1 = X1
        self.X2 = X2
