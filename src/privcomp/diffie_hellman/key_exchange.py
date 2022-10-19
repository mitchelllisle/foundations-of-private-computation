from random import SystemRandom
from typing import Tuple, Union

from privcomp.crypto_utils import generate_prime_generator_pair
from privcomp.typing import PublicInt, PublicStr, SecretInt


class Party:

    random: SystemRandom = SystemRandom()

    def __init__(self, name: PublicStr, p: PublicInt, g: PublicInt):
        self.name = name
        self.p = p
        self.g = g

        self.a = self.random.randrange(self.p)
        self.A: SecretInt = pow(self.g, self.a, self.p)
        self.secret: Union[SecretInt, None] = None

    def get_B(self, B: int):
        self.secret = pow(B, self.a, self.p)

    def __str__(self) -> str:
        return f'Party: {self.name}\np: {self.p}\ng: {self.g}\na: {self.a}\nA: {self.A}\ns: {self.secret}'


class DiffieHellmanKeyExchange:
    def __init__(self, parties: Tuple[Party, Party]):
        self.p1, self.p2 = parties

    @classmethod
    def generate_prime_generator_pair(cls, size: int = 8) -> Tuple[int, int]:
        return generate_prime_generator_pair(size)

    def exchange(self):
        p1_A = self.p1.A
        p2_A = self.p2.A

        self.p1.get_B(p2_A)
        self.p2.get_B(p1_A)
