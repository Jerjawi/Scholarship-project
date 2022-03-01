from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def regirster(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Hello {username} login Now' )
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request , 'User/register.html', {'form': form})

def start_view(request):
    return render(request, 'User/start_view.html')