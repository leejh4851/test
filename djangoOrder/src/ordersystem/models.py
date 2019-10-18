from django.db import models
from astropy.table.operations import unique
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Customer(models.Model):
    customid = models.ForeignKey(User,on_delete=models.CASCADE) #>>>> FK
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=50,null=True, blank=True)
    postcode = models.CharField(max_length=5)
    address = models.CharField(max_length=200)
    detailAddress = models.CharField(max_length=200,null=True, blank=True)
    extraAddress = models.CharField(max_length=200,null=True, blank=True)
        
    def __str__(self):
        return self.name;
        
class Destination(models.Model):#수신처등록
    
    customid = models.CharField(max_length=50) #Customer 와 유사하나 이 부분이 틀림 포린키가 아니고 여러개 배송처 등록가능
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=50,null=True, blank=True)
    postcode = models.CharField(max_length=5)
    address = models.CharField(max_length=200)
    detailAddress = models.CharField(max_length=200,null=True, blank=True)
    extraAddress = models.CharField(max_length=200,null=True, blank=True)
        
    def __str__(self):       
        return self.customid+":"+self.name;

class Enterprise(models.Model):#업체정보  - /업체번호/사업자등록번호,업체명,업종코드,주소 
    corporate_reg_no = models.CharField(max_length=50,unique=True,null=False) 
    enterprise_name = models.CharField(max_length=50)
    industry_code = models.CharField(max_length=50)
    enterprise_address = models.CharField(max_length=200)
    
    def __str__(self):       
        return self.enterprise_name;

    
class Goods(models.Model):#상품정보 -/상품번호/상품명,상품분류,주문단위,판매업체번호 (FK)
    
    goodName = models.CharField(max_length=100) 
    classification = models.CharField(max_length=20) #상품분류 ~ 대,중,소, 500cc,1000cc etc 
    orderUnit =  models.CharField(max_length=20) #주문단위 ~ 박스,개, ... 
    enterprise_id = models.ForeignKey(Enterprise,on_delete=models.CASCADE) #>>>> FK
    
    def __str__(self):       
        return self.goodName;
 
    
class Orders(models.Model):#주문정보 -/주문번호,일련번호/주문일시,고객번호(FK),상품번호(FK),주문수량
    class Meta:
        unique_together = (('orderCode','id'),)
        
    orderCode = models.CharField(max_length=20) 
    orderDay = models.DateTimeField(auto_now_add=True, blank=True)
    destinationId = models.ForeignKey(Destination,on_delete=models.CASCADE) #>>>> FK
    goodId = models.ForeignKey(Goods,on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    
    def __str__(self):       
        return self.orderCode +':'+str(id);


class Price(models.Model):#가격정보 - /상품번호(FK),적용시작일,적용종료일/,가격,단위 
    class Meta:
        unique_together = (('goodNo','startDay','endDay'),)
        
    goodNo = models.ForeignKey(Goods,on_delete=models.CASCADE) #>>>> FK
    startDay = models.DateTimeField()
    endDay = models.DateTimeField()
    salePrice =  models.IntegerField(default=0)
    saleUnit = models.CharField(max_length=20) #가격 단위 ~ 개, 박스, 박스 대, 박스 중,....
 
    def __str__(self):     
        #dt1 =  datetime.strptime(str(self.startDay,''))
        #dt2 =  datetime.strptime(str(self.endDay,''))
        return '상품번호:'+str(self.goodNo) # +':'+dt1+'~'+dt2
