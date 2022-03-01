from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from .models import Finance
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib import messages
#if superuser

def superuser_view(request):
    if request.user.is_superuser:
        context = {
            'all_files' : Finance.objects.all().order_by('-date')
        }
        return render(request , 'Files/superuser_files.html',context)

#for messages
class SuccessMessageMixin:
    """
    Add a success message on successful form submission.
    """
    success_message = ''

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data

class DRY(UserPassesTestMixin):
    def test_func(self):
        finance = self.get_object()
        if finance.Finance_student == self.request.user or self.request.user.is_superuser:
            return True
        return False
class Finance_list(LoginRequiredMixin,ListView):
    model = User
    template_name = 'Files/FinanceSpecific.html'
    def get_queryset(self):
        #self.kwargs is a dictionary ==> .get('thing') this is to get a key
        now_user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Finance.objects.filter(Finance_student__username = now_user )
    
class Finance_Create(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Finance
    template_name = 'Files/Finance_create.html'
    fields = ['Finance_name','finance_reports']
    success_message = 'The Finanace File have been created'
    def form_valid(self,form):
        form.instance.Finance_student = self.request.user
        return super().form_valid(form)
    

    
    
class Finance_Update(LoginRequiredMixin,SuccessMessageMixin,DRY,UpdateView):
    model = Finance
    template_name = 'Files/Finance_update.html'
    fields = ['Finance_name','finance_reports']
    success_message = 'The Finanace File have been updated'

    def form_valid(self,form):
            file = self.get_object()
            form.instance.Finance_student = file.Finance_student
            return super().form_valid(form)
    
    
class Finance_Detail(LoginRequiredMixin,DetailView):
    model = Finance
    template_name = 'Files/Finance_detail.html'

class Finance_Delete(DRY,SuccessMessageMixin,DeleteView):
    model = Finance
    template_name = 'Files/Finance_delete.html'
    success_message = 'The Finanace File have been Deleted Successfully'

    def get_success_url(self) -> str:
        return reverse_lazy('files_of', kwargs = {'username' : self.object.Finance_student})
    