from django.contrib import admin
from .models import Tareas
from .models import Arancel
from .models import Caeb
from .models import Nandina
from .models import Productos
from .models import RelCaebCaeb
from .models import RelCcpCaeb
from .models import Sinonimos


admin.site.register(Tareas)
admin.site.register(Arancel)
admin.site.register(Caeb)
admin.site.register(Nandina)
admin.site.register(Productos)
admin.site.register(RelCaebCaeb)
admin.site.register(RelCcpCaeb)
admin.site.register(Sinonimos)