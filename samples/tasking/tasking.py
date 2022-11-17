import dace
import numpy as np


N = dace.symbol('N')


@dace.program
def function(A: dace.int32[N, N]):
    return A.T

@dace.program(use_tasking=True)
def function2(A: dace.int32[N, N]):
    return A.T



if __name__ == "__main__":
    n = 10
    A = np.random.randint(100, size=(n, n), dtype=np.int32)

    ## First method using activate_tasking() on the sdfg 
    sdfg = function.to_sdfg()
    sdfg.activate_tasking()
    B = sdfg(A=A, N=np.int32(n))
    print(A)
    print()
    print(B)
    print()


    ## Second method using the argument use_tasking=True in to_sdfg()
    sdfg = function.to_sdfg(use_tasking=True)
    B = sdfg(A=A, N=np.int32(n))
    print(B)
    print()
    
    ## Third method using use_tasking=True in the decorator.
    csdfg = function2.compile()
    B = csdfg(A=A, N=np.int32(n))
    print(B)
