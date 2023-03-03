from django.urls import path

from currency.views import (
    ContactListView,
    ContactDetailView,
    ContactCreateView,
    ContactUpdateView,
    ContactDeleteView,
    RateListView,
    RateCreateView,
    RateUpdateView,
    RateDeleteView,
    RateDetailView,
    SourceListView,
    SourceCreateView,
    SourceUpdateView,
    SourceDeleteView,
    SourceDetailView,
)

app_name = 'currency'

urlpatterns = [
    path('contact_us/list/', ContactListView.as_view(), name='contact_us-list'),
    path('contact_us/details/<int:pk>/', ContactDetailView.as_view(), name='contact_us-details'),
    path('contact_us/create/', ContactCreateView.as_view(), name='contact_us-create'),
    path('contact_us/update/<int:pk>/', ContactUpdateView.as_view(), name='contact_us-update'),
    path('contact_us/delete/<int:pk>/', ContactDeleteView.as_view(), name='contact_us-delete'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source-details'),
]
