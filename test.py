import gym
import gym_gridworld
import time

env = gym.make('gridworldrandom-v0')

env.verbose=True

for i in range(1000):
    time.sleep(0.5)
    a = env.action_space.sample()
    print(a)
    env.step(a)
    if i % 50 == 0 :
        env.reset()
