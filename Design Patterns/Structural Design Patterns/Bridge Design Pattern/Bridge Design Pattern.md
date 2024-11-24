A Bridge Pattern says that just "decouple the functional abstraction from the implementation so that the two can vary independently".

The Bridge Pattern is also known as Handle or Body.

Advantage of Bridge Pattern
- It enables the separation of implementation from the interface.
- It improves the extensibility.
- It allows the hiding of implementation details from the client.

Note: Besides interface and its implementation, create a bridge class to use interface and its implementation. Client class can use bridge class for its requirements. In this way, interface and implemetation is decoupled.