from django.contrib.auth.forms import UserCreationForm # fomrulário
from django.urls import reverse_lazy # redirecionar usuário
from django.views import generic # criar uma classe base


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    # sucess_url = reverse_lazy('login')
    template_name = 'registration/register.html'
    
    def get_success_url(self):
        return reverse_lazy('login')
        # sulução para erro