from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DetailView,CreateView
from Files.views import SuccessMessageMixin
def all_profiles(request):
    if request.user.is_superuser:
        context = {
            'all_profile': Profile.objects.all()
        }
        return render(request, 'Profile/all_profiles.html',context)
        
class DRY(UserPassesTestMixin):
    def test_func(self):
        profile = self.get_object()
        if profile.user == self.request.user or self.request.user.is_superuser:
            return True
        return False

class Protofile(LoginRequiredMixin,DRY,DetailView):
    model = Profile
    template_name = 'Profile/profile_detail.html'
    

class Profile_Create(LoginRequiredMixin,CreateView):
    model = Profile
    template_name = 'Profile/Profile_create.html'
    fields = ['age','email','phone_number','living_place','id_number','specialization',
    'year_of_graduation','achieved_hours','still_hours','image','Cumulative_average',
    'seimester_average','price_of_hour']
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Profile_Update(LoginRequiredMixin,SuccessMessageMixin,DRY,UpdateView):
    model = Profile
    template_name = 'Profile/Profile_update.html'
    fields = ['age','email','phone_number','living_place','id_number','specialization',
    'year_of_graduation','achieved_hours','still_hours','image','Cumulative_average',
    'seimester_average','price_of_hour']
    success_message = 'The Profile have been Updated successfully'

    def form_valid(self,form):
        profile = self.get_object()
        form.instance.user = profile.user
        return super().form_valid(form)