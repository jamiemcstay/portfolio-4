from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm


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


@login_required
def my_reviews(request):
    #Fetch only logged in users reviews
    reviews = Review.objects.filter(author=request.user).order_by('-date_created')

    # Handle form submission
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.author = request.user
            new_review.excerpt = new_review.content[:100]
            new_review.save()
            return redirect("my_reviews")
    else:
        form = ReviewForm()
    return render(request, 'my_reviews.html', {'reviews': reviews, 'form': form})

