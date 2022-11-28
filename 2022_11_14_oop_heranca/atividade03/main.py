from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

poli = '*'*10

pessoaFisica1 = PessoaFisica('Jerson', '140.555.555.-55', 350.00)
print(f'{poli}\n Pessoa Física Inicial\n{poli}')
print(pessoaFisica1)
pessoaFisica1.segundo_titular = 'Cleusa Casagrande'

print(f'{poli}\n Pessoa Física Alterações\n{poli}')
print(pessoaFisica1)

pessoaJuridica1 = PessoaJuridica('Catarininho', '08.239.325/0001-33', 1500.00)
print(f'{poli}\n Pessoa Jurídica Inicial\n{poli}')
print(pessoaJuridica1)
pessoaJuridica1.segundo_titular = 'Beterraba Importações'

print(f'{poli}\n Pessoa Jurídica Alterações\n{poli}')
print(pessoaJuridica1)