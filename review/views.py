from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Review


# Create your views here.

class ReviewList(generic.ListView):
    queryset = Review.objects.all()
    template_name = "review/index.html"
    paginate_by = 9


def review_detail(request, slug):
    """
    Display the full review for the user

    **Context**

    ``review``
        an instance of the :model: `review.Review`

    **Template:**

        :template:`review/review_detail.html`
    """

    review = get_object_or_404(Review, slug=slug)

    return render(
        request,
        "review/review_detail.html",
        {"review": review},
    )

    
    

