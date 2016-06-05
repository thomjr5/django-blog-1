from django.shortcuts import render
# Create your vierws here.
def post_list(request):
    return render(request, 'blog/post_list.html',{})
