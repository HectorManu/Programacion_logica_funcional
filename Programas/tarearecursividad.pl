% caso base 1: si uno de los arreglos está vacío, la respuesta es el otro arreglo
unir_arreglos([], Y, Y).
unir_arreglos(X, [], X).

% caso base 2: si ambos arreglos están vacíos, la respuesta es un arreglo vacío
unir_arreglos([], [], []).

% caso recursivo: se compara el primer elemento de cada arreglo y se agrega el más pequeño al nuevo arreglo
unir_arreglos([X|Xs], [Y|Ys], [X|Zs]) :- X =< Y, unir_arreglos(Xs, [Y|Ys], Zs).
unir_arreglos([X|Xs], [Y|Ys], [Y|Zs]) :- X > Y, unir_arreglos([X|Xs], Ys, Zs).
