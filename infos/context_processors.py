from django.urls import reverse

def menu_dict(request):
    return {'con': {'Home': reverse('main'), 'About me': reverse('me'), 'Contact': reverse('contact')}}



