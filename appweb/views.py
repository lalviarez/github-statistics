from django.shortcuts import render
from .githubapi import Githubapi

# Create your views here.
def list(request):
    country = request.GET.get("country", "")
    if country:
        g = Githubapi()
        most_popular_repos = g.getMostPopularReposByCountry(country)
        most_collaborators_repos = g.getMostCollaboratorsReposByCountry(country)
    else:
        most_popular_repos = []
        most_collaborators_repos = []

    return render(request, 'appweb/list.html', {'country': country, 'most_popular_repos': most_popular_repos, 
                                                'most_collaborators_repos': most_collaborators_repos})
