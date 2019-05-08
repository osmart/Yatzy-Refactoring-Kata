from collections import Counter


class Yatzy:
    """
    Class to score Yatzy simple dice game. This class interface
    is deprecated and will be dropped in a future release. Please
    update to use the YatzyClean class.

    See https://github.com/emilybache/Yatzy-Refactoring-Kata
    """

    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [d1, d2, d3, d4, d5]

    @staticmethod
    def ones(d1,  d2,  d3,  d4,  d5):
        """ returns the sum of dice that are 1 """
        return YatzyClean([d1, d2, d3, d4, d5]).ones

    @staticmethod
    def twos(d1,  d2,  d3,  d4,  d5):
        """ returns the sum of dice that are 2 """
        return YatzyClean([d1, d2, d3, d4, d5]).twos

    @staticmethod
    def threes(d1,  d2,  d3,  d4,  d5):
        """ returns the sum of dice that are 3 """
        return YatzyClean([d1, d2, d3, d4, d5]).threes

    def fours(self):
        """ returns the sum of dice that are 4 """
        return YatzyClean(self.dice).fours

    def fives(self):
        """ returns the sum of dice that are 5 """
        return YatzyClean(self.dice).fives

    def sixes(self):
        """ returns the sum of dice that are 6 """
        return YatzyClean(self.dice).sixes

    @staticmethod
    def chance(d1, d2, d3, d4, d5):
        """
        In chance the player scores the sum of all dice,
        no matter what they read.
        """
        return YatzyClean([d1, d2, d3, d4, d5]).chance

    @staticmethod
    def yatzy(dice):
        """
        If all dice have the same number, the player scores 50 points.
        """
        return YatzyClean(dice).yatzy

    @staticmethod
    def score_pair(d1,  d2,  d3,  d4,  d5):
        """
        The player scores the sum of the two highest matching dice.
        """
        return YatzyClean([d1, d2, d3, d4, d5]).pair

    @staticmethod
    def two_pair(d1,  d2,  d3,  d4,  d5):
        """
        If there are two pairs of dice with the same number,
        the player scores the sum of these dice.
        """
        return YatzyClean([d1, d2, d3, d4, d5]).two_pair

    @staticmethod
    def four_of_a_kind(d1,  d2,  d3,  d4,  d5):
        """
        If there are four dice with the same number,
        the player scores the sum of these dice.
        """
        return YatzyClean([d1, d2, d3, d4, d5]).four_of_a_kind

    @staticmethod
    def three_of_a_kind(d1,  d2,  d3,  d4,  d5):
        """
        If there are three dice with the same number,
        the player scores the sum of these dice.
        """
        return YatzyClean([d1, d2, d3, d4, d5]).three_of_a_kind

    @staticmethod
    def smallStraight(d1,  d2,  d3,  d4,  d5):
        """
        When placed on "small straight", if the dice read
        1,2,3,4,5,
        the player scores 15 (the sum of all the dice).
        """
        return YatzyClean([d1, d2, d3, d4, d5]).small_straight

    @staticmethod
    def largeStraight(d1,  d2,  d3,  d4,  d5):
        """
        When placed on "large straight", if the dice read
        2,3,4,5,6,
        the player scores 20 (the sum of all the dice).
        """
        return YatzyClean([d1, d2, d3, d4, d5]).large_straight

    @staticmethod
    def fullHouse(d1,  d2,  d3,  d4,  d5):
        """
        If the dice are two of a kind and three of a kind,
        the player scores the sum of all the dice.
        """
        return YatzyClean([d1, d2, d3, d4, d5]).full_house


class YatzyClean(object):
    """
    Class to score Yatzy simple dice game. This is a clean
    reimplementation that will ultimately replace the
    original Yatzy class above.

    See https://github.com/emilybache/Yatzy-Refactoring-Kata
    """
    def __init__(self, dice):
        self.dice = dice

    @property
    def chance(self):
        """
        In chance the player scores the sum of all dice,
        no matter what they read.
        """
        return sum([d for d in self.dice])

    @property
    def yatzy(self):
        """
        If all dice have the same number, the player scores 50 points.
        """
        if len(Counter(self.dice)) == 1:
            return 50
        else:
            return 0

    @property
    def ones(self):
        """ returns the sum of dice that are 1 """
        return self.__numbers(1)

    @property
    def twos(self):
        """ returns the sum of dice that are 2 """
        return self.__numbers(2)

    @property
    def threes(self):
        """ returns the sum of dice that are 3 """
        return self.__numbers(3)

    @property
    def fours(self):
        """ returns the sum of dice that are 4 """
        return self.__numbers(4)

    @property
    def fives(self):
        """ returns the sum of dice that are 5 """
        return self.__numbers(5)

    @property
    def sixes(self):
        """ returns the sum of dice that are 6 """
        return self.__numbers(6)

    @property
    def pair(self):
        """ scores the sum of the two highest matching dice. """
        counts = Counter(self.dice)
        for d in 6, 5, 4, 3, 2, 1:
            if counts[d] >= 2:
                return 2*d
        return 0

    @property
    def two_pair(self):
        """
        If there are two pairs of dice with the same number,
        the player scores the sum of these dice.
        """
        counts = Counter(self.dice)
        pair = []
        for d in 6, 5, 4, 3, 2, 1:
            if counts[d] >= 2:
                pair.append(d)
        if len(pair) == 2:
            return 2*sum(pair)
        else:
            return 0

    @property
    def four_of_a_kind(self):
        """
        If there are four dice with the same number,
        the player scores the sum of these dice.
        """
        return self.__of_a_kind(4)

    @property
    def three_of_a_kind(self):
        """
        If there are four dice with the same number,
        the player scores the sum of these dice.
        """
        return self.__of_a_kind(3)

    @property
    def small_straight(self):
        """
        When placed on "small straight", if the dice read
        1,2,3,4,5,
        the player scores 15 (the sum of all the dice).
        """
        if sorted(self.dice) == [1, 2, 3, 4, 5]:
            return 15
        else:
            return 0

    @property
    def large_straight(self):
        """
        When placed on "large straight", if the dice read
        2,3,4,5,6,
        the player scores 20 (the sum of all the dice).
        """
        if sorted(self.dice) == [2, 3, 4, 5, 6]:
            return 20
        else:
            return 0

    @property
    def full_house(self):
        """
        If the dice are two of a kind and three of a kind,
        the player scores the sum of all the dice.
        """
        counts = Counter(self.dice)
        most_common_two = counts.most_common(2)
        if most_common_two[0][1] == 3 and most_common_two[1][1] == 2:
            return self.chance
        else:
            return 0

    def __of_a_kind(self, n_kind):
        """
        returns the number of nkind, where n_kind is 3 or 4.
        """
        counts = Counter(self.dice)
        pips, count = counts.most_common(1)[0]
        if count >= n_kind:
            return n_kind*pips
        else:
            return 0

    def __numbers(self, number):
        """ returns the of the dice that match the number """
        return sum([d for d in self.dice if d == number])
