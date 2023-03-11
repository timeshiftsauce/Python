while True:
    user_weight = float(input("体重kg"))
    user_height = float(input("身高m"))
    user_BMI = user_weight / user_height ** 2
    if(user_BMI<=18.5):
        print("瘦")
    elif 18.5<user_BMI<=25:
        print("正常")
    elif 25 <user_BMI<=30:
        print("偏胖")
    else:
        print("bigger")
    print("您的BMI值为：" + str(user_BMI) + str(1==1 and 6==7))