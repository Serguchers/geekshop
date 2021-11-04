import datetime
import json

from django.shortcuts import render

with open('context_data/data.json', 'r') as f:
    context_data = json.load(f)

main_data = context_data['main']
products_data = context_data['products']
contact_data = context_data['contact']


def main(request):

    content = {"title": main_data['title'], "products": main_data['products']}
    return render(request, "mainapp/index.html", content)


def products(request):

    content = {"title": products_data['title'], "links_menu": products_data['links_menu'], "same_products": products_data['same_products']}
    return render(request, "mainapp/products.html", content)


def contact(request):

    visit_date = datetime.datetime.now()

    content = {"title": contact_data['title'], "visit_date": visit_date, "locations": contact_data['locations']}
    return render(request, "mainapp/contact.html", content)