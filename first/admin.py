from django.contrib import admin

from first.models import Donate
from first.models import Fund
from first.models import Feedback
from first.models import Don
from first.models import Total_Donate
# Register your models here.

admin.site.register(Donate)
admin.site.register(Fund)
admin.site.register(Feedback)
admin.site.register(Don)
admin.site.register(Total_Donate)