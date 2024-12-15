# Design Elevator System

- There is multi floor building with n floors. There is an user on ith floor of the building. There is a Lift. Outside the Lift, there is an external button that contains upward and downward buttons.

## Clarifying requirements

- How many lifts are there in the building ? m lifts
- Life dispatch Algorithm: This algorithm decides which lift reaches the customer at ith-floor.
   -- odd, even (one lift serves odd floors and other lift serves even floors)
   -- fixed
   -- minimum seek time

### List of objects

- Building
- Floor
- ExternalButton
- ElevatorCar
   -> Display
   -> current_floor : Floor
   -> direction (UP or DOWN)
   -> status (MOVING or IDLE)
   -> internal_button : InternalButton
   -> doors : Doors
- Display
- InternalButton
- Doors