import django_filters


from .models import * 

class ReturFilter(django_filters.FilterSet):
	class Meta:
		model = Retur
		fields = "__all__"
		