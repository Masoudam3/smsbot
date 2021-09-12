from django.db import models



class Login(models.Model):

    user_name = models.CharField(max_length=40, primary_key=True)
    password  = models.CharField(max_length=64)


    def __str__(self):
        return self.user_name





class ChangePassword(models.Model):

    user_name = models.CharField(max_length=30, primary_key=True)
    last_password = models.CharField(max_length=64)
    new_password = models.CharField(max_length=64, null=True, blank=True)



    def __str__(self):
        return self.user_name






class ForgetPassword(models.Model):

    user_name = models.CharField(max_length=64)
    

    def __str__(self):
        return self.user_name






class DeviceTbl(models.Model):

    devicetoken = models.TextField( null=False)
    devicemodel = models.TextField( null=False)
    deviceandroidversion = models.CharField(max_length=200, null=False)
    datetimeregister = models.DateTimeField(null=False)
    datetimeregisterfa = models.CharField(max_length=50, null=False)





class PingDeviceTbl(models.Model):

    iddevice = models.IntegerField(null=False)
    datetimelastonline = models.DateTimeField()
    datetimelastonlinefa = models.CharField(max_length=50)





class Setting(models.Model):

    settingname = models.CharField(max_length=50, null=False)
    settingvalue = models.TextField(null=False)






class SmsInbox(models.Model):

    sendernumber = models.CharField(max_length=50, null=False) 
    smsmessage   = models.TextField(null=False)
    datetimeen   = models.DateTimeField(null=False)
    datetimefa   = models.CharField(max_length=50, null=False)
    iddevice     = models.IntegerField(null=False)
