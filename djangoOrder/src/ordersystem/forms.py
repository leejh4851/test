from django.forms import ModelForm
from ordersystem.models import *
class Form(ModelForm):
    class Meta:
        model = Destination
        '''
        customid = models.CharField(max_length=50)
        name = models.CharField(max_length=50)
        tel = models.CharField(max_length=50)
        postcode = models.CharField(max_length=5)
        address = models.CharField(max_length=200)
        detailAddress = models.CharField(max_length=200)
        extraAddress = models.CharField(max_length=200)
        '''
        fields =['customid','name','tel','postcode','address','detailAddress','extraAddress']
        
class OrderForm(ModelForm):
    class Meta:
        model = Orders
        '''
        orderCode = models.CharField(max_length=20) 
        orderDay = models.DateTimeField(auto_now_add=True)
        destinationId = models.ForeignKey(Destination,on_delete=models.CASCADE) #>>>> FK
        goodId = models.ForeignKey(Goods,on_delete=models.CASCADE)
        '''
        fields=['orderCode','destinationId','goodId','qty']