# Assignment 4

## test.py - King.move()

- **test_move_dead**             - checking if dead king move's
- **test_move_on_normal_blank**  - move in all directions on blank spaces
- **test_move_on_normal_spawn**  - move in all directions on spawn spaces
- **test_move_on_buildings**     - move on buildings - shouldn't move
- **test_move_after_boundaries** - move by crossing boundaries (up,down,left,right) - shouldn't move 

## test_bonus.py - King.attack_target()
- **test_attack_target_health_check1** - target.health - wrong inequality check to destroy (or) wrong attack happening
- **test_attack_target_health_check2** - target.health < 0 -> destroy the troop
- **test_attack_target_health_check3** - target.health > 0 -> shouldn't destroy the troop
- **test_attack_target_alive**         - King is dead, check if it still destroys the target.

- for each test function in each class, related test case is explained in the function also