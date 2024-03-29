"""
Complete a função verificaTriangulo, que recebe 3 valores inteiros como parâmetro,
considerando que esses valores representam os 3 lados de um triângulo. Como resultado,
o método deve informar se os valores realmente correspondem a um triângulo,
e se o triângulo é equilátero, isósceles ou escaleno.


A saída deve ser apenas um número, conforme o demonstrado abaixo:
0: não é um triângulo
1: equilátero # "triângulo que possui três lados com medidas iguais."
2: isósceles # "triângulo que possui dois lados com medidas iguais"
3: escaleno # "triângulo que possui todos os lados com medidas diferentes"

Veja mais sobre "O que é triângulo?" em: https://brasilescola.uol.com.br/o-que-e/matematica/o-que-e-triangulo.htm

Condição do triângulo
Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra:
um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados
e menor que a soma dos outros dois lados.
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
"""


def validaTriangulo(ladoA: int, ladoB: int, ladoC: int) -> bool:
    if abs(ladoB - ladoC) < ladoA < ladoB + ladoC:
        if abs(ladoA - ladoC) < ladoB < ladoA + ladoC:
            if abs(ladoA - ladoB) < ladoC < ladoA + ladoB:
                return True
    return False


def verificaTriangulo(lado_a: int, lado_b: int, lado_C: int) -> int:
    if not validaTriangulo(lado_a, lado_b, lado_C):
        return 0

    isEquilatero = lado_a == lado_b == lado_C
    isIsosceles = lado_a == lado_b or lado_a == lado_C or lado_b == lado_C
    isEscaleno = lado_a != lado_b != lado_C

    if isEquilatero:
        return 1

    if isIsosceles:
        return 2

    if isEscaleno:
        return 3


if __name__ == '__main__':
    tipos_triangulo = ("Não é um triângulo", "Equilátero", "Isósceles", "Escaleno")

    lados_triangulo = input("Digite os três lado do triangulo separado por virgula (,) [Ex: 5,10,9]: ")
    lados_triangulo = lados_triangulo.split(',')

    ladoA = int(lados_triangulo[0])
    ladoB = int(lados_triangulo[1])
    ladoC = int(lados_triangulo[2])

    class_triangulo = verificaTriangulo(ladoA, ladoB, ladoC)
    print(f"Resultado: {tipos_triangulo[class_triangulo]}")
