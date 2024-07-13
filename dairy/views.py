from django.shortcuts import render,redirect
from .models import dairy_item
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dairy_list(request):
    """Show all dairy items."""
    dairy_items = dairy_item.objects.filter(owner=request.user).order_by('date_added')
    context = {'dairy_items': dairy_items}
    return render(request, 'dairy/dairy_list.html', context)
@login_required
def add_dairy(request):
    """Add a new dairy item."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        return render(request, 'dairy/add_dairy.html')
    else:
        # POST data submitted; process data.
        text = request.POST['text']
        mood = request.POST['mood']
        new_dairy = dairy_item(text=text, mood=mood, owner=request.user)
        new_dairy.save()
        return redirect('dairy:dairy_list')