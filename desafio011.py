larg = float(input('Digite aqui a largura da sua perde: '))
alt = float(input('Digite aqui a altura da sua parde: '))
area = larg*alt
tinta = area/2
print('Sua perde tem a dimensão de {} x {} e sua área é de {}m² \nPara pintar essa parede, você precisará de {}l de tinta'.format(larg, alt, area, tinta))