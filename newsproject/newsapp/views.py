from django.shortcuts import render
def index(request):
    return render(request,'newsapp/index.html')
def moviesinfo(request):
    head_msg="Latest Movie Information"
    msg1="Samantha slowly getting cured"
    msg2="Prabhas going to marriage soon"
    msg3="Narendra Modi is prime minister of India"
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news1.html',context=my_dict)
def sportsinfo(request):
    head_msg="Latest Sports Information"
    msg1 = "Police return a silver medal stolen from Mohamed Salah's home in Cairo. ... "
    msg2 = "NBA suspends Trey Lyles, fines Brook Lopez as temper flares on court."
    msg3 = "FIH Pro League: India beat Australia in penalty shootout in second leg. ... "
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3}
    return render(request, 'newsapp/news2.html', context=my_dict)
def politicsinfo(request):
    head_msg="Latest Politics Information"
    msg1 = "Another Proof Of Govt In Panic': Congress Responds To Delhi Police Notice To Rahul Gandhi"
    msg2 = "Telangana Fire: 4 Women Among 6 Killed In Massive Fire At Commercial Complex In Secunderabad"
    msg3 = "Amazon Sale 2023 On LG ACs: Save Up To 50% On Best AC Brand "
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3}
    return render(request, 'newsapp/news3.html', context=my_dict)
# Create your views here.
