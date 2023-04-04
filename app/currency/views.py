from currency.models import Rate, Source, ContactUs
from currency.forms import RateForm, SourceForm, ContactUsForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView


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

    def _slow(self):
        from time import sleep
        sleep(10)

    def _send_mail(self):
        subject = 'User ContactUs'
        # recipient = settings.DEFAULT_FROM_EMAIL
        message = f'''
        Request from: {self.object.name}.
        Reply to email: {self.object.email_from}.
        Subject: {self.object.subject},
        Body: {self.object.message}
        '''
        from currency.tasks import send_mail
        # send_mail.delay(subject, message)
        # send_mail.apply_async(args=[subject, message])
        '''
        0 - 8.59 | 9.00 - 19.00 | 19.01 23.59
           9.00  |    send      | 9.00 next day
        '''
        send_mail.apply_async(
            kwargs={'subject': subject, 'message': message},
            # countdown=20
            # eta=datetime(2023, 3, 28, 20, 49, 0)
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
    queryset = Rate.objects.all().select_related('source')


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
