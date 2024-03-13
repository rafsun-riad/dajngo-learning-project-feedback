from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm

# Create your views here.


def review(request):
    # if request.method == 'POST':
    #     entered_username = request.POST['username']
    #     if entered_username == "":
    #         return render(request, "reviews/review.html", {"has_error": True})
    #     return HttpResponseRedirect("/thank-you")

    form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form,
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
