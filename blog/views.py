from django.shortcuts import render 




def Index(request):
    
    return render(request, 'blog/index.html', context={'data':'data'})





def MobilePhone(request):

    return render(request, 'blog/mobile-table.html', context={'data':'data'})






def InboxTable(request):
    
    return render(request, 'blog/inbox-table.html', context={'data':'data'})




def ChangePassword(request):
    
    return render(request, 'blog/change-password.html', context={'data':'data'})



def SendSms(request):
    
    return render(request, 'blog/send-sms.html', context={'data':'data'})



def Login(request):
    
    return render(request, 'blog/login.html', context={'data':'data'})




def ChangeLink(request):
    
    return render(request, 'blog/change-link.html', context={'data':'data'})
