"""
Tratamento de erros
    o python não aceita erro de sintaxe, mas erros de semântica às vezes passam despercebidos, se ligue;
    quando os erros são semânticos, são chamados de excessão, ou Exception:
        NameError
        ValueError
        TypeError
        ZeroDivisionError

    um try pode ter vários except
        try:

        except TypeError:

        except ValueError:

        except OSError:
"""
try:
    a = int(input('numerado: '))
    b = int(input('denominador: '))
    n = a/b
except (ValueError, TypeError):
    print(f'erro: tipo de dados digitados')
except ZeroDivisionError:
    print('impossibilidade de dividir por zero')
except KeyboardInterrupt:
    print('não digitou valores')
except Exception as erro:
    print(f'deu erro: {erro}')
# opcional else
else:
    print(f'{a}/{b} = {n:.2f}')
# opcional finally
finally:
    print('programa finalizado')
