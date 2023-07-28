from django.shortcuts import render, get_object_or_404, redirect
from .models import video, comment, chategory

# Create your views here.
def home(request):
    selected_category = chategory.objects.all()
    items = video.objects.all()
    print(items)
    if request.method =='POST':
     
        searched_data = request.POST.get('search')
        print(searched_data)
        videos = video.objects.filter(title__icontains=searched_data)
        return render(request, 'index.html', {'items': videos})
    
    return render(request, 'index.html', {'items': items, 'chategories': selected_category})

def details(request, id):
    item = get_object_or_404(video, id=id)
    items = comment.objects.filter(video=item)

    if request.method == "POST":
       
        commentt = request.POST.get('comment')  # Get the comment from the POST data

        if commentt:  # Check if the commentt variable is not empty
            user = request.user
            new_comment = comment(video=item, content=commentt, user= user)
            new_comment.save()

        return redirect('details', id=id)

  
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

def category_template(request, category_id):
    selected_category = get_object_or_404(chategory, pk=category_id)
    print(selected_category)
    videos = video.objects.filter(chategory=selected_category)
    print(videos)
    context = {
        'category': selected_category,
        'videos': videos,
    }
    return render(request, 'category_template.html', context)