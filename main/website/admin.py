from django.contrib import admin
from .models import TeamMember, CaseStudy

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    search_fields = ('name', 'role')


@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'created_at')
    search_fields = ('title', 'subtitle')