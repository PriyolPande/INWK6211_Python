def my_sum(a,b):
    return(a+b)
def do_twice(f,a,b):
    f(a,b)
    f(a,b)
do_twice(my_sum,5,7)