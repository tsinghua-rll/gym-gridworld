from gym.envs.registration import register

register(
    id='gridworldRGB-v0',
    entry_point='gym_gridworld.envs:SimpleGridworldRGBEnv',
    reward_threshold=50.0,
)

register(
    id='gridworld-v0',
    entry_point='gym_gridworld.envs:GridworldEnv',
    reward_threshold=50.0,
)

register(
    id='gridworldrandom-v0',
    entry_point='gym_gridworld.envs:GridworldRandomEnv',
    reward_threshold=50.0,
)

register(
    id='simplegridworld-v0',
    entry_point='gym_gridworld.envs:SimpleGridworldEnv',
    reward_threshold=50.0,
)

register(
    id='simplegridworldrandom-v0',
    entry_point='gym_gridworld.envs:SimpleGridworldRandomEnv',
    reward_threshold=50.0,
)
register(
    id='gridworldaa-v0',
    entry_point='gym_gridworld.envs:GridworldAAEnv',
    reward_threshold=50.0,
)
