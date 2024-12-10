# Code without Strategy Pattern

- Child Classes are inheriting drive method from Vehicle class.
- SportsVehicle and OffLoadVechicle have same requirement in drive capability.
  These two child classes have same code in drive method.
- Above two classes require same `Drive Strategy`.
- This causes `Code Duplication` among the two child classes.

## Code with Strategy Pattern

- Create new interface `DriveStrategy` for handling logic for drive strategy.
- Concrete classes `NormalDriveStrategy` and `SportDriveStrategy` implement the `DriveStrategy` interface.
- Implement normal drive logic and sport drive logic in the above concrete classes.
- In Base class `Vehicle` add attribute `strategy` of type `DriveStrategy`.
- Call the drive method of `strategy` object inside the `drive` method of `Vehicle` class
- Now, Child classes can pass the required `DriveStrategy` object to Base class through super constructor to get desired DriveStrategy Logic.

### Additional Info

- We can implement multiple drive strategies by using `DriveInfo`.
