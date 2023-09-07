from .models import Season

def context(request):
    dict = {}
    seasons = Season.objects.all()
    
    for season in seasons:
        dict[season.key] = season.url

    return dict

