from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import AddTweetForm
from .models import Tweets


@login_required
def add_tweet_view(request):
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweets.objects.create(
                text=data.get("text"),
                user=request.user
            )
            return HttpResponseRedirect(reverse("home"))
    form = AddTweetForm()
    return render(request, "generic_form.html", {
        "title": "Twitter Clone",
        "form": form
    })
