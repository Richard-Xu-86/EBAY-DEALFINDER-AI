from django.shortcuts import render
from .scrapers import search_ebay
import json

def home(request):
    query = request.GET.get("query", "")
    marketplace_id = request.GET.get("marketplace", "EBAY_CA")

    with open("zone.json") as f: #With ensures json is closed after beign read
        marketplaces = json.load(f)

    cheapest, best_reviewed = [], []

    if query:
        cheapest, best_reviewed = search_ebay(query, marketplace_id) #throw to search_ebay function

    return render(request, "search/home.html", { #send back to html
        "cheapest": cheapest,
        "marketplaces": marketplaces,
        "selected_marketplace": marketplace_id,
        "best_reviewed": best_reviewed,
        "query": query,
    })