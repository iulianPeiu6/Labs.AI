import gym
import numpy as np


class Stage(object):
    def __init__(self, start, end, dimension, danger_points):
        self.start = start
        self.current = tuple(list(start))
        self.end = end
        self.dimension = dimension
        self.board = np.zeros((dimension, dimension), dtype=int)
        for danger_point in danger_points:
            self.board[danger_point[0], danger_point[1]] = -1
        self.board[start] = 1
        self.board[end] = 2

    def next(self, direction):
        self.board[self.current] = 0

        new_position = (self.current[0] + direction[0], self.current[1] + direction[1])
        self.current = new_position

        self.board[self.current] = 1

    def show_board(self):
        print(self.board)


if __name__ == '__main__':
    stage = Stage((0, 0), (3, 3), 4, [(1, 1), (1, 3), (2, 3), (3, 0)])
    stage.show_board()
    stage.next((1, 0))
    stage.show_board()
env = gym.make('FrozenLake-v1')
action_size = env.action_space.n
state_size = env.observation_space.n

Q = np.zeros([state_size, action_size])

alpha = .65
gamma = .9
number_of_episodes = 1000
max_steps = 99
rev_list = []
for i in range(number_of_episodes):
    state = env.reset()
    total_reward = 0
    done = False
    j = 0
    while j < max_steps:
        env.render()
        j += 1
        action = np.argmax(Q[state, :] + np.random.randn(1, env.action_space.n) * (1./(i + 1)))
        new_state, reward, done, _ = env.step(action)
        Q[state, action] = Q[state, action] + alpha * (reward + gamma * np.max(Q[new_state, :]) - Q[state, action])
        if done:
            total_reward = 1
            break
        state = new_state
    rev_list.append(total_reward)
    env.render()
    print(f"Reward:{total_reward}")
    print("Final Values Q table")
    print(Q)
