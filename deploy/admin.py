from django.contrib import admin

# Register your models here.
import models

class HostAdmin(admin.ModelAdmin):
    list_display = ('id','name','ip_addr','memo')
    filter_horizontal = ('host_groups','project')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','Type','deploy_dir')

admin.site.register(models.Host,HostAdmin)
admin.site.register(models.HostGroup)
admin.site.register(models.Project,ProjectAdmin)
