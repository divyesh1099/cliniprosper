# decorators.py
from django.shortcuts import redirect
from home.models import Subscription
from django.contrib import messages

def user_is_subscribed(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect to login if user is not authenticated
        else:
            try:
                subscription = Subscription.objects.get(user=request.user)
                is_subscription_active = subscription.is_active
            except Subscription.DoesNotExist:
                is_subscription_active = False

            if not is_subscription_active:
                messages.success(request, "You need to subscribe to access this page.", extra_tags='bg-green-100 text-green-700 border border-green-400')
                return redirect('home:services')  # Redirect to subscription services page

        return function(request, *args, **kwargs)
    return wrap
