from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.utils import timezone
import datetime
from decorators import *

# Create your views here.
@user_is_subscribed
def index(request):
    lectures = Lecture.objects.all().order_by('-date')  # Ordering lectures by date

    # Handling the search query
    query = request.GET.get('q')
    if query:
        # Attempt to parse the query as a date
        try:
            query_date = datetime.datetime.strptime(query, '%Y-%m-%d').date()
            date_filter = Q(created_at__date=query_date)
        except ValueError:
            # If the query is not a valid date, consider it a text search
            date_filter = Q(title__icontains=query) | Q(description__icontains=query)

        lectures = lectures.filter(date_filter)

    # Pass current time to the template for comparison
    current_time = timezone.now()
    context = {
        'lectures': lectures,
        'current_time': current_time
    }
    return render(request, 'lecture/index.html', context)