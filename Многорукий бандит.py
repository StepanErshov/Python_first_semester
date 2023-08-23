#Вы сами не знаете как так вышло, но вы обнаружили себя в зале с игровыми автоматами с целым мешком жетонов
#К сожалению, в кассе жетоны назад принимать отказываются, и вы решили испытать свою удачу.
#В зале есть много автоматов, в которые вы можете играть. Для одной игры с автоматом вы используете один жетон.
#В случае выигрыша автомат даёт вам один доллар, в случае проигрыша — ничего.
#У каждого автомата есть фиксированная вероятность выигрыша (которую вы не знаете), но у разных автоматов она разная.
#Изучив сайт производителя этих автоматов, вы выяснили, что вероятность выигрыша у каждого автомата выбирается случайно
#на этапе изготовления из бета-распределения с определёнными параметрами.
#Вам хочется максимизировать свой ожидаемый выигрыш.

import random
import sys
import time
class SolverFromStdIn(object):
    def __init__(self):
        self.regrets = [0.]
        self.total_win = [0.]
        self.moves = []


class ThompsonSampling(SolverFromStdIn):
    def __init__(self, bandits_total, init_a=1, init_b=1):
        """
        init_a (int): initial value of a in Beta(a, b).
        init_b (int): initial value of b in Beta(a, b).
        """

        SolverFromStdIn.__init__(self)
        self.n = bandits_total

        self.alpha = init_a
        self.beta = init_b

        self._as = [init_a] * self.n  # [random.betavariate(self.alpha, self.beta) for _ in range(self.n)]
        self._bs = [init_b] * self.n  # [random.betavariate(self.alpha, self.beta) for _ in range(self.n)]
        self.last_move = -1
        random.seed(int(time.time()))

    def move(self):
        samples = [random.betavariate(self._as[x], self._bs[x]) for x in range(self.n)]
        self.last_move = max(range(self.n), key=lambda x: samples[x])

        self.moves.append(self.last_move)
        return self.last_move

    def set_reward(self, reward):
        i = self.last_move
        r = reward

        self._as[i] += r
        self._bs[i] += (1 - r)

        return i, r


while True:
    n, m = map(int, sys.stdin.readline().split())

    if n == 0 and m == 0:
        break

    alpha, beta = map(float, sys.stdin.readline().split())
    solver = ThompsonSampling(m)

    for _ in range(n):
        print(sys.stdout, solver.move() + 1)
        sys.stdout.flush()
        reward = int(sys.stdin.readline())
        solver.set_reward(reward)