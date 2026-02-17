class Result:
    def __init__(self, value = None, error = None):
        self.value = value
        self.error = error

    def is_ok(self):
        return self.error is None


def calcular (valor1 , valor2, operação) -> Result:
    try:
        if operação == '+':
            resultado = valor1 + valor2

        elif operação == '-':
            resultado = valor1 - valor2

        elif operação == '/':
            resultado = valor1 / valor2

        else:
            return Result (error = 'Operação invalida')

        return Result (value=resultado)

    except Exception as e:
        return Result(error=str(e))

while True:
    try:
        v1 = float(input('Digite o primeiro valor: '))
        op = input('Digite a operação (+ - / ) ')
        v2 = float(input('Digite o segundo valor: '))

        resultado = calcular(v1, v2, op)

        if resultado.is_ok():
            print('Resultado: ', resultado.value)
        else:
            print('Resultado: ', resultado.error)

    except ValueError:
        print('Digite apenas números!')

    escolha = input('Deseja continuar? ').upper()
    if escolha != 'S':

        break