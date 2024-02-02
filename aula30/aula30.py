"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

# Exemplo 1
# velocidade = 61  # velocidade atual do carro
# local_carro = 99  # local em que o carro está na estrada

# RADAR_1 = 60  # velocidade máxima do radar 1
# LOCAL_1 = 100  # local onde o radar 1 está
# RADAR_RANGE = 1  # A distância onde o radar pega

# if velocidade > RADAR_1:
#     print("Velocidade carro passou do radar 1")

# if local_carro >= (LOCAL_1 - RADAR_RANGE) \
#     and local_carro <= (LOCAL_1 + RADAR_RANGE) \
#     and velocidade > RADAR_1:
#     print("carro multado em radar 1")

velocidade = 61  # velocidade atual do carro
local_carro = 99  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

carro_local_range_min = LOCAL_1 - RADAR_RANGE
carro_local_range_max = LOCAL_1 + RADAR_RANGE
vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_esta_no_range_min = local_carro >= carro_local_range_min
carro_esta_no_range_max = local_carro <= carro_local_range_max
carro_passou_radar_1 = carro_esta_no_range_min and carro_esta_no_range_max
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print("Velocidade carro passou do radar 1")

if carro_passou_radar_1:
    print("Carro passou no radar 1")

if carro_multado_radar_1:
    print("carro multado em radar 1")
