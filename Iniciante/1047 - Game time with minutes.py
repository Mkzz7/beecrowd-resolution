a, b, c, d = map(int, input().split())

inicio_em_minutos = (a * 60) + b
fim_em_minutos = (c * 60) + d

duracao_em_minutos = fim_em_minutos - inicio_em_minutos

if duracao_em_minutos <= 0:
    duracao_em_minutos += 24 * 60

duracao_horas = duracao_em_minutos // 60
duracao_minutos = duracao_em_minutos % 60

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")