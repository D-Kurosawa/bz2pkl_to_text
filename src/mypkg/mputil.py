"""Multi process utility module"""
import os


class MpCPU:
    """Get number of CPU used by multi process

    :type _cpu: int | str | None
    :type _max_cpu: int
    :type _min_cpu: int
    :type _character_pattern: tuple of str
    """

    def __init__(self, cpu=None):
        """
        :type cpu: int | str | None
        """
        self._cpu = cpu
        self._max_cpu = os.cpu_count()
        self._min_cpu = 1
        self._character_pattern = ('max', 'min', 'mid', 'auto')

    def get(self):
        """
        :rtype int
        """
        if self._cpu is None:
            return self._max_cpu - 1

        if isinstance(self._cpu, int):
            return self._int_process()

        if isinstance(self._cpu, str):
            return self._str_process()

        raise TypeError(f"{type(self._cpu)} : Not int or str")

    def _int_process(self):
        if self._cpu > self._max_cpu:
            return self._max_cpu

        if self._min_cpu > self._cpu:
            return self._min_cpu

        return self._cpu

    def _str_process(self):
        if self._cpu.lower() not in self._character_pattern:
            raise KeyError(f"{self._cpu} not in {self._character_pattern}")

        if self._cpu.lower() == 'max':
            return self._max_cpu

        if self._cpu.lower() == 'min':
            return self._min_cpu

        if self._cpu.lower() == 'mid':
            mid = self._max_cpu // 2
            if self._min_cpu > mid:
                return self._min_cpu
            else:
                return mid

        return self._max_cpu - 1


class MpCounter:
    """Get number of process by multi process

    :type num: int
    """
    _mp_count = 0

    def __init__(self):
        MpCounter.count_up()
        self.num = MpCounter._mp_count

    @classmethod
    def count_up(cls):
        cls._mp_count += 1

    def count_reset(self):
        MpCounter._mp_count = 0
        self.num = 0


class MpLines:
    """Multi process information lines"""

    def __init__(self, process_num, cpu_num, name=None):
        """
        :type process_num: int
        :type cpu_num: int
        :type name: str | None
        """
        self._process = process_num
        self._cpu = cpu_num
        self._name = name

    def top(self):
        print(f"\n{'*' * 60}")
        if self._name is None:
            print(f"<Multi process Start>")
        else:
            print(f"<Multi process [{self._name}] Start>")
        print(f"  Process:{self._process:>5}")
        print(f"  CPU    :{self._cpu:>5}")
        print(f"{'*' * 60}")

    def bottom(self):
        print(f"{'*' * 60}")
        if self._name is None:
            print(f"<Multi process End>")
        else:
            print(f"<Multi process [{self._name}] End>")
        print(f"{'*' * 60}\n")


if __name__ == '__main__':
    pass