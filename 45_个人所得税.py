yingnashui = float (yingnashui) - 3500
def shui(x):         #阶梯纳税表
    if x < 1500:
        return x * 0.03
    elif x <= 0:
        return 'Error'
    elif (x>1500 and x<=4500):
        return (x*0.10 - 105)
    elif x>4500 and x<=9000:
        return (x*0.20 - 555)
    elif x>9000 and x<=35000:
        return (x*0.25 - 1005)
    elif x>3500 and x<=55000:
        return (x*0.3 - 2755)
    elif x>55000 and x<=80000:
        return(x*0.35 - 5505)
    elif x>80000:
        return (x*0.45 - 13505)
 
tax = shui(yingnashui)
 
 
print("税额共计：%.2f"   %tax)
 
result = yingnashui - shui(yingnashui) +3500
 
print ("税后剩余：%.2f"  %result)
