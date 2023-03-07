todosiguales([]).
todosiguales([_]).
todosiguales([Elem,Elem|Cola]):-
    todosiguales([Elem|Cola]).
