# Design Parking Lot

- Vehicle enters the gate and takes the ticket for parking. Car owner parks his vehicle in parking spot. While exiting, car owner pays parking charges. There can be M entrances and N exits.

## Requirement Clarification

- How many entrances are there for vehicle to enter? (1 entrance and 1 exit)
- What are the different types of parking spot ?
  -> Two Wheeler
  -> Four Wheeler
  -> Three Wheeler (should be extensibile)
- Payment Strategy : Hour based charge or minute based charge
- Optimise the find_parking_space function to find the nearest parking space from the gate where vehicle entered.
- Are there any parking floor ? (No)

### Listing out objects

- Vehicle
  -> vehicle no
  -> vehicle type (2 wheeler, 4 wheeler)
- Ticket
  -> entry time
  -> parking spot
- Entrance Gate
  -> find_parking_space()
  -> update_parking_space()
  -> generate_ticket()
- Parking Spot
  -> id
  -> is_empty
  -> vehicle
  -> price
- Exit Gate
  -> calculate_cost()
  -> proceed_payment()
  -> update_parking_spot
