import argparse
import gym
import gym.spaces
import gym_gridworld
import os
import sys
import termios
import pickle
from itertools import count
import numpy as np

from play import get

parser = argparse.ArgumentParser(description='Save expert trajectory')
parser.add_argument('--tag', default="default", metavar='G')
parser.add_argument('--env-name', default="Hopper-v1", metavar='G',
                    help='name of the environment to run')
parser.add_argument('--max-expert-state-num', type=int, default=50000, metavar='N',
                    help='maximal number of main iterations (default: 50000)')
args = parser.parse_args()

env = gym.make(args.env_name)
env.verbose = True
expert_traj = []


def main_loop():

    num_steps = 0

    for i_episode in count():

        state = env.reset()
        reward_episode = 0
        reward_show_episode = 0

        for t in range(10000):
            action = get()
            if action is None:
                continue
            else:
                next_state, reward, done, opt = env.step(action)
            try:
                tmp = opt['show']
            except:
                opt['show'] = 0
            reward_episode += reward
            reward_show_episode += opt['show']

            num_steps += 1

            expert_traj.append(
                np.hstack([state, action, next_state, reward, done, opt['show']]))

            if done:
                break

            state = next_state

        print('Episode {}\t reward: {:.2f}\t reward_show: {:.2f} \tnum_steps: \
              {}/{}'.format(i_episode, reward_episode, reward_show_episode, num_steps,
                            args.max_expert_state_num))

        if num_steps >= args.max_expert_state_num:
            break


main_loop()
expert_traj = np.stack(expert_traj)
pickle.dump(expert_traj, open('{}_{}_expert_traj.p'.format(args.tag, args.env_name),
            'wb'), protocol=pickle.HIGHEST_PROTOCOL)
