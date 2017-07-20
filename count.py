#coding:utf-8
'''
//评测题目:
两辆火车相向而行，速度分别是Va,Vb,+初始距离是S，
另外一个小球和火车A在一个点上，以Vc速度向火车B运动，Vc>Va,+Vc>Vb。
小球遇到火车B后折返，遇到火车A后再折返，就这样在两火车间反复运动，直到两火车相遇。
求解：从初始到两火车相遇时，小球折返的次数。


距离 >> S
火车A >> Va
火车B >> Vb
小球  >> Vc

S/(va+vb) = time

小球运动的路长 = vc*time

第一次小球折返时间 t1 = (s-t0*vb)/(vb+vc)
第二次小球折返时间 t2 = (s-t0*vb-t1*va)/(va+vc)
第二次小球折返时间 t3 = (s-t0*vb-t1*va-t2*vb)/(va+vc)
t1+tx = time
'''


class Count:
    def __init__(self, va, vb, vc, s):
        self.flag = 0
        self.va = float(va)
        self.vb = float(vb)
        self.vc = float(vc)
        self.return_a_speed = self.vb + self.vc
        self.return_b_speed = self.va + self.vc
        self.total_distance = float(s)
        self.total_time = s / (va + vb)

    def func(self):
        if self.flag % 2 == 0 and self.total_time > 0:
            release_time = (self.total_distance / self.return_b_speed)
            self.total_time = self.total_time - release_time
            self.total_distance -= release_time * self.va
            self.flag += 1
            self.func()
        else:
            if self.total_time > 0:
                release_time = (self.total_distance / self.return_a_speed)
                self.total_time = self.total_time - release_time
                self.total_distance -= release_time * self.vb
                self.flag += 1
                self.func()
        return self.flag


if __name__ == '__main__':
    test = Count(20, 30, 300, 10000)
    print test.func()


















