"""
Função boletim() que recebe várias notas e colocar em um dicionário: quant de notas, maior, menor, média e situação
"""


def boletim(*notas, sit=False):
    """
    analisa notas e situação do aluno
    :param notas: uma ou mais notas de um aluno
    :param sit: valor booleano, indica se quer ver a situação do anulo
    :return: dicionário com quantidade de notas, maior nota, menor nota, média e situação
    """
    final = {
        'total': len(notas),
        'maior': max(notas),
        'menor': min(notas),
        'media': sum(notas)/len(notas),
    }
    if sit:
        if 0 <= final['media'] < 5:
            final['situação'] = str('reprovado')
        elif 5 <= final['media'] < 7:
            final['situação'] = str('em recuperacao')
        else:
            final['situação'] = str('aprovado')
    return final


resposta = boletim(3.5, 9, 2, 7, 4, sit=True)
print(resposta)
