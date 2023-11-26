from .models import Subscription

def global_context(request):
    is_subscription_active = False
    if request.user.is_authenticated:
        try:
            subscription = Subscription.objects.get(user=request.user)
            is_subscription_active = subscription.is_active
        except Subscription.DoesNotExist:
            pass
    return {'path': request.path, 'is_subscription_active': is_subscription_active}