% Facts: defining parent relationships
parent(john, mary).    % John is a parent of Mary
parent(john, peter).   % John is a parent of Peter
parent(susan, mary).   % Susan is a parent of Mary
parent(susan, peter).  % Susan is a parent of Peter
parent(mary, james).   % Mary is a parent of James
parent(mary, linda).   % Mary is a parent of Linda
parent(paul, james).   % Paul is a parent of James
parent(paul, linda).   % Paul is a parent of Linda

% Gender facts
male(john).
male(peter).
male(james).
male(paul).

female(susan).
female(mary).
female(linda).

% Rules: defining child relationships
child(X, Y) :- parent(Y, X).

% Rule to define grandparent relationship
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% Rule to define grandchild relationship
grandchild(X, Y) :- grandparent(Y, X).

% Rule to define sibling relationship
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Rule to define brother relationship
brother(X, Y) :- sibling(X, Y), male(X).

% Rule to define sister relationship
sister(X, Y) :- sibling(X, Y), female(X).

% Rule to define uncle relationship
uncle(X, Y) :- brother(X, Z), parent(Z, Y).

% Rule to define aunt relationship
aunt(X, Y) :- sister(X, Z), parent(Z, Y).
