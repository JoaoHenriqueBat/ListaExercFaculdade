
quantidade_pequenas = int(input("Digite a quantidade de camisetas pequenas vendidas: "))
quantidade_medias = int(input("Digite a quantidade de camisetas médias vendidas: "))
quantidade_grandes = int(input("Digite a quantidade de camisetas grandes vendidas: "))


valor_arrecadado = quantidade_pequenas * 10 + quantidade_medias * 12 + quantidade_grandes * 15

print("O valor arrecadado com a venda das camisetas foi R$ {:.2f}".format(valor_arrecadado))
