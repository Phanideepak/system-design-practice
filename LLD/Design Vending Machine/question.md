# Design Vending Machine

- We have Vending Machine of N rows. Each Row contains a tray that consists of M number of items. Each item is kept in a item self.  Each item has name, code and price. Below are the functionalities of Vending Machine
  --> Vending Machine has `insert cash` feature where user can insert the cash in `insert cash slot`  after clicking on `insert cash button`
  --> Vending Machine has `item selection` feature where user can select product by entering `item code` in keypad. After that, User needs to click `item selection button`.
  --> Vending Machine has `cancel button` for refund
  --> Vending Machine has `Cash Change Tray` option to collect residue change after the purchase.
  --> Vending Machine has `item disperse tray` where user can collect purchased items.

## Happy Flow of Vending Machine

- Initially Vending Machine is in `Idle` state.

- User Clicks on insert cash button then state changes from `Idle` to `Accepting-Cash` or `Has-Money`. Now user can add either coins or cash.
  
- User clicks on `item selection button` then state changes from `Accepting-Cash` to `Item-Selection`. User enters the `item code` in the keypad.

- If inserted money >= items cost, then state changes from `Item-Selection` to `Dispense Item`. User can collect his items. Then state changes from `Dispense Item` to `Idle`.  

### Negative Flow of Vending Machine

- When state of Vending machine is in `Accepting-Cash`, User might cancel the transaction by clicking on `cancel button`. User will get refund and state changes from `Accepting-Cash` to `Idle` state.

- When state of Vending Machine is in `Item-Selection`, User might cancel the transaction by clicking on `cancel button`. User should get refund and state changes from `Item-Selection` to `Idle`.

- When state of Vedning Machine is in `Item-Selection`.  If User's input amount is less than product's amount then User should get refund and State changes from `Item-Selection` to `Idle`.
