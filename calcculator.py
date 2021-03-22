num_1 = input("please enter the first number : ")
if num_1.strip()=='':
    exit ("error please enter the num_1")
else:
    try : 
        num_a=float(num_1)
    except Exception as e : 
        exit ('num_1 must be a number ')

opt = input("please enter opt : ")
if opt.strip()=='':
    print ("error please enter opt")
elif opt!='+' and opt!='-' and opt!='*' and opt!='/' and opt!='\\' and opt!='^' and opt!='%':
    exit('please enter the valid opt !!!!')

num_2 = input("please enter the second number : ")
if num_2.strip()=='':
    exit ("error please enter the num_2")
else:
    try : 
        num_b=float(num_2)
    except Exception as e : 
        exit ('num_2 must be a number ')   

if opt=="+":
    num_c = num_a + num_b
elif opt=="-":
    num_c = num_a - num_b
elif opt=="*":
    num_c = num_a * num_b
elif opt=="/" or opt=="\\":
    if num_b == 0:
        exit ('division by zero not possible ')
    else:
        num_c = num_a / num_b
elif opt=="%":
    if num_b == 0:
        exit('division by zero not possible ')
    else:
        num_c = num_a % num_b
elif opt=="^":
    num_c = num_a**num_b

print (num_a,opt,num_b,"=",num_c)