import os
import random
import django

django.setup()
from django.core.files import File
from ecommerce.models import Product, Image

# get a list of image file paths in the images folder
image_folder = '/path/to/images/folder/'
image_paths = [os.path.join(image_folder, f)
               for f in os.listdir(image_folder) if f.endswith('.jpg')]

# specify the number of products to create
num_products = 10

# create the products and images
for i in range(num_products):
    # create a product
    product = Product(name='Product {}'.format(i+1),
                      price=random.randint(10, 50))
    product.save()

    # create an image for the product for each image file
    for image_path in image_paths:
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                # generate random data for the image
                poster = random.choice([True, False])
                image = Image(product=product, poster=poster)
                image.image.save(os.path.basename(
                    image_path), File(f), save=True)
