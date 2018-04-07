
/*-----FACTS-----*/
parents(jennifer, george, noreen).
parents(david, george, noreen).
parents(georgejr, george, noreen).
parents(scott, george, noreen).
parents(joanne, george, noreen).
parents(jessica, david, edel).
parents(clara, david, edel).
parents(michael, david, edel).
parents(laura, georgejr, susan).
parents(anna, scott, siobhan).

male(george).
male(david).
male(georgejr).
male(scott).
male(michael).

female(noreen).
female(jennifer).
female(joanne).
female(edel).
female(jessica).
female(clara).
female(susan).
female(laura).
female(siobhan).
female(anna).


/*-----RULES----- */
father(X, Y):-
	parents(Y, X, _).

mother(X, Y):-
	parents(Y, _, X).
	
brother(X, Y):-
	male(X),
	father(Z, X),
	father(Z, Y),
	X \= Y.

sister(X, Y):-
	female(X),
	father(Z, X),
	father(Z, Y),
	X \= Y.
	
grandfather(X, Y) :- 
	father(X, Z), father(Z, Y);
	father(X, Z), mother(Z, Y).

grandmother(X, Y) :- 
	mother(X, Z), mother(Z, Y);
	mother(X, Z), father(Z, Y).

uncle(X, Y) :- 
	male(X),
	brother(X, Z), 
	father(Z, Y).

aunt(X, Y) :- 
	female(X),
	sister(X, Z), 
	father(Z, Y).

cousin(X, Y) :- 
	father(Z, X), 
	father(W, Y), 
	brother(Z, W).

	
