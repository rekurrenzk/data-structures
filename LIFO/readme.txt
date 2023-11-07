In this py. filed, I implemented a class that tracks actions.

It also allows for some level of history management.

This concept is useful for two main reason:

    1- It is possible to create an activity recorder for automatized
    data algorithm suggestion. Here think of it as a "did you mean {x}?" suggestion used
    in browsers.

    2- Since the 'recall' mechanism is limited with a buffer (here we used 10)
    for word/command choices) it is possible to implement a further function design for suggestions.
    For example, although buffer would delete command choices, the data can be
    vectorized to heuristic guessing. It is somewhat similar to NL algorithms, where direct usage
    of matrix is not suggested but rather weights are calculated through vectorization.

