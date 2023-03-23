from currency.models import Rate, Source, ContactUs
from currency.forms import RateForm, SourceForm, ContactUsForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from settings import settings


class ContactListView(ListView):
    template_name = 'contact_list.html'
    queryset = ContactUs.objects.all()


class ContactDetailView(DetailView):
    template_name = 'contact_details.html'
    queryset = ContactUs.objects.all()


class ContactCreateView(CreateView):
    form_class = ContactUsForm
    template_name = 'contacts_create.html'
    success_url = reverse_lazy('index')

    def _send_mail(self):
        subject = 'User ContactUs'
        recipient = settings.DEFAULT_FROM_EMAIL
        message = f'''
        Request from: {self.object.name}.
        Reply to email: {self.object.email_from}.
        Subject: {self.object.subject},
        Body: {self.object.message}
        '''

        from django.core.mail import send_mail
        send_mail(
            subject,
            message,
            recipient,
            [recipient],
            fail_silently=False,
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_mail()
        return redirect


class ContactUpdateView(UpdateView):
    form_class = ContactUsForm
    template_name = 'contacts_update.html'
    success_url = reverse_lazy('currency:contact_us-list')
    queryset = ContactUs.objects.all()


class ContactDeleteView(DeleteView):
    template_name = 'contacts_delete.html'
    success_url = reverse_lazy('currency:contact_us-list')
    queryset = ContactUs.objects.all()


class RateListView(ListView):
    template_name = 'rates_list.html'
    queryset = Rate.objects.all()


class RateDetailView(LoginRequiredMixin, DetailView):
    template_name = 'rate_details.html'
    queryset = Rate.objects.all()


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rates_create.html'
    success_url = reverse_lazy('currency:rate-list')


class RateUpdateView(UserPassesTestMixin, UpdateView):
    form_class = RateForm
    template_name = 'rates_update.html'
    success_url = reverse_lazy('currency:rate-list')
    queryset = Rate.objects.all()

    def test_func(self):
        return self.request.user.is_superuser


class RateDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'rates_delete.html'
    success_url = reverse_lazy('currency:rate-list')
    queryset = Rate.objects.all()

    def test_func(self):
        return self.request.user.is_superuser


class SourceListView(ListView):
    template_name = 'sources_list.html'
    queryset = Source.objects.all()


class SourceDetailView(DetailView):
    template_name = 'source_details.html'
    queryset = Source.objects.all()


class SourceCreateView(CreateView):
    form_class = SourceForm
    template_name = 'sources_create.html'
    success_url = reverse_lazy('currency:source-list')


class SourceUpdateView(UpdateView):
    form_class = SourceForm
    template_name = 'sources_update.html'
    success_url = reverse_lazy('currency:source-list')
    queryset = Source.objects.all()


class SourceDeleteView(DeleteView):
    template_name = 'sources_delete.html'
    success_url = reverse_lazy('currency:source-list')
    queryset = Source.objects.all()


class IndexView(TemplateView):
    template_name = 'index.html'


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('index')
    model = get_user_model()
    fields = (
        'first_name',
        'last_name'
    )

    def get_object(self, queryset=None):
        return self.request.user
