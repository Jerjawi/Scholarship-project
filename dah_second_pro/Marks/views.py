from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Marks
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from Files.views import SuccessMessageMixin
def super_user_marks(request):
    if request.user.is_superuser:
        context = {
            'all_marks': Marks.objects.all().order_by('-date')
        }
        return render(request, 'Marks/superusr_marks.html',context)
class DRY(UserPassesTestMixin):
    def test_func(self):
        mark = self.get_object()
        if mark.mark_student == self.request.user or self.request.user.is_superuser:
            return True
        return False

class Marks_list(LoginRequiredMixin,ListView):
    model = User
    template_name = 'Marks/MarkSpecific.html'
    def get_queryset(self):
        #self.kwargs is a dictionary ==> .get('thing') this is to get a key
        now_user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Marks.objects.filter(mark_student__username = now_user )

class Marks_Create(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Marks
    template_name = 'Marks/marks_create.html'
    fields = ['marks_name','marks']
    success_message = 'The Mark have been Created successfully'

    def form_valid(self,form):
        form.instance.mark_student = self.request.user
        return super().form_valid(form)




class Marks_Update(LoginRequiredMixin,SuccessMessageMixin,DRY,UpdateView):
    model = Marks
    template_name = 'Marks/marks_update.html'
    fields = ['marks_name','marks']
    success_message = 'The Mark have been Updated successfully'

    def form_valid(self,form):
            mark = self.get_object()
            form.instance.mark_student = mark.mark_student
            return super().form_valid(form)


class Mark_Detail(LoginRequiredMixin,DetailView):
    model = Marks
    template_name = 'Marks/Mark_detail.html'

class Mark_Delete(LoginRequiredMixin,SuccessMessageMixin,DRY,DeleteView):
    model = Marks
    template_name = 'Marks/mark_delete.html'
    success_message = 'The Mark have been Deleted successfully'

    def get_success_url(self) -> str:
        return reverse_lazy('specific_marks', kwargs = {'username' : self.object.mark_student})