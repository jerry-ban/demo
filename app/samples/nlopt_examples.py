
import numpy as np
import nlopt
import logging

class nlopt_examples_dummy :
    def __init__(self):
        self.status = -999
        self.dummy_result = [{"optId": 1, "title": "official example", "type": "no linear optimization"},
                  {"optId": 2, "title": "time-consuming example", "type": "custom examples"},
                  {"optId": 3, "title": "time-consuming example with queue", "type": "custom examples"}
                  ]
        pass

    def get_all_examples(self):
        return self.dummy_result

    def run_offcial_example(self):
        return self.dummy_result

    def run_simple_example(self):
        return self.dummy_result

    def run_very_long_example(self):
        return self.dummy_result

class nlopt_examples:
    def __init__(self):
        self.status = -999
        pass

    def get_all_examples(self):
        result = [{"optId": 1, "title": "official example", "type": "no linear optimization"},
                  {"optId": 2, "title": "time-consuming example", "type": "custom examples"},
                  {"optId": 3, "title": "time-consuming example with queue", "type": "custom examples"}
                  ]
        return result
########### example from author   ##############
###
###     min: sqre(x_2)
###     st: x2>=0, x_2 >= (a_1*x_1+b_1)**3, x_2 >=(a_2*x_1+b_2)**3
###     a: [2,-1];  b: [0,1]
#######################################
    def run_offcial_example(self):
        opt = nlopt.opt(nlopt.LD_MMA, 2)
        opt.set_lower_bounds([-float('inf'), 0])
        opt.set_min_objective(self._official_myfunc)
        opt.add_inequality_constraint(lambda x, grad: self._official_myconstraint(x, grad, 2, 0), 1e-8)
        opt.add_inequality_constraint(lambda x, grad: self._official_myconstraint(x, grad, -1, 1), 1e-8)
        opt.set_xtol_rel(1e-4)
        print("\noptimization starts!")
        x = opt.optimize([1.234, 5.678])
        print("\noptimization finished!\n")
        minf = opt.last_optimum_value()
        status=opt.last_optimize_result()
        print("optimum at ", x[0], x[1])
        print("minimum value = ", minf)
        print("result code = ", status)
        result = {"variableList": [{"id": 0, "name": "x1", "value": x[0] }, {"id": 1, "name": "x2", "value": x[1] }]
                  , "objectiveValue": minf, "optStatusCode": status }
        return result

    def _official_myfunc(self, x, grad):
        if grad.size > 0:
            grad[0] = 0.0
            grad[1] = 0.5 / pow(x[1], 0.5)
        print(".")
        return pow(x[1], 0.5)

    def _official_myconstraint(self, x, grad, a, b):
        if grad.size > 0:
            grad[0] = 3 * a * (a * x[0] + b) ** 2
            grad[1] = -1.0
        return (a * x[0] + b) ** 3 - x[1]


####### my dummy example   ##############
    def run_simple_example(self):
        # print ('nlopt version='+nlopt.__version__)
        n = 4
        lb = np.array([40., 50., 30e3, 1.])
        ub = np.array([60., 60., 40e3, 10.])
        x = (lb + ub) / 2.

        opt = nlopt.opt(nlopt.LN_COBYLA, n)
        opt.set_min_objective(self._simple_func)
        opt.set_lower_bounds(lb)
        opt.set_upper_bounds(ub)
        opt.set_xtol_rel(1e-3)
        opt.set_ftol_rel(1e-3)
        xopt = opt.optimize(x)

        opt_val = opt.last_optimum_value()
        status = opt.last_optimize_result()
        logging.info('opt_status = ' + str(status))
        logging.info('optimizer=' + str(xopt))
        logging.info('opt_val=' + str(opt_val))
        return 'opt_status = ' + str(status)

    def _simple_func(self, x, grad):
        F=x[0]
        L=x[1]
        E=x[2]
        I=x[3]
        D=F*L**3/(3.*E*I)
        return D

####### my dummy time-consuming example   ##############
    def run_very_long_example(self):
        counter1 = 1
        counter2 = 1

        return x

