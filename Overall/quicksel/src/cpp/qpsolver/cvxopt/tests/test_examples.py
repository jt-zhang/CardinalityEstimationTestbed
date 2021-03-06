import os
import unittest


class TestExamples(unittest.TestCase):

    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.expath = os.path.normpath(dir_path + "/../examples")

    def exec_example(self, example):
        fname = os.path.join(self.expath, example)
        gdict = dict()
        with open(fname) as f:
            code = compile(f.read(), fname, 'exec')
            exec(code, gdict)
        return gdict

    def assertAlmostEqualLists(self, L1, L2, places=7):
        self.assertEqual(len(L1), len(L2))
        for u, v in zip(L1, L2): self.assertAlmostEqual(u, v, places)

    ## examples/doc/chap8 scripts

    def test_ch8_conelp(self):
        gdict = self.exec_example('doc/chap8/conelp.py')
        self.assertTrue(gdict['sol']['status'] is 'optimal')

    def test_ch8_coneqp(self):
        gdict = self.exec_example('doc/chap8/coneqp.py')
        self.assertAlmostEqualLists(gdict['x'], [0.72558319, 0.61806264, 0.30253528], 5)

    def test_ch8_lp(self):
        gdict = self.exec_example('doc/chap8/lp.py')
        self.assertTrue(gdict['sol']['status'] is 'optimal')
        self.assertAlmostEqualLists(list(gdict['sol']['x']), [1.0, 1.0], 5)

    def test_ch8_socp(self):
        gdict = self.exec_example('doc/chap8/socp.py')
        self.assertTrue(gdict['sol']['status'] is 'optimal')

    def test_ch8_sdp(self):
        gdict = self.exec_example('doc/chap8/sdp.py')
        self.assertTrue(gdict['sol']['status'] is 'optimal')

    def test_ch8_mcsdp(self):
        gdict = self.exec_example('doc/chap8/mcsdp.py')
        n = gdict['n']
        z = +gdict['z']
        self.assertAlmostEqualLists(list(z[::n + 1]), n * [1.0], 5)

    def test_ch8_l1(self):
        gdict = self.exec_example('doc/chap8/l1.py')
        P, x, y = gdict['P'], gdict['x'], gdict['y']
        self.assertAlmostEqualLists(list(P.T * y), P.size[1] * [0.0], 5)

    def test_ch8_l1regls(self):
        gdict = self.exec_example('doc/chap8/l1regls.py')

    ## examples/doc/chap9 scripts

    def test_ch9_gp(self):
        gdict = self.exec_example('doc/chap9/gp.py')

    def test_ch9_acent(self):
        gdict = self.exec_example('doc/chap9/acent.py')

    def test_ch9_acent2(self):
        gdict = self.exec_example('doc/chap9/acent2.py')

    def test_ch9_l2ac(self):
        gdict = self.exec_example('doc/chap9/l2ac.py')

    ## examples/doc/chap10 scripts

    def test_ch10_lp(self):
        gdict = self.exec_example('doc/chap10/lp.py')

    def test_ch10_acent2(self):
        gdict = self.exec_example('doc/chap10/roblp.py')

    def test_ch10_l2ac(self):
        gdict = self.exec_example('doc/chap10/l1svc.py')

    ## ML book examples
    def test_l1(self):
        from cvxopt import normal, setseed
        import l1
        setseed(100)
        m, n = 500, 250
        P = normal(m, n)
        q = normal(m, 1)
        u1 = l1.l1(P, q)
        u2 = l1.l1blas(P, q)
        self.assertAlmostEqualLists(list(u1), list(u2), places=3)

    def test_l1regls(self):
        from cvxopt import normal, setseed
        import l1regls
        setseed(100)
        m, n = 250, 500
        A = normal(m, n)
        b = normal(m, 1)

        x = l1regls.l1regls(A, b)
        # Check optimality conditions (list should be empty, e.g., False)
        self.assertFalse([t for t in zip(A.T * (A * x - b), x) if abs(t[1]) > 1e-6 and abs(t[0]) > 1.0])


if __name__ == '__main__':
    unittest.main()
