import grSimRemote
import rule
import atexit
import time

engine = rule.Rule()

visionPlugin = rule.VisionPlugin("224.5.23.2", 10020, "VisionPlugin")
refereePlugin = rule.RefereePlugin("224.5.23.1", 10003, "RefereePlugin")
navigatorPlugin = rule.UDPNavigatorPlugin(20011, "127.0.0.1", "UDPNavigatorPlugin")
engine.install_plugin(visionPlugin)
engine.install_plugin(refereePlugin)
engine.install_plugin(navigatorPlugin)

engine.start()


def isInZone(position, zone):
    return (position[0] > zone[0] and position[1] > zone[1]
            and
            position[0] < zone[2] and position[1] < zone[3])

def reset():
    grSimRemote.move_to_kickoff()
    time.sleep(0.1)
    engine.grab_vision_frames() # Flush vision frames

game_zone = (-3000, -2000, 3000, 2000)
blue_goal = (-3160, -350, -3000, 350)
yellow_goal = (3000, -350, 3160, 350)

def update_ball():
    vision_frames = engine.grab_vision_frames()
    if vision_frames:
        vision_frame = vision_frames[0]
        ball_position = (vision_frame.balls[0].position.x, vision_frame.balls[0].position.y,
                                vision_frame.balls[0].position.z)

        if isInZone(ball_position, blue_goal):
            return "yellow"
        elif isInZone(ball_position, yellow_goal):
            return "blue"
        elif not isInZone(ball_position, game_zone):
            return "out"

atexit.register(engine.stop)

if __name__ == "__main__":
    while True:  # TODO: Replace with a loop that will stop when the game is over
        result = update_ball()
        if result:
            reset()
