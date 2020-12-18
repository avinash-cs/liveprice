from django.db import models 
from taggit.managers import TaggableManager

STATUS_CHOICE = (
    ('Yes', 'In Stock'),
    ('No', 'Out of Stock'),
)

CATEGORIES = (
    ('Electronics', 'Electronics'),
    ('Fashion', 'Fashion'),
    ('Furniture', 'Furniture'),
    ('Toys & Baby', 'Toys & Baby'),
    ('Beauty', 'Beauty'),
    ('Sports & Exercise', 'Sports & Exercise'),
    ('Grocery', 'Grocery'),

)
class ProductInfo(models.Model):
   product_name= models.CharField(max_length=300)
   product_url=models.URLField()
   product_img=models.URLField()
   product_price=models.CharField(max_length=100)
   product_seller=models.CharField(max_length=100)

   def __str__(self):
            return str(self.product_name)

class ProductDetail(models.Model):
    product_name = models.CharField(max_length=100)
    product_image = models.URLField(max_length=3000)
    product_categories = models.CharField(max_length=60, choices=CATEGORIES)
    url = models.URLField()
    seller_name = models.CharField(max_length=60, blank=True)
    in_stock = models.CharField(max_length=20, choices=STATUS_CHOICE)
    product_id = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=7, blank=True, default=0)
    product_color = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    tags = TaggableManager()

    quotedate = models.DateField(blank=True, null=True)

    def __str__(self):
            return str(self.product_name)
