from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404


# Create your views here.

from .models import Product

# class based view (bit complicated) wrt function based views (which we already did) 

class ProductListView(ListView):
	queryset	= Product.objects.all()
	template_name= "products/list.html"

	#def get_context_data(self,**kwargs):									#important function for all classes, gets you the conext
	#	context = super().get_context_data(**kwargs)					# this is just to get stuff disl=palyed in cmd
	#	print(context)
	#	return context


# doing the same same thing with function based view

def product_list_view(request):
	queryset	= Product.objects.all()
	context		={
		'object_list': queryset
	}
	return render(request,"products/list.html",context)

class ProductDetailSlugView(DetailView):
	queryset	= Product.objects.all()
	template_name= "products/detail.html"

	def get_object(self,*args,**kwargs):
		request	= self.request
		slug 	= self.kwargs.get('slug')

		try:
			instance= Product.objects.get(slug=slug)
		except Product.DoesNotExist:
			raise Http404("Not found")
		except Product.MultipleObjectsReturned:
			qs = Product.objects.filter(slug=slug)
			instance = qs.first()
		except:
			raise Http404("uhmmmm")
		return instance

class ProductDetailView(DetailView):
	queryset	= Product.objects.all()
	template_name= "products/detail.html"
	print(queryset)

	#def get_context_data(self,**kwargs):						 #important function for all classes, gets you the conext
	#	context = super().get_context_data(**kwargs)					# this is just to get stuff disl=palyed in cmd
	#	print(context)
	#	return context

def product_detail_view(request,pk=None, *args,**kwargs):
	instance	= Product.objects.get(pk=pk)
	print(Product.objects.all())
	#instance	= get_object_or_404(Product, pk=pk)
	try:
		instance	= Product.objects.get(pk=id)
	except Product.DoesNotExist:
		print("no product")
		raise Http404("product illa")
	except:
		print("huh")

	context		={
		'object': instance
	}
	return render(request,"products/detail.html",context)