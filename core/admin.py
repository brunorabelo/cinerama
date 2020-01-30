from django.contrib import admin

from core.models import ActivityLog,Movie,Rating


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('tmdb_id', 'title', 'overview','release_date')

    actions=['update_movies']

    #todo fazer ação para atualizar filmes selecionados
    def update_movies(self,request,queryset):
        for movie in queryset:
            movie.update_from_internet()

    update_movies.short_description = 'Atualizar filmes selecionados'


    


admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Rating)

