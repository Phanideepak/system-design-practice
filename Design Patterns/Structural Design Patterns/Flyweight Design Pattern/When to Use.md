# When to Use Fly Weight Pattern

- When Memory is limited.
- When Objects share data.
  -> Intrinsic Data: The data shared among objects and remain same once defined one value
  -> Extrinsic Data: Changes based on client input and differs from one object to another.
- Creation of Object is expensive

## Implement Fly weight Pattern

- Intrinsic Data will be used in flyweight pattern and cached. Extrinsic Data will be passed through a function of a object.
- From object, Remove all extrinsic data and keep intrinsic data. This object is called Flyweight pattern
- Pass the extrnsic data through method in flyweight object.
