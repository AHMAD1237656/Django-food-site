from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')

def feedback(request):
    return render(request, 'feedback.html')

def gallery(request):
    items = [
        {'name': 'Burger', 'image': 'burger.jpg'},
        {'name': 'Pizza', 'image': 'pizza.jpg'},
        {'name': 'Coke', 'image': 'coke.jpg'},
        {'name': 'Nuggets', 'image': 'nuggets.jpg'},
        {'name': 'Samosa', 'image': 'samosa.jpg'},
        {'name': 'Wings', 'image': 'wings.jpg'},
        {'name': 'Sandwich', 'image': 'sandwich.jpg'},
        {'name': 'Chips', 'image': 'chips.jpg'},
    ]
    return render(request, 'gallery.html', {'items': items})
def submit_feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')
        
        # Yahan aap data save kar sakte ho ya email bhej sakte ho
        
        # Temporary ke liye redirect ya success message dikhao
        return HttpResponse("Thank you for your feedback!")
    else:
        return redirect('feedback')  # jahan feedback form render hota hai