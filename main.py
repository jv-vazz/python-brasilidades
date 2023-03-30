from acesso_cep import BuscaEndereco

cep = '25056120'

localidade = BuscaEndereco(cep)

logradouro, bairro, localidade, uf = localidade.acessa_via_cep()


print(f"Meu bairro é {bairro} o logradouro é {logradouro}, minha cidade é {localidade} no estado {uf}")

