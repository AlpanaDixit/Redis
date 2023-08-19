from django.shortcuts import render, redirect
from django.core.cache import cache
from .models import User, Product

# Partial Caching 
def user_profile(request, user_id):
    user = User.objects.get(user_id=user_id)

    print(user)
    # Caching name and photo for 1 day
    cache.set(f'user_name_{user_id}', user.name, 86400)  # 1 day in seconds
    cache.set(f'user_photo_{user_id}', user.last_name, 86400)  # 1 day in seconds

    return render(request, 'profile.html', {'user': user})

# Full Caching 
def product_details(request, product_id):
    product = Product.objects.get(product_id = product_id)

    # Caching product details for 1 hour
    cache.set(f'product_details_{product_id}', product, 3600)  # 1 hour in seconds

    return render(request, 'product_details.html', {'product': product})

# Eviction
def product_page(request, product_id):
    product = Product.objects.get(product_id = product_id)

    # Caching product details for 1 day
    cache.set(f'product_price_{product_id}', product.price, 86400)  # 1 day in seconds
    cache.set(f'product_review_{product_id}', product.review, 86400)  # 1 day in seconds
    cache.set(f'product_ratings_{product_id}', product.ratings, 86400)  # 1 day in seconds

    return render(request, 'product_page.html', {'product': product})

# Invalidated
def update_product_price(request, product_id, new_price):
    # Update the product's price in the database
    # update_product_price_in_database(product_id, new_price)
    Product.objects.filter(id=product_id).update(price=new_price)

    # Invalidate cached price
    cache.delete(f'product_price_{product_id}')

    return redirect('product_page', product_id=product_id)