from gym.envs.registration import register

register(
    id='gridworldRGB-v0',
    entry_point='gym_gridworld.envs:SimpleGridworldRGBEnv',
)

register(
    id='gridworld-v0',
    entry_point='gym_gridworld.envs:GridworldEnv',
)

register(
    id='gridworldrandom-v0',
    entry_point='gym_gridworld.envs:GridworldRandomEnv',
)

register(
    id='simplegridworld-v0',
    entry_point='gym_gridworld.envs:SimpleGridworldEnv',
)

register(
    id='simplegridworldrandom-v0',
    entry_point='gym_gridworld.envs:SimpleGridworldRandomEnv',
)
