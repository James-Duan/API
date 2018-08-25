# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-7-25 16:14
# @File     : method_loop.py
from threading import Timer


class LoopTimer(Timer):

    def __init__(self, interval, function, args=None, kwargs=None):
        Timer.__init__(self, interval, function, args, kwargs)

    def run(self):
        while True:
            self.finished.wait(self.interval)
            if self.finished.is_set():
                self.finished.set()
                break
            self.function(*self.args, **self.kwargs)

    def cancel(self):
        self.finished.set()


if __name__ == '__main__':
    # t = LoopTimer(1, a)
    # t.start()
    pass