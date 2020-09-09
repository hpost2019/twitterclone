from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddTweetForm
from .models import Tweets
from .helpers import parse_tweet


# @login_required
# def add_tweet_view(request):
#     if request.method == "POST":
#         form = AddTweetForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             tweet = Tweets.objects.create(
#                 text=data.get("text"),
#                 user=request.user
#             )
#             parse_tweet(tweet)
#             return HttpResponseRedirect(reverse("home"))
#     form = AddTweetForm()
#     return render(request, "generic_form.html", {
#         "title": "Twitter Clone",
#         "form": form
#     })


class AddTweetView(LoginRequiredMixin, TemplateView):

    def get(self, request):
        form = AddTweetForm()
        return render(request, "generic_form.html", {
            "title": "Twitter Clone",
            "form": form
        })

    def post(self, request):
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweets.objects.create(
                text=data.get("text"),
                user=request.user
            )
            parse_tweet(tweet)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "generic_form.html", {
                "title": "Twitter Clone",
                "form": form
            })
