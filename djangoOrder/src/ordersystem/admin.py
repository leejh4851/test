from django.contrib import admin
from ordersystem.models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customid','name','tel','postcode','address','detailAddress','extraAddress')
    list_filter = ['customid']
    search_fields = ['customid','name','tel','postcode','address','detailAddress','extraAddress']

class DestinationAdmin(admin.ModelAdmin):
    list_display = ('customid','name','tel','postcode','address','detailAddress','extraAddress')
    list_filter = ['customid']
    search_fields = ['customid','name','tel','postcode','address','detailAddress','extraAddress']
    
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id','goodName','classification','orderUnit','enterprise_id')
    list_filter = ['goodName']
    search_fields = ['goodName','classification','orderUnit','enterprise_id']
    '''
    goodName = models.CharField(max_length=100) 
    classification = models.CharField(max_length=20) #상품분류 ~ 대,중,소, 500cc,1000cc etc 
    orderUnit =  models.CharField(max_length=20) #주문단위 ~ 박스,개, ... 
    enterprise = models.ForeignKey(Enterprise,on_delete=models.CASCADE) #>>>> FK
    '''

class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('id','corporate_reg_no','enterprise_name','industry_code','enterprise_address')
    list_filter = ['enterprise_name']
    search_fields = ['corporate_reg_no','enterprise_name','industry_code','enterprise_address']
    '''
    corporate_reg_no = models.CharField(max_length=50,unique=True,null=False) 
    enterprise_name = models.CharField(max_length=50)
    industry_code = models.CharField(max_length=50)
    enterprise_address = models.CharField(max_length=200)
    '''

class PriceAdmin(admin.ModelAdmin):
    list_display = ('id','goodNo','startDay','endDay','salePrice','saleUnit')
    list_filter = ['goodNo']
    search_fields = ['goodNo','startDay','endDay','salePrice','saleUnit']
    '''
    goodNo = models.ForeignKey(Goods,on_delete=models.CASCADE) #>>>> FK
    startDay = models.DateTimeField()
    endDay = models.DateTimeField()
    salePrice =  models.IntegerField()
    saleUnit = models.CharField(max_length=20) #가격 단위 ~ 개, 박스, 박스 대, 박스 중,....
    '''

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id','orderCode','orderDay','destinationId','goodId','qty')
    list_filter = ['destinationId','goodId','orderCode']
    search_fields = ['id','orderCode','orderDay','destinationId','goodId','qty']
    '''
    class Meta:
        unique_together = (('orderCode','id'),)
        
    orderCode = models.CharField(max_length=20) 
    orderDay = models.DateTimeField(auto_now_add=True, blank=True)
    destinationId = models.ForeignKey(Destination,on_delete=models.CASCADE) #>>>> FK
    goodId = models.ForeignKey(Goods,on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    '''

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Destination,DestinationAdmin)
admin.site.register(Enterprise,EnterpriseAdmin)
admin.site.register(Goods,GoodsAdmin)
admin.site.register(Price,PriceAdmin)
admin.site.register(Orders,OrdersAdmin)
