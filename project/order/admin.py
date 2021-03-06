from django.contrib import admin
from order.models import Klijent, Narudzba, NarucenArtikal, Kosarica, KosaricaArtikal

class NarudzbaAdmin(admin.ModelAdmin):
  list_display=('id', 'klijent', 'sifra', 'status', 'created', 'modified', 'zabiljezba', 'status',)

class NarucenArtikalAdmin(admin.ModelAdmin):
  list_display=('id', 'ime', 'kolicina', 'std_kolicina', 'jedinice', 'kratica_dobavljaca', 'jedinicna_cijena', 'created',)

class KosaricaAdmin(admin.ModelAdmin):
  list_display=('id', 'djelatnik',)
#  exclude = ('klijent',)

class KosaricaArtikalAdmin(admin.ModelAdmin):
  list_display=('id', 'kosarica',)
  exclude = ('artikal',)

admin.site.register(Klijent)
admin.site.register(Narudzba, NarudzbaAdmin)
admin.site.register(NarucenArtikal, NarucenArtikalAdmin)
 
admin.site.register(Kosarica, KosaricaAdmin)
admin.site.register(KosaricaArtikal, KosaricaArtikalAdmin)
