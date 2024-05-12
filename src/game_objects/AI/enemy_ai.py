import math


class EnemyAI:
    def __init__(self, enemy, player):
        self.enemy = enemy
        self.player = player

    def update(self):
        # Calculate direction to the player
        direction_to_player = (self.player.position[0] - self.enemy.position[0],
                               self.player.position[1] - self.enemy.position[1])

        # Calculate rotation angle to face the player
        target_angle = math.atan2(direction_to_player[1], direction_to_player[0])
        angle_diff = target_angle - self.enemy.rotation
        # Adjust angle_diff to be between -pi and pi for smoother rotation
        if angle_diff > math.pi:
            angle_diff -= 2 * math.pi
        elif angle_diff < -math.pi:
            angle_diff += 2 * math.pi

        # Rotate enemy
        rotation_speed = 0.05  # Adjust this value based on your game
        if abs(angle_diff) > rotation_speed:
            rotation_direction = 1 if angle_diff > 0 else -1
            self.enemy.rotation += rotation_speed * rotation_direction
        else:
            self.enemy.rotation = target_angle

        # Shoot at player if within range
        distance_to_player = math.sqrt(direction_to_player[0] ** 2 + direction_to_player[1] ** 2)
        # if aiming in +- 10 degrees of the player shoot
        if abs(angle_diff) < math.radians(10):
            self.enemy.shoot()
