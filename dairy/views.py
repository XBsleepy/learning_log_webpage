from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import DairyItemForm
from django.utils import timezone
from .models import DairyItem
from django.http import Http404
# Create your views here.
@login_required
def dairy_list(request):
    """Show all dairy items."""
    dairy_items = DairyItem.objects.filter(owner=request.user).order_by('date_added')
    context = {'dairy_items': dairy_items}
    return render(request, 'dairy/dairy_list.html', context)
@login_required
def add_dairy(request):
    """Add a new dairy item."""
    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form = DairyItemForm()
    else:
        # POST提交的数据，对数据进行处理
        form = DairyItemForm(data=request.POST)
        if form.is_valid():
            new_dairy_item = form.save(commit=False)
            new_dairy_item.owner = request.user
            if not new_dairy_item.date_added:
                new_dairy_item.date_added = timezone.now()
            new_dairy_item.save()
            return redirect('dairy:dairy_list') 
    context = {'form': form}
    return render(request, 'dairy/add_dairy.html', context)

def delete_dairy(request, dairy_id):
    """Delete a dairy item."""
    dairy_item = DairyItem.objects.get(id=dairy_id)
    if dairy_item.owner != request.user:
        raise Http404
    dairy_item.delete()
    return redirect('dairy:dairy_list')