import sympy
import random
def generate_cubic_lifefunction(var,end,start=0,c = 1):
    """
    Docstring for generate_cubic_lifefunction
    
    :param start: Description
    :param end: Description
    """
    temp_end = end-start
    if c != 1:
        raise ValueError("Not yet implemented")
    l_x = 2*(c)*(var**3)/(temp_end**3) - 3*c*(var**2)/(temp_end**2)+c
    l_x = l_x.subs(var,var-start)

    #Error check to see if derivative makes sense

    # print(f'end value is {l_x.subs(var,end)}')
    if l_x.subs(var,end) != 0 or l_x.subs(var,start) != c:
        print(float(l_x.subs(var,start)))
        raise ValueError('End value should be zero')

    
   
    t = sympy.symbols('t')

    test = random.uniform(start,end)
    l_start = l_x.subs(var,test)
    l_x_t = l_x.subs(var,test+t)
    u_x_t = -sympy.diff(sympy.ln(l_x_t))
    pdf_integral = float(sympy.integrate(u_x_t*l_x_t/l_start,(t,0,end-test)))

    if -10**(-5)>= pdf_integral-1 or pdf_integral-1 >= 10**(-5):
        print(pdf_integral)
        raise ValueError("PDF value is not good")
        # print(pdf_integral)

        # print(f'The integral value is {pdf_integral}')


    return l_x

def cont_assurance_EV(pop_end,pop_start,start,end,interest):
    #Need to debug - check with TI to see if integrals are set up correctly!!
    x = sympy.symbols('x')
    l_x = generate_cubic_lifefunction(x,pop_end,pop_start)
    t = sympy.symbols('t')


    l_start = l_x.subs(x,start)
    l_x_t = l_x.subs(x,start+t)
    u_x_t = -sympy.diff(sympy.ln(l_x_t))

    test_integral =  float(sympy.integrate(u_x_t*l_x_t/l_start,(t,0,pop_end - start)))
    if test_integral != 1:
        print(test_integral)
        raise ValueError("Integral should be 1")


    #Error check
    # print(f'The pdf value is {pdf_integral}')

    # print(l_x_t)
    u_x_t = -sympy.diff(sympy.ln(l_x_t))
    l_start = l_x.subs(x,start)
    v_t = (1+interest)**(-1*t)

    # print(l_start)
    # print(u_x_t)
    # print(v_t)

    

    # if pdf_integral !==

    ldash_x_t = sympy.diff(l_x_t)
    res_2 = float(sympy.integrate(-1*ldash_x_t*v_t/l_start,(t,0,end-start)))

    # if 
    # print(f'The alternate  value is {res_2} ')
    

    res = float(sympy.integrate(u_x_t*l_x_t*v_t/l_start,(t,0,end-start)))

    if res != res_2:
        print(res)
        print(res_2)
        raise ValueError("The two values should be equal")

    return res
    pass

if __name__=="__main__":
    x = sympy.symbols('x')
    l_x = (2*10**(-9))*((x)**(3))-(3*10**-6)*((x)**2)+1
    # print(l_x)
    l_x = generate_cubic_lifefunction(x,117,17,1)
    print(l_x)
    # u_x =  -sympy.diff(sympy.ln(l_x))

    # print(u_x)

    # def_integral = sympy.integrate(u_x * l_x,(x,0,117))
    # print(def_integral)


    print(cont_assurance_EV(117,17,50,117,0.04))

    print(cont_assurance_EV(117,17,17,117,0.04))