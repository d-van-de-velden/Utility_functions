import sys, getopt
import numpy as np 
import matplotlib.pyplot as plt

def dv_distr_plotter(argv):
# dv_distr_plotter(a=0, b=2, N_vals=30, title='', distr_type='gauss', 
#                    pfname='distribution_plot.png'):
#

    try:
        opts, args = getopt.getopt(argv[1:], "a:b:N:title:d:p",
                                   ["a=", "b=", "N=", "title=", "d="
                                    , "p="])
        print(opts)
        print(args)
    except:
        print('Input variable syntax seems wrong.')
        sys.exit(2)
    
    print('Input variables are: ')
    for opt, arg in opts:
        print(opt)
        if opt in ("-a", "--a"):
            arg_a = arg
            print(arg_a)
        elif opt in ("-b", "--b"):
            arg_b = arg
            print(arg_b)
        elif opt in ("-N", "--N"):
            arg_N_vals = arg
            print(arg_N_vals)
        elif opt in ("-title", "--title"):
            arg_title = arg
            print(arg_title)
        elif opt in ("-d", "--d"):
            arg_distr_type = arg
            print(arg_distr_type)
        elif opt in ("-p", "--p"):
            arg_pfname = arg
            print(arg_pfname)

    # default values
    a          = 0
    b          = 2
    N_vals     = 500
    title      = 'dummy distribution'
    distr_type = 'gauss'
    pfname     = 'dummy_distr_plot'

    if 'arg_a' not in locals(): 
        arg_a = a      # or some other default value.
    else:
        arg_a = float(arg_a)
    
    if 'arg_b' not in locals(): 
        arg_b = b      # or some other default value.
    else:
        arg_b = float(arg_b)
    
    if 'arg_N_vals' not in locals(): 
        arg_N_vals = N_vals      # or some other default value.
    else:
        arg_N_vals = int(arg_N_vals)

    if 'arg_title' not in locals(): 
        arg_title = title      # or some other default value.

    if 'arg_distr_type' not in locals(): 
        arg_distr_type = distr_type      # or some other default value.

    if 'arg_pfname' not in locals(): 
        arg_pfname = pfname      # or some other default value.
 

    print('Distribution plotting funtion')
    if arg_distr_type == 'gauss':
        print('Default or not. You chose the gauss distribution')
        print('Therefore -> ' + 'a=mu : ' + str(arg_a) + 
              ' & b=sigma : ' + str(arg_b))
        distr_data = np.random.normal(arg_a, arg_b, arg_N_vals)
    elif arg_distr_type == 'uniform':
        print('You chose the uniform distribution')
        print('Therefore -> ' + 'a=mu : ' + str(arg_a) +
              ' & b=sigma : ' + str(arg_b))
        distr_data = np.random.uniform(arg_a, arg_b, arg_N_vals)

    elif arg_distr_type == 'lognormal':
        print('Default or not. You chose the lognormal distribution')
        print('Therefore -> ' + 'a=alpha : ' + str(arg_a) +
              ' & b=beta : ' + str(arg_b))
        distr_data = np.random.lognormal(arg_a, arg_b, arg_N_vals)


    plt.cla()
    plt.hist(distr_data, bins=150)
    plt.ylabel('Probability')
    plt.title(arg_title)
    plot_fname = arg_pfname + '.png'
    print(plot_fname)
    plt.savefig(plot_fname, dpi=150)

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    print('Function input: -a: int(), -b: int(), -N=int(), --title=str(), d=str(''gauss''), p=filepath / str()')
    dv_distr_plotter(sys.argv)
