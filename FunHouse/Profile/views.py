from django.views import generic
from .models import Profile
from django.shortcuts import render_to_response,get_object_or_404,render
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request,pk):
    if  request.user == 'POST':
        form= ProfileForm(request.POST,instance=request.user.profile)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/profile/'+str(request.user.profile.pk))
    user=request.user
    profile=user.profile
    form=ProfileForm(instance=profile)
    object=get_object_or_404(Profile,pk=pk)
    args={'form':form,'object':object}
    return render(request,'profile/user_profile.html',args)


# class profile(generic.DetailView):
#     model = Profile
#     template_name = 'profile/user_profile.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(profile, self).get_context_data(**kwargs)
#         context['form'] = ProfileForm
#         return context
#
# class profileForm(generic.FormView):
#     form_class = ProfileForm
#     success_url = '/home/'
#     def form_valid(self, form):
#         form=Profile(instance==)



