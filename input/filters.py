import django_filters


from .models import * 

class InputFilter(django_filters.FilterSet):
	class Meta:
		model = Input
		fields = "__all__"
		