from urllib.request import Request

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram.pets.forms import PetForm, PetDeleteForm
from petstagram.pets.models import Pet


class AddPetView(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})

# def pet_add_view(request):
#     form = PetForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('profile-details', pk=1)
#
#     context = {'form': form}
#     return render(request, 'pets/pet-add-page.html', context)


class EditPetView(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'
    context_object_name = 'pet'

    def get_success_url(self):
        return reverse_lazy(
            'pet-details',
            kwargs={
                'username': self.kwargs['username'],
                'pet_slug': self.kwargs['pet_slug'],
            }
        )
# def pet_edit_view(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#     if request.method == 'GET':
#         form = PetForm(instance=pet, initial=pet.__dict__)
#     else:
#         form = PetForm(request.POST, instance=pet)
#         if form.is_valid():
#             form.save()
#             return redirect('pet-details', username, pet_slug)
#
#     context = {'form': form}
#
#     return render(request, 'pets/pet-edit-page.html', context=context)


class DeletePetView(DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    context_object_name = 'pet'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})

    def get_object(self, queryset=None):
        return Pet.objects.get(slug=self.kwargs['pet_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PetDeleteForm(instance=self.object.__dict__)
        return context

    def delete(self, request, *args, **kwargs):
        pet = self.get_object()
        pet.delete()
        return redirect(self.get_success_url())
#
# def pet_delete_view(request: Request, username, pet_slug) -> HttpResponse:
#     pet = Pet.objects.get(slug=pet_slug)
#     if request.method == 'POST':
#         pet.delete()
#         return redirect('profile-details', pk=1)
#     form = PetDeleteForm(instance=pet.__dict__)
#     context = {'form': form}
#
#     return render(request, 'pets/pet-delete-page.html', context=context)


class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = self.object.photo_set.all()
        context['comment_form'] = self.object.photo_set.all()


# def pet_details_view(request: Request, username, pet_slug) -> HttpResponse:
#     pet = Pet.objects.get(slug=pet_slug)
#     all_photos = pet.photo_set.all()
#
#     context = {
#         'pet': pet,
#         'all_photos': all_photos,
#     }
#
#     return render(request, 'pets/pet-details-page.html', context=context)
