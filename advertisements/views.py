import json

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from advertisements.models import Advertisement
from advertisements.serializers import *
from categories.models import Category


@method_decorator(csrf_exempt, name='dispatch')
class IndexView(View):
    def get(self, request):
        return JsonResponse({'status': 'ok'}, status=200)


class AdsListView(ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementListSerializer

    def get(self, request, *args, **kwargs):

        cat_id_list = request.GET.getlist("cat", None)
        name_text = request.GET.get('text', None)
        location_text = request.GET.get('location', None)
        price_from_criteria = request.GET.get('price_from', None)
        price_to_criteria = request.GET.get('price_to', None)

        category_query = None

        if category_query:
            for category in cat_id_list:
                if not category_query:
                    category_query = Q(category_id=category)
                else:
                    category_query |= Q(category_id=category)
            if category_query:
                self.queryset = self.queryset.filter(category_query)

        if name_text:
            self.queryset = self.queryset.filter(name__icontains=name_text)

        if location_text:
            self.queryset = self.queryset.filter(author_id__location__name__icontains=location_text)

        if price_from_criteria and not price_to_criteria:
            self.queryset = self.queryset.filter(Q(price__gte=price_from_criteria))

        if price_to_criteria and not price_from_criteria:
            self.queryset = self.queryset.filter(Q(price__lte=price_to_criteria))

        if price_to_criteria and price_from_criteria:
            self.queryset = self.queryset.filter(Q(price__gte=price_from_criteria), Q(price__lte=price_to_criteria))

        return super().get(request, *args, **kwargs)


class AdEntityView(RetrieveAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementDetailSerializer
    permission_classes = [IsAuthenticated]


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Advertisement
    fields = ["name", "author_id", "price", "description", "category_id"]

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        author = get_object_or_404(get_user_model(), pk=data.get('author_id'))
        category = get_object_or_404(Category, pk=data.get('category_id'))

        ad = Advertisement.objects.create(
            name=data.get('name'),
            author=author,
            price=data.get('price'),
            description=data.get('description'),
            category=category,
            is_published=data.get('is_published')
        )

        ad.save()

        response = {'id': ad.id,
                    'name': ad.name,
                    'author_id': ad.author.id,
                    'author': ad.author.first_name,
                    'price': ad.price,
                    'description': ad.description,
                    'is_published': ad.is_published,
                    'category_id': ad.category_id,
                    'image': ad.image.url if ad.image else None
                    }

        return JsonResponse(response, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Advertisement
    fields = ("name", "author", "price", "description", "category")

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        data = json.loads(request.body)

        self.object.name = data.get('name')
        self.object.author = get_object_or_404(get_user_model(), pk=data.get('author_id'))
        self.object.price = data.get('price')
        self.object.description = data.get('description')
        self.object.category= get_object_or_404(Category, pk=data.get('category_id'))

        self.object.save()

        response = {'id': self.object.id,
                    'name': self.object.name,
                    'author_id': self.object.author.id,
                    'author': self.object.author.first_name,
                    'price': self.object.price,
                    'description': self.object.description,
                    'is_published': self.object.is_published,
                    'category_id': self.object.category.id,
                    "category_name": self.object.category.name,
                    'image': self.object.image.url if self.object.image else None
                    }
        return JsonResponse(response, status=200)


class AdDeleteView(DestroyAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementDestroySerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdImageUploadView(UpdateView):
    model = Advertisement
    fields = ["name", "author", "price", "description", "category"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        self.object = self.get_object()

        image = request.FILE['image']
        self.object.image = image

        #self.object.author = get_object_or_404(get_user_model(), pk=self.object.author.id)
        #self.object.category = get_object_or_404(Category, pk=self.object.category.id)

        self.object.save()

        response = {'id': self.object.id,
                    'name': self.object.name,
                    'author_id': self.object.author.id,
                    'author': self.object.author.first_name,
                    'price': self.object.price,
                    'description': self.object.description,
                    'is_published': self.object.is_published,
                    'category_id': self.object.category.id,
                    "category_name": self.object.category.name,
                    'aimage': self.object.image.url if self.object.image else None
                    }
        return JsonResponse(response, status=200)
