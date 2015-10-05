def main():
    import random
    start=1
    end=1000
    x=random.randint(1,1000)
    number=eval(input('請從1~1000（不含）之中輸入一個整數：'))

    #錯誤外迴圈
    while 1>=number or number>=1000 or round(number)!=number:               ##一開始就輸入錯誤，小於1、大於1000或不是整數
        print('\n你輸入的不是範圍內的整數喔！\n1 ~ 1000')                                            
        number=eval(input('請再輸入一次：'))
        if 0<number<1000 and round(number)==number:                         ##一旦輸入正確（0到1000 且 是整數）
            break                                                           ##就脫離while迴圈
        
    #主迴圈
    while 0<number<1000:
        
        if number==x:                                                       ##答對
            print('\ncongrats!\n')
            break
        
        elif start<number<x and round(number)==number:                      ##number比x小，number變成初值
            start=number
            print('\n',start,' ~ ',end,sep='')
            number=eval(input('輸入：'))
            
            #錯誤內迴圈1
            while number<=start or number>=end or round(number)!=number:
                print('\n你輸入的不是範圍內的整數喔！\n',start,' ~ ',end,sep='')
                number=eval(input('請再輸入一次：'))
                if start<number<end and round(number)==number:              ##為了要符合主迴圈所訂定的條件而設
                    break
            
            
        elif end>number>x and round(number)==number:                        ##number比x大，number變成末值
            end=number
            print()
            print('\n',start,' ~ ',end,sep='')
            number=eval(input('輸入：'))
            
            #錯誤內迴圈2
            while number<=start or number>=end or round(number)!=number:
                print('\n你輸入的不是範圍內的整數喔！\n',start,' ~ ',end,sep='')
                number=eval(input('請再輸入一次：'))
                if start<number<end and round(number)==number:               ##為了要符合主迴圈所訂定的條件而設
                    break
            
        else:
            #錯誤內迴圈3，是否為多餘？
            while number<=start or number>=end or round(number)!=number:
                print('error內3\n',start,'~',end)
                number=eval(input('input again:'))
                if start<number<end:                                        ##為了要符合主迴圈所訂定的條件而設
                    break

            
            
    
main()
    
