from django.shortcuts import render

# Create your views here.



def main(request):
    return render(
    	    request=request,
    	    template_name="infos/homepage.html",
    	    context={'title': 'Home'}
   )


def me(request):
    return render(
    	    request=request,
    	    template_name="infos/me.html",
    	    context={'title': 'About me'}
   )


def contact(request):
    return render(
    	    request=request,
    	    template_name="infos/contact.html",
    	    context={'title': 'Contact'}
   )
