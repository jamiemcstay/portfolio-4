from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Review
from .forms import ReviewForm


# Create your views here.

class ReviewList(generic.ListView):
    queryset = Review.objects.all()
    template_name = "review/index.html"
    paginate_by = 6


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
    review_list = Review.objects.filter(author=request.user).order_by('-date_created')

    #pagination: 6 reviews per page
    paginator = Paginator(review_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'review/my_reviews.html', {
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages()
    })


@login_required
def add_review(request):
        # Handle form submission
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.author = request.user
            new_review.excerpt = new_review.content[:100]
            new_review.save()
            messages.success(request, 'Review successfully added')
            return redirect("review_detail", slug=new_review.slug)
    else:
        form = ReviewForm()
    return render(request, 'review/add_review.html', {'form': form})


@login_required
def review_edit(request, slug):
    review = get_object_or_404(Review, slug=slug)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if review.author != request.user:
            messages.error(request, "You can only edit you're own album review")
            return redirect('review_detail', slug=review.slug)

        if form.is_valid():
            form.save()
            messages.success(request, "Review successfully updated")
            return redirect('review_detail', slug=review.slug)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'review/review_edit.html', {'form': form, 'review': review})

@login_required
def review_delete(request, slug):
    review = get_object_or_404(Review, slug=slug)

    if request.method == 'POST':
        if review.author != request.user:
            messages.error(request, "You can only delete you're own album review")
            return redirect('review_detail', slug=review.slug)
        review.delete()
        messages.success(request, "Review successfully deleted")
        return redirect('my_reviews')

    return render(request, 'review/review_confirm_delete.html', {'review': review})

