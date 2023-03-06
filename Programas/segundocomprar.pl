sevende(vestido).
sevende(sombrero).
sevende(zapatos).
gusta(jaime,zapatos).
gusta(maria,vetido).
gusta(maria,sombrero).
bueno(sombrero).
compra(Quien,Algo):-sevende(Algo),gusta(Quien,Algo),bueno(Algo).
