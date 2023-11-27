from django.shortcuts import render
from .models import *
from django.db.models import Q
import datetime
# Create your views here.
def index(request):
    notes = Note.objects.all().order_by('-upload_date')
    # Handling the search query
    query = request.GET.get('q')
    if query:
        # Attempt to parse the query as a date
        try:
            query_date = datetime.datetime.strptime(query, '%Y-%m-%d').date()
            date_filter = Q(upload_date__date=query_date)
        except ValueError:
            # If the query is not a valid date, skip date filtering
            date_filter = Q()

        notes = notes.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            date_filter
        )

    context={
        'notes': notes
    }
    return render(request, 'note/index.html', context)