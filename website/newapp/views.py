from django.shortcuts import render, get_object_or_404, redirect
from .models import video, comment

# Create your views here.
def home(request):
    items = video.objects.all()
    if request.method =='POST':
        #print("post methos ")
        searched_data = request.POST.get('search')
        print("the search data is : "+ str(searched_data))
        videos = video.objects.filter(title__icontains=searched_data)
        return render(request, 'index.html', {'items': videos})
    return render(request, 'index.html', {'items': items})

def details(request, id):
    item = get_object_or_404(video, id=id)
    items = comment.objects.filter(video=item)

    if request.method == "POST":
        print("method is POST")
        commentt = request.POST.get('comment')  # Get the comment from the POST data

        if commentt:  # Check if the commentt variable is not empty
            user = request.user
            new_comment = comment(video=item, content=commentt, user= user)
            new_comment.save()

        return redirect('details', id=id)

    print("method is GET")
    item = {
        'item': item,
        'items' : items
    }
    return render(request, 'details.html', item)


def video_search(request):

    if request.method =='POST':
        searched_data = request.POST.get('search')
        videos = video.objects.filter(titile__tcontent=searched_data)
        return render(request, 'search_results.html', {'videos': videos})
    return redirect('home')