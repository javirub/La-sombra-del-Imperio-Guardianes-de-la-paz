import math
import pygame


class EnemyAI:
    def update(self, enemy, player, max_speed):
        # Calculate distance to the player
        direction_to_player = (player.rect.x - enemy.rect.x,
                               player.rect.y - enemy.rect.y)

        # Calculate rotation angle to face the player
        target_angle = math.atan2(direction_to_player[1], -direction_to_player[0])
        target_angle_deg = math.degrees(target_angle)

        # Normalize the target angle to be in the range of 0 to 360 degrees
        if target_angle_deg < 0:
            target_angle_deg += 360

        # Normalize the enemy angle to be in the range of 0 to 360 degrees
        if enemy.angle >= 360:
            enemy.angle -= 360
        elif enemy.angle < 0:
            enemy.angle += 360

        # Calculate the difference between the target angle and the enemy angle
        angle_diff = target_angle_deg - enemy.angle

        # Normalize the angle difference to be in the range of -180 to 180 degrees
        if angle_diff > 180:
            angle_diff -= 360
        elif angle_diff < -180:
            angle_diff += 360

        # Rotate enemy in the shortest direction
        if angle_diff > 0:
            enemy.rotate(0.5)
        elif angle_diff < 0:
            enemy.rotate(-0.5)

        # if aiming in +- 10 degrees of the player shoot
        if abs(angle_diff) < 10:
            enemy.shoot(pygame.time.get_ticks())

        # Accelerate until max speed
        if enemy.speed < max_speed:
            enemy.increase_speed()
