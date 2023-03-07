encuentra(Elem,[Elem|_]).
encuentra(Elem,[_|Cola]):-
    encuentra(Elem,Cola).
